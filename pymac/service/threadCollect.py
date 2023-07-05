import logging
import threading
import time

from base.serialDevice import SerialDevice
from devices.AppResource import AppResource
from protocol.channelEntity import ChannelEntity
from protocol.frameInstructionResult import FrameInstructionResult
from protocol.frameReadRegister import FrameReadRegister
from utils.byteUtils import ByteUtils
from utils.crcUtils import CrcUtils
from utils.csvutils import CsvUtils
from protocol.packConst import RegAddress
from utils.dateUtils import DateUtils

logger = logging.getLogger('service.log')

class ThreadCollect(threading.Thread):
    DATA_PACKET_SIZE = 9

    def __init__(self):
        threading.Thread.__init__(self)
        # actionCode = (int)REG_ADDRESS.COLLECT
        self.actionCode = RegAddress.COLLECT
        self.bool_exit = False
        self.bool_pause = False
        self.list_channel = []
        self.list_serial = []
        self.started = False
        self.appResource = AppResource.ins()
        self.bautrate = 9600

    def reset(self):
        self.bool_exit = False
        self.bool_pause = False

    def pause(self):
        self.bool_pause = True

    def resume(self):
        self.bool_pause = False

    def stop(self):
        self.bool_exit = False

    def loadChannelList(self):
        csvutils = CsvUtils()
        self.list_channel = []
        lst = csvutils.readChannelList()
        app = AppResource.ins()
        app.clearChannels()
        for chan in lst:
            # 1	99002310	COM19	1	35	1
            item = ChannelEntity()
            item.id = int(chan[0])
            item.nodeNum = int(chan[1])
            item.port = chan[2]
            item.slaveAddr = int(chan[3])
            item.sensorType = int(chan[4])
            item.channel = int(chan[5])
            self.list_channel.append(item)
            app.addChannel(item)

    def closeAllSerial(self):
        for item in self.list_serial:
            item.closeSerial()

    def addSerial(self, port, bautrate):
        item = SerialDevice()
        item.openSerial(port, bautrate)
        self.list_serial.append(item)
        return item

    def findSerial(self, port):
        for item in self.list_serial:
            if item.port == port:
                return item
        # end for
        return None

    def getSerial(self, port, bautrate):
        item = self.findSerial(port)
        if item is not None:
            return item

        item = self.addSerial(port, bautrate)
        return item

    def stopCollecting(self):
        self.bool_pause = True
        self.closeAllSerial()

    def startCollecting(self):
        self.bool_pause = False

    def endCollecting(self):
        self.bool_pause = True
        self.bool_exit = True


    def run(self):
        self.started = True
        self.loadChannelList()
        check_result = ""
        while not self.bool_exit:
            if AppResource.ins().bool_exit or self.bool_exit:
                print("Collecting thread exited")
                logger.info("Collecting thread exited")
                break

            if self.bool_pause:
                time.sleep(1)

                continue
            time.sleep(3)

            for chan in self.list_channel:
                if AppResource.ins().bool_exit or self.bool_exit:
                    print("Collecting thread exited")
                    logger.info("Collecting thread exited")
                    break
                serial_dev = self.getSerial(chan.port, self.bautrate)
                if serial_dev is None:
                    continue

                # 如果串口没有打开，则打开
                if not serial_dev.isOpen():
                    if not serial_dev.openSerial(chan.port, self.bautrate):
                        continue

                # nChannel = chan.channel - 1
                # read sensor value
                self.ReadDataFromSensor(chan, 0, serial_dev)
                # read AD value
                self.ReadDataFromSensor(chan, 1, serial_dev)



        # end
        self.closeAllSerial()
        self.end()
        print("THREAD COLLECTING EXITED")
        logger.info("THREAD COLLECTING EXITED")

    def ReadDataFromSensor(self, chan, channel, serial_dev):
        # 地址 = 类型号（高字节）+通道号 * 2(低字节)
        memAddress = chan.sensorType << 8
        memAddress += (channel * 2)
        pack = FrameReadRegister([FrameReadRegister.READ_DATA_ADDR, chan.slaveAddr, memAddress, RegAddress.COLLECT_LEN])
        bytesArr = pack.ToByeArray()
        if serial_dev.writeBytes(bytesArr) > 0:
            buf_byte = bytearray()
            res = 0
            for s in range(20):
                time.sleep(0.5)
                res = serial_dev.readBytes(buf_byte)
                if res > 0:
                    break
            if res > 0:
                self.parseSensorBytesData(buf_byte, chan, pack, channel)

    def parseSensorBytesData(self, buf_byte, chan, pack, channel):
        # 采集数据得到的包长度是固定的 07030443C7F3333CAF
        n_item = round(len(buf_byte) / ThreadCollect.DATA_PACKET_SIZE)
        buf_item = []
        # 可能会有多组数据
        for i in range(0, n_item):
            if AppResource.ins().bool_exit or self.bool_exit:
                print("Collecting thread exited")
                logger.info("Collecting thread exited")
                break
                # 先取出一组数据
            if len(buf_byte) < (i + 1) * ThreadCollect.DATA_PACKET_SIZE:
                break
            pos_from = i * ThreadCollect.DATA_PACKET_SIZE
            pack_size = ThreadCollect.DATA_PACKET_SIZE
            arr_item = bytearray(pack_size)
            ByteUtils.CopyByteArray(arr_item, buf_byte, pos_from, pack_size)
            buf_item = bytes(arr_item)
            if CrcUtils.CheckPacket(buf_item):
                if pack.Parse(buf_item) > 0:
                    # 第一个字节是地址
                    bus_addr = pack.fldAddress.buf[0]
                    if bus_addr == chan.slaveAddr:
                        if 0 == channel:
                            self.parseSensorData(chan.id, self.actionCode, buf_byte)
                        if 1 == channel:
                            self.parseAdData(chan.id, self.actionCode, buf_byte)
            # end if
        # end for

    def closeAllSerial(self):
        for chan in self.list_channel:
            serial_dev = self.getSerial(chan.port, self.bautrate)
            if serial_dev is None:
                continue
            serial_dev.closeSerial()

    def parseSensorData(self, chan_id, bus_addr, bytes_data):
        instruction = FrameInstructionResult(bus_addr, bytes_data)
        instruction.ParseChannelData(bytes_data, chan_id)
        self.appResource.updateChannelValue(chan_id, instruction.channel.senorValue)
        str_value = "{\"ID\":" + str(instruction.channel.id) + ",\"calibrateDate\":\"" + DateUtils.now2full() + "\", \"VALUE\":" + str(instruction.channel.senorValue) + "}"
        self.appResource.sendMessage("COLLECT_SENSOR_VALUE", str_value)
        # 通知页面更新

    def parseAdData(self, chan_id, bus_addr, bytes_data):
        instruction = FrameInstructionResult(bus_addr, bytes_data)
        instruction.ParseChannelAdData(bytes_data, chan_id)
        self.appResource.updateChannelAdValue(chan_id, instruction.channel.senorValue)
        str_value = "{\"ID\":" + str(instruction.channel.id) + ",\"calibrateDate\":\"" + DateUtils.now2full() + "\", \"VALUE\":" \
                    + "\"" + str(
            instruction.channel.adValue) + "\"}"
        self.appResource.sendMessage("COLLECT_AD_VALUE", str_value)
        # 通知页面更新




