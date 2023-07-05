# coding=utf-8
from protocol.frameFieldItem import FrameFieldItem
from utils.byteUtils import ByteUtils
from utils.crcUtils import CrcUtils





class FramePacket:
    def __init__(self):
        self.fldAddress = FrameFieldItem()
        self.fldActionCode = FrameFieldItem()
        self.fldContent = FrameFieldItem()
        self.fldCheckCode = FrameFieldItem()
        self.fldAddress.pos = 0
        self.fldAddress.byteCount = 1
        self.fldAddress.ResetBuf()

        self.fldActionCode.pos = 1
        self.fldActionCode.byteCount = 1
        self.fldActionCode.ResetBuf()

        self.fldContent.pos = self.fldActionCode.pos + self.fldActionCode.byteCount

        self.fldCheckCode.byteCount = 2
        self.fldCheckCode.ResetBuf()

    def ToByeArray(self,):
        nSize = self.fldAddress.byteCount + self.fldActionCode.byteCount + self.fldContent.byteCount + self.fldCheckCode.byteCount
        byteArr = bytes(nSize)
        item = self.fldAddress
        byteArr = ByteUtils.ByteFillArray(byteArr, item.pos, item.byteCount, item.buf)
        item = self.fldActionCode
        byteArr = ByteUtils.ByteFillArray(byteArr, item.pos, item.byteCount, item.buf)
        item = self.fldContent
        byteArr = ByteUtils.ByteFillArray(byteArr, item.pos, item.byteCount, item.buf)
        item = self.fldCheckCode
        byteArr = ByteUtils.ByteFillArray(byteArr, item.pos, item.byteCount, item.buf)
        return byteArr

    def GenCRC16(self,):
        bytesContent = self.fldAddress.buf
        bytesContent = ByteUtils.AppendBuffer(bytesContent, self.fldActionCode.buf)
        bytesContent = ByteUtils.AppendBuffer(bytesContent, self.fldContent.buf)

        bytesCrc = CrcUtils.GenModbusCRC16(bytesContent)
        self.fldCheckCode.pos = self.fldContent.pos + self.fldContent.byteCount
        self.fldCheckCode.byteCount = 2
        self.fldCheckCode.CloneBuffer(bytesCrc)

    def Parse(self, buf):
        size = len(buf)
        if size < 5:
            return 0
        self.fldAddress.CopyFromPos(buf)
        self.fldActionCode.CopyFromPos(buf)
        self.fldContent.pos = self.fldActionCode.pos + self.fldActionCode.byteCount
        self.fldContent.byteCount = size - self.fldAddress.byteCount - self.fldActionCode.byteCount - self.fldCheckCode.byteCount
        self.fldContent.CopyFromPos(buf)
        self.fldCheckCode.pos = size - 2
        self.fldCheckCode.byteCount = 2
        self.fldCheckCode.CopyFromPos(buf)
        return size

