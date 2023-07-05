# coding=utf-8
import threading
import time
import sys
import codecs
import io


class StrUtils:
    def __init__(self):
        print('StrUtils init')

    @staticmethod
    def strToBytes(str):
        # 整除符号：//
        wdLen = len(str) // 2
        i = 0
        byteArr = bytearray()
        while i < wdLen:
            wd = str[2 * i:2 * i + 2]
            try:
                nByte = int(wd, 16)
                byteArr.append(nByte)
            except Exception as e:
                print(e)
            i = i + 1
        return byteArr

    @staticmethod
    def bytesToStr(byteArr):
        strData = ""
        for b in byteArr:
            item = '{:02X}'.format(b)
            strData += item
        return strData

    @staticmethod
    def hexToStr(hexStr):
        strData = ""
        for b in hexStr:
            item = '{:02X}'.format(ord(b))
            strData += item
        return strData


    @staticmethod
    def byeHexToStr(hexStr):
        strData = ""
        for b in hexStr:
            strData += chr(b)
        return strData

    @staticmethod
    def byeToNumber(hexStr):
        strData = ""
        for b in hexStr:
            if chr(b) in "0123456789.+-":
                strData += chr(b)
        return strData

    @staticmethod
    def str(item):
        return '"' + item + '"'

    @staticmethod
    def parseFloat(str_value):
        str_value = str_value.replace(" ", "")
        str_value = str_value.replace("\r\n", "")
        f = float(str_value)
        # print("f = ", f)
        return f

    # @staticmethod
    # def strToBytes(str):
    #     # 整除符号：//
    #     wdLen = len(str) // 2
    #     i = 0
    #     byteArr = bytearray()
    #     while i < wdLen:
    #         wd = str[2 * i:2 * i + 2]
    #         try:
    #             nByte = int(wd, 16)
    #             char = char(nByte)
    #         except Exception as e:
    #             print(e)
    #         i = i + 1
    #     return byteArr


if __name__ == '__main__':
   str_value = "+  1.6995"
   print(StrUtils.parseFloat(str_value))

