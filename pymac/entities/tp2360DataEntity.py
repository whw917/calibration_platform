#coding=utf-8
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils

class Tp2360DataEntity:
    def __init__(self):
        #数据结构
        # 01 03 02 3B 61 6A 9C
        # 01 从机地址（从机ID） 字节1
        # 03 功能码字节2
        # 02 数据长度2 字节3、4
        # 3B 61 2 字节数据温度字节5、6
        # 6A 9C CRC 校验低位、高位字节7、8
        self.addr = 0x00
        self.code = 0x03
        self.byteCnt = 0x0002
        self.value = 0.0
        self.crc = 0x0000
    def parse(self,data):
        if( len(data)!=9):
            print("Tp2360DataEntity size is invalid")
            return 0
        
        self.addr=int(data[0])
        self.code=int(data[1])
        byteVal=[]
        byteVal.append( data[2])
        byteVal.append( data[3])
        self.byteCnt= ByteUtils.bytes2int( byteVal)
        byteVal=[]
        byteVal.append( data[4])
        byteVal.append( data[5])
        val = ByteUtils.bytes2int( byteVal)
        #数据解析运算：3B61=15201 15201*0.02-273.15=30.87℃
        self.value = val*0.02-273.15
        print("Tp2360DataEntity data : %d" % (self.value))
        return self.value

if __name__ == '__main__':
    str = '0103040F001900F2B7'
    byteData = StrUtils.strToBytes( str )
    e = Tp2360DataEntity()
    e.parse(byteData)
    print(e)
