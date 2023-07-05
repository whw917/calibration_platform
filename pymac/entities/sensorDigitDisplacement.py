# coding=utf-8
from utils.strUtils import StrUtils
from utils.crcUtils import CrcUtils


class SensorDigitDisplacement:
    def __init__(self):
        #百叶箱温湿度传感器
        self.sensorName="digit displacement"
        #总线地址，取值0-255
        self.addr=0x00
        self.readAddrCode=0x03
        self.readDataCode=0x04
        self.dataStart=0x00
        self.dataCount=0x00
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

    def readDisplacementData(self):
        #01 04 00 04 00 02 30 0A
        arrBytes = bytearray()
        arrBytes.append(self.addr)
        arrBytes.append(self.readDataCode)
        arrBytes.append(0x00)
        arrBytes.append(0x04)
        arrBytes.append(0x00)
        arrBytes.append(0x02)
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append( crcBytes[0] )
        arrBytes.append( crcBytes[1] )
        # print( StrUtils.bytesToStr( arrBytes))
        return arrBytes

if __name__ == '__main__':
    sensor = SensorDigitDisplacement()
    sensor.readBusAddress()
