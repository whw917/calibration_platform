from protocol.frameFieldItem import FrameFieldItem
from protocol.framePack import FramePacket
from utils.byteUtils import ByteUtils


class FrameReadRegister(FramePacket):
    # 读设备数据的地址
    READ_DATA_ADDR = 0X04

    def __init__(self, args=[]):
        super().__init__()
        if len(args) == 0:

            self.fldAddrStart = FrameFieldItem()
            self.fldRegisterCount = FrameFieldItem()
            self.fldAddrStart.byteCount = 2
            self.fldAddrStart.ResetBuf()
            self.fldRegisterCount.byteCount = 2
            self.fldRegisterCount.ResetBuf()
        elif len(args) == 4:
            actonCode = args[0]
            busAddress = args[1]
            regStart = args[2]
            regCount = args[3]

            # def __init__(self, actonCode, busAddress, regStart, regCount):
            #     super().__init__()
            self.fldAddress.CloneBuffer(ByteUtils.int2bytes1(busAddress))

            self.fldActionCode.CloneBuffer(ByteUtils.int2bytes1(actonCode))

            self.fldAddrStart = FrameFieldItem()
            self.fldAddrStart.pos = self.fldActionCode.pos + self.fldActionCode.byteCount
            self.fldAddrStart.byteCount = 2
            self.fldAddrStart.ResetBuf()
            self.fldAddrStart.CloneBuffer(ByteUtils.int2bytes2(regStart))

            self.fldRegisterCount = FrameFieldItem()
            self.fldRegisterCount.pos = self.fldAddrStart.pos + self.fldAddrStart.byteCount
            self.fldRegisterCount.byteCount = 2
            self.fldRegisterCount.ResetBuf()
            self.fldRegisterCount.CloneBuffer(ByteUtils.int2bytes2(regCount))

            self.fldContent.pos = self.fldActionCode.pos + self.fldActionCode.byteCount
            self.fldContent.byteCount = self.fldAddrStart.byteCount + self.fldRegisterCount.byteCount
            self.fldContent.ResetBuf()
            self.fldContent.CloneBuffer(self.fldAddrStart.buf)
            end = self.fldAddrStart.byteCount
            self.fldContent.AppendBuffer(end, self.fldRegisterCount.buf)

            self.fldCheckCode.pos = self.fldContent.pos + self.fldContent.byteCount
            self.fldCheckCode.byteCount = 2
            self.fldCheckCode.ResetBuf()
            #
            # 需要计算校验码
            self.GenCRC16()

    def ParseContent(self, ):
        bufContent = self.fldContent.buf
        arr_item = bytearray(self.fldAddrStart.buf)
        ByteUtils.CopyByteArray(arr_item, bufContent, 0, 2)
        self.fldAddrStart.buf = bytes(arr_item)
        arr_item = bytearray(self.fldRegisterCount.buf)
        ByteUtils.CopyByteArray(arr_item, bufContent, 2, 2)
        self.fldRegisterCount.buf = bytes(arr_item)
        return 0
