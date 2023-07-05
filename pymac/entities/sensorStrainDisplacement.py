#coding=utf-8
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils
from utils.crcUtils import CrcUtils

class SensorStrainDisplacement:
    def __init__(self):
        #振弦传感器
        self.sensorName="vibration wire"
        #总线地址，取值0-255
        self.addr=0x00
        self.readAddrCode=0x6E
        self.readDataCode=0x03
        self.typeCode=0x05
        self.channel = 0x00
    def readBusAddress(self):
        #00 03 00 30 00 01 85 D4
        arrBytes = []
        self.addr = 0x00
        arrBytes.append(self.addr)
        arrBytes.append(self.readAddrCode)
        arrBytes.append(0x00)
        arrBytes.append(0x30)
        arrBytes.append(0x00)
        arrBytes.append(0x01)
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append( crcBytes[0] )
        arrBytes.append( crcBytes[1] )
        print( StrUtils.bytesToStr( arrBytes))
        return arrBytes
    def parse(self,data):
        #00 03 02 00 01 44 44
        
        return 0

    def readData(self):
        # 发送数据：01 03 00 00 00 02 C4 0B
        # 数据说明：本机地址指令寄存器地址寄存器数量CRC 校验
        arrBytes = []
        self.addr = 0x01
        arrBytes.append(self.addr)
        arrBytes.append(self.readDataCode)
        arrBytes.append(ByteUtils.int2bytes(0x00))
        arrBytes.append(ByteUtils.int2bytes(0x00))
        arrBytes.append(ByteUtils.int2bytes(0x00))
        arrBytes.append(ByteUtils.int2bytes(0x02))
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append( crcBytes[0] )
        arrBytes.append( crcBytes[1] )
        print( StrUtils.bytesToStr( arrBytes))
        return arrBytes

if __name__ == '__main__':
    sensor = SensorStrainDisplacement()
    sensor.readBusAddress()
