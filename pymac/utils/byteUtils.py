# coding=utf-8
import copy
import struct


class ByteUtils:
    def __init__(self):
        print('ByteUtils init')

    @staticmethod
    def bytesToFloat(h1, h2, h3, h4):
        ba = bytearray()
        ba.append(h1)
        ba.append(h2)
        ba.append(h3)
        ba.append(h4)
        # network (= big-endian)
        val = struct.unpack("!f", ba)
        print(val)
        return struct.unpack("!f", ba)[0]

    @staticmethod
    def bytesToFloat2(arr_bytes):
        if len(arr_bytes) != 4:
            return None

        ba = bytearray()
        ba.append(arr_bytes[0])
        ba.append(arr_bytes[1])
        ba.append(arr_bytes[2])
        ba.append(arr_bytes[3])
        # network (= big-endian)
        val = struct.unpack("!f", ba)
        print(val)
        return struct.unpack("!f", ba)[0]

    @staticmethod
    def bytes2Float(arrByte):
        # network (= big-endian)
        val = struct.unpack("!f", arrByte)
        print(val)
        return struct.unpack("!f", arrByte)[0]

    @staticmethod
    def floatToBytes(f):
        bs = struct.pack("!f", f)
        # network (= big-endian)
        # return (bs[0],bs[1],bs[2],bs[3])
        return bs

    @staticmethod
    def int2byte(n):
        return str(n).encode()

    @staticmethod
    def short2bytes(n):
        b = n.to_bytes(length=2, byteorder='big', signed=False)
        return b

    @staticmethod
    def int2bytes3(n):
        n = 0x00FFFFFF & n
        b = n.to_bytes(length=3, byteorder='big', signed=False)
        return b

    @staticmethod
    def int2bytes2(n):
        n = 0xFFFF & n
        b = n.to_bytes(length=2, byteorder='big', signed=False)
        return b

    @staticmethod
    def int2bytes1(n):
        n = 0xFF & n
        b = n.to_bytes(length=1, byteorder='big', signed=False)
        return b

    @staticmethod
    def int2bytes(n):
        b = n.to_bytes(length=4, byteorder='big', signed=False)
        return b

    @staticmethod
    def bytes2int(b):
        n = int.from_bytes(b, byteorder='big', signed=False)
        return n

    @staticmethod
    def concatBytes(arr1, arr2):
        if type(arr1) == bytearray:
            for item in arr2:
                arr1.append(item)


    @staticmethod
    def ByteFillArray(arr_byte, pos_from, n_bytes, bytes_source):
        lst_item = list(arr_byte)
        pos_to = pos_from + n_bytes
        for i in range(pos_from, pos_to):
            if i < len(arr_byte) and (i - pos_from) < len(bytes_source):
                lst_item[i] = bytes_source[i - pos_from]
            else:
                break
        result = bytes(lst_item)
        return result

    @staticmethod
    def CopyByteArray(arr_item, byte_source, pos_from, n_read):
        n_return = 0
        pos_to = pos_from + n_read
        for i in range(pos_from, pos_to):
            if i - pos_from < len(arr_item) and i < len(byte_source):
                arr_item[i - pos_from] = byte_source[i]
                n_return += 1
            else:
                print("ERROR CopyByteArray")
        return n_return

    @staticmethod
    def CopyByteArray_0(byte_source, pos_from, n_read):
        n_return = 0
        pos_to = pos_from + n_read
        temp_item = []
        for i in range(pos_from, pos_to):
            if len(temp_item) > i:
                temp_item.append(byte_source[i])
                n_return += 1
        return bytes(temp_item)

    @staticmethod
    def BytesClone(byte_source):
        byte_target = []
        pos_to = len(byte_source)
        for i in range(0, pos_to):
            byte_target.append(byte_source[i])
        result = bytes(byte_target)
        return result

    @staticmethod
    def AppendBuffer(bytes_main, bytes_source):
        if len(bytes_source) <= 0:
            return bytes_main
        return bytes_main + bytes_source



    @staticmethod
    def revertArray(arr):
        if type(arr) == bytes:
            arr = list(arr)
        new_arr = []
        n_size = len(arr)
        for i in range(n_size):
            new_arr.append(arr[n_size - i - 1])
        return new_arr

    @staticmethod
    def revertBytes(arr):
        if type(arr) == bytes:
            arr = list(arr)
        new_arr = []
        n_size = len(arr)
        for i in range(n_size):
            new_arr.append(arr[n_size - i - 1])
        return bytes(new_arr)


if __name__ == '__main__':
    # 40DB5DA0
    val = bytes([0x40, 0xDB, 0x5D, 0xA0])
    print(ByteUtils.bytesToFloat2(val))

