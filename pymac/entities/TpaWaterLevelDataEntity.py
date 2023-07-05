#coding=utf-8
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils

class TpaWaterLevelDataEntity:
    def __init__(self):
        #数据结构
        # 回应数据:    02   03      08      43 5F 28 F6     41 CD 80 00     5B 8D
        # 数据说明:本机地址 指令    数据长度    水位数据        温度       CRCL/CRCH
        self.addr = 0x00
        self.code = 0x03
        self.byteCnt = 0x08
        self.value = 0.0
        self.temperature = 0.0
        self.crc = 0x0000
    #
    #解析数据，数据类型包括频率和温度
    def parse(self,data):
        if( len(data)!=13):
            print("water level size is invalid")
            return 0
        
        self.addr=int(data[0])
        self.code=int(data[1])
        self.byteCnt= ByteUtils.int2byte( data[2])
        byteVal=bytearray()
        byteVal.append( data[3])
        byteVal.append( data[4])
        byteVal.append( data[5])
        byteVal.append( data[6])
        self.value = ByteUtils.bytes2Float( byteVal )
        byteVal=bytearray()
        byteVal.append( data[7])
        byteVal.append( data[8])
        byteVal.append( data[9])
        byteVal.append( data[10])
        self.temperature = ByteUtils.bytes2Float( byteVal )
        print("water level data : %.2f,%.2f" % (self.value,self.temperature))
        return self.value

if __name__ == '__main__':
    str = '020308435F28F641CD80005B8D'
    byteData = StrUtils.strToBytes( str )
    e = TpaWaterLevelDataEntity()
    e.parse(byteData)
    print(e)
