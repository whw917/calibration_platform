from utils.byteUtils import ByteUtils


class FrameFieldItem:
    def __init__(self, args=[]):
        if len(args) == 0:
            self.buf = []
            self.pos = 0
            self.byteCount = 1
        elif args == 3:
            pos = args[0]
            byte_count = args[1]
            arr_byte = args[2]
            # def __init__(self, pos, byte_count, arr_byte):
            self.pos = pos
            self.byteCount = byte_count
            if byte_count == 0:
                byte_count = 1
            lst_buf = [byte_count]  # byte[byteCount];
            for i in range(0, byte_count):
                if i < len(arr_byte):
                    lst_buf[i] = arr_byte[i]
                else:
                    break
            self.buf = bytes(lst_buf)

    def CopyFromPos(self, data):
        self.buf = bytes(self.byteCount)
        end = self.pos + self.byteCount
        if end > len(data):
            return 0
        lst_buf = list(self.buf)
        for i in range(self.pos, end):
            lst_buf[i-self.pos] = data[i]
        self.buf = bytes(lst_buf)
        return self.byteCount

    def ResetBuf(self):
        if self.byteCount == 0:
            self.byteCount = 1
            self.buf = bytes(1)
        else:
            self.buf = bytes(self.byteCount)

    def AppendBuffer(self, from_pos, bytes_content):
        if bytes_content is None or len(bytes_content) <= 0:
            return self.byteCount;

        if self.byteCount <= 0:
            return 0

        if self.buf is None:
            self.buf = bytes(self.byteCount)

        self.buf = ByteUtils.ByteFillArray(self.buf, from_pos, len(bytes_content), bytes_content)
        return self.byteCount

    def CloneBuffer(self, data):
        if self.byteCount == 0:
            self.buf = ByteUtils.BytesClone(data)
            self.byteCount = len(data)
        else:
            if self.buf is None:
                self.buf = bytes(self.byteCount)
            # ByteUtils.ResetBuffer(self.buf);
            lst_buf = list(self.buf)
            for i in range(self.byteCount):
                if i < len(data):
                    lst_buf[i] = data[i];
                else:
                    break
            self.buf = bytes(lst_buf)


