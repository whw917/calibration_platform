#coding=utf-8
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils

class StrainDisplacementDataEntity:
    def __init__(self):
        #数据结构
        # 回应数据:     01 03       04      00 80 A9 3C     85 9A
        # 数据说明:本机地址 指令    数据长度    数据        CRCL/CRCH
        self.addr = 0x00
        self.code = 0x03
        self.byteCnt = 0x04
        self.value = 0.0
        self.crc = 0x0000
    #
    #解析数据，数据类型包括频率和温度
    def parse(self,data):
        if( len(data)!=9):
            print("VibrationDataEntity size is invalid")
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
        print("VibrationDataEntity data : %f" % (self.value))
        return self.value

if __name__ == '__main__':
    str = '0103040080A93C859A'
    byteData = StrUtils.strToBytes( str )
    e = StrainDisplacementDataEntity()
    e.parse(byteData)
    print(e)
