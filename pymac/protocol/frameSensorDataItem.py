import logging

from utils.byteUtils import ByteUtils
from utils.strUtils import StrUtils

logger = logging.getLogger('service.log')


class FrameSensorDataItem:
    SENSOR_DATA_SIZE = 4

    def __init__(self, buf, dt):
        self.data = []
        nSize = len(buf)
        if nSize == FrameSensorDataItem.SENSOR_DATA_SIZE:
            arr_item = bytearray(FrameSensorDataItem.SENSOR_DATA_SIZE)
            ByteUtils.CopyByteArray(arr_item, buf, 0, FrameSensorDataItem.SENSOR_DATA_SIZE)
            self.data = bytes(arr_item)

        self.senValue = 0.0
        self.dt = dt

    def Parse(self, ):
        if len(self.data) < FrameSensorDataItem.SENSOR_DATA_SIZE:
            return False

        # /**
        #  读取数据回应	XX	 03     04	        XX	XX	XX	XX
        #  说明	        地址 功能码	数据长度	4个字节数据	    CRC校验
        #  本次改动，将通道号及传感器类型去掉了
        #  */
        # // channel = ByteUtil.SingleByte2Int(new byte[] { data[0] });
        # // senType = ByteUtil.SingleByte2Int(new byte[] { data[1] });
        # //
        # //4个字节的float
        # Array.Reverse( data );
        # new_data = ByteUtils.revertArray(self.data)
        logger.info("bytes= " + StrUtils.bytesToStr(self.data))
        self.senValue = ByteUtils.bytesToFloat2(self.data)

        logger.info("bytes= " + StrUtils.bytesToStr(self.data) + ",value= " + str(self.senValue))
        return True
