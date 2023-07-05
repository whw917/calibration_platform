#coding=utf-8
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils

class VibrationDataEntity:
    def __init__(self):
        #数据结构
        # XX 		03 		04 		44 7A 00 00	XXXX
        # 地址	功能码	数据长度	4 字节浮点 	CRC 校验
        # 0X44 7A 00 00，实际频率值为1000Hz。
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
    str = '01030441A000000101'
    byteData = StrUtils.strToBytes( str )
    e = VibrationDataEntity()
    e.parse(byteData)
    print(e)
