import logging

from protocol.channelEntity import ChannelEntity
from protocol.frameSensorAdDataItem import FrameSensorAdDataItem
from protocol.frameSensorDataItem import FrameSensorDataItem
from utils.byteUtils import ByteUtils
from utils.dateUtils import DateUtils


logger = logging.getLogger('service.log')


class FrameInstructionResult:
    CHANNEL_DATA_SIZE = 4
    DATA_POS_START = 3
    # /**
    #  读取数据回应	XX	 03     04	        XX	XX	XX	XX
    #  说明	        地址 功能码	数据长度	4个字节数据	    CRC校验

    def __init__(self, packet_address, bytes_data):
        self.arr_bytes = bytes_data
        self.functionCode = packet_address  # =寄存器地址， 根据数据的寄存器地址来判断当前进行的是什么操作
        self.channel = ChannelEntity()

    def ParseChannelData(self, data, chan_id):
        if self.functionCode <= 0x0100:
            return False
        arr_item = bytearray(FrameInstructionResult.CHANNEL_DATA_SIZE)

        ByteUtils.CopyByteArray(arr_item, data, FrameInstructionResult.DATA_POS_START, FrameInstructionResult.CHANNEL_DATA_SIZE)
        sen = FrameSensorDataItem(arr_item, DateUtils.now2full())
        if not sen.Parse():
            return False

        # 保存数据
        self.channel.id = chan_id
        self.channel.senorValue = sen.senValue

    def ParseChannelAdData(self, data, chan_id):
        if self.functionCode <= 0x0100:
            return False
        arr_item = bytearray(FrameInstructionResult.CHANNEL_DATA_SIZE)

        ByteUtils.CopyByteArray(arr_item, data, FrameInstructionResult.DATA_POS_START, FrameInstructionResult.CHANNEL_DATA_SIZE)
        sen = FrameSensorAdDataItem(arr_item, DateUtils.now2full())
        if not sen.Parse():
            return False

        # 保存数据
        self.channel.id = chan_id
        self.channel.adValue = sen.senValue


