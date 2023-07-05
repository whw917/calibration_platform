# coding=utf-8

from utils.strUtils import StrUtils


class CrcUtils:
    def __init__(self):
        print('CrcUtils init')

    @staticmethod
    def GenByeCRCModBus(cDataIn, wCRCIn):
        wCheck = 0
        lnByte = cDataIn & 0xFF
        wCRCIn = wCRCIn ^ lnByte

        for i in range(8):
            wCheck = wCRCIn & 1
            wCRCIn = wCRCIn >> 1
            wCRCIn = wCRCIn & 0x7fff

            if wCheck == 1 :
                wCRCIn = wCRCIn ^ 0xa001
            
            wCRCIn = wCRCIn & 0xffff

        return wCRCIn

    @staticmethod
    def GenByteArrCRC(i_len_in, byte_arr):
        wHi = 0
        wLo = 0
        wCRC = 0
        wCRC = 0xFFFF

        for i in range(i_len_in):
            wCRC = CrcUtils.GenByeCRCModBus(byte_arr[i], wCRC)

        wHi = wCRC // 256
        wLo = wCRC % 256
        wCRC = (wHi << 8) | wLo

        return wCRC
  
    @staticmethod
    def GenModbusCRC16( bytesSource):
        nCrc = CrcUtils.GenByteArrCRC(len(bytesSource), bytesSource)
        byteCRC = [int(0xFF), int(0xFF)]
        byteCRC[0] = int((nCrc >> 8) & 0xFF)
        byteCRC[1] = int(nCrc & 0xFF)

        # swap the two bytes
        tmpByte = byteCRC[0]
        byteCRC[0] = byteCRC[1]
        byteCRC[1] = tmpByte
        return byteCRC

    @staticmethod
    def GenModbusCRC8(arr_bytes):
        crc_byte = arr_bytes[0]
        for i in range(len(arr_bytes)):
            if i != 0:
                crc_byte = crc_byte ^ arr_bytes[i]
                crc_byte = crc_byte & 0x00FF

        return crc_byte

    @staticmethod
    def CheckPacket(arr_bytes):
        sz = len(arr_bytes)
        arr = bytearray()
        for i in range(len(arr_bytes)-2):
            arr.append(arr_bytes[i])
        crc_codes = CrcUtils.GenModbusCRC16(arr)
        if crc_codes[0] == arr_bytes[sz-2] and crc_codes[1] == arr_bytes[sz-1]:
            return True
        else:
            print("INVALID CRC")
            return False


if __name__ == '__main__':
    #001001BDC0
    #010400040002300A
    byteArr = StrUtils.strToBytes("BA03ED800203032000639C00C800C8")
    crc = CrcUtils.GenModbusCRC8( byteArr )
    strCrc = StrUtils.bytesToStr( crc )
    print( strCrc )
