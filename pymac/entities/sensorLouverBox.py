#coding=utf-8
from utils.byteUtils import ByteUtils
from utils.crcUtils import CrcUtils
from utils.strUtils import StrUtils


class SensorLouverBox:
    def __init__(self):
        #百叶箱温湿度传感器
        self.sensorName="louver box"
        #总线地址，取值0-255
        self.addr="00"
        self.writeAddrCode="10"
        self.readAddrCode="20"
        self.readDataCode="03"
        self.dataStart="0000"
        self.dataCount="0002"
        

    def writeAddress(self,id):
        #0010AdressCRC （5 个字节） 返回： 0010CRC （4 个字节）
        arrBytes = []
        self.addr = id
        arrBytes.append(self.addr)
        arrBytes.append(self.writeAddrCode)
        bId = ByteUtils.int2byte(id)
        arrBytes.append(bId)
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append( crcBytes[0] )
        arrBytes.append( crcBytes[1] )
        print( StrUtils.bytesToStr( arrBytes))
        return arrBytes
        
    def readAddress(self):
        #0020CRC （4 个字节） 返回： 0020AdressCRC （5 个字节）
        arrBytes = []
        self.addr = 0x00
        arrBytes.append(self.addr)
        arrBytes.append(self.readAddrCode)
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append(crcBytes[0])
        arrBytes.append(crcBytes[1])
        print( StrUtils.bytesToStr( arrBytes))
        return arrBytes
        
    def readDisplacementData(self):
        #01 04 00 04 00 02 30 0A
        arrBytes = []
        self.addr = 0x01
        arrBytes.append(self.addr)
        arrBytes.append(self.readDataCode)
        arrBytes.append(0x00)
        arrBytes.append(0x04)
        arrBytes.append(0x00)
        arrBytes.append(0x02)
        crcBytes = CrcUtils.GenModbusCRC16( arrBytes )
        arrBytes.append( crcBytes[0] )
        arrBytes.append( crcBytes[1] )
        print( StrUtils.bytesToStr( arrBytes))
        return arrBytes


