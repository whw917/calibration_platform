# coding=utf-8
from utils import crcUtils
from utils.crcUtils import CrcUtils
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils


class RealInstruction:
    # 模式选项
    MODE_CLICK = 0x00  # 点动模式
    MODE_STEP = 0x01  # 单步模式
    MODE_AUTO = 0x02  # 自动模式
    MODE_RETURN = 0x03  # 单次往返
    MODE_RETURN_TIME = 0x04  # 按次往返
    MODE_CLICK_ZERO = 0x05  # 按键回零单方向
    MODE_FORWARD_ZERO = 0x06  # 前进回零往返模式
    MODE_DIRECTORY_ZERO = 0x07  # 单方向运行模式
    # 运动方向
    MOVE_PLUS = 0x01
    MOVE_MINUS = 0x02
    MOVE_STOP = 0x003
    # 标志位
    FLAG_LAUNCH = 0
    FLAG_ENABLE = 0
    FLAG_ZERO = 1
    FLAG_URGENT_STOP = 2
    FLAG_LIMIT_POSITION = 3
    FLAG_02_OUT = 4
    FLAG_SINGLE_SWITCH_TRIGGER = 5
    FLAG_INPUT_SWITCH_TRIGGER_DISABLED = 6
    FLAG_POSITION_CONTROL = 7

    def __init__(self):
        self.header = 0xBA  # 包头
        self.mode = 0x00  # 运动模式

        self.frequencyDivision = 0x0000  # 分频基数，字节顺序：高位低位
        self.controllerCode = 0x00  # 控制器编号
        self.moveTime = 0x00  # 执行次数，（提示：只在04:按次往返模式时有效）
        self.moveDirectory = 0x01  # 01 :正运行02 :负运行03 :停止

        # 数据标志位
        self.moveFlag = 0x00  # 本字节拆分数据位8位11111111 （1：代表常开、使能启动 0：代表常闭、不启动）
        # 如例：11111111 (例中全部有效位) 代表：依次排序从左至右位，启动上电运行使能、启动上电回零使能、急停常开、限位常开、启动0.2 倍频率输出、启动单开关触发、启动输入开关失效、启动位置控制使能、
        # 例中串口应发数据：FF

        self.movePulse = 0x000000  # 行进脉冲总数高位、中位、低位
        self.acceleratePulse = 0x00  # 加速脉冲数高位、低
        self.deceleratePulse = 0x00  # 降速脉冲数高位、低
        self.crc = 0x00
        self.tail = 0xFE

    def package(self):
        byte_codes = bytearray()
        byte_codes.append(self.header)
        byte_codes.append(self.mode)
        ByteUtils.concatBytes(byte_codes, ByteUtils.int2bytes2(self.frequencyDivision))
        byte_codes.append(self.controllerCode)
        byte_codes.append(self.moveTime)
        byte_codes.append(self.moveDirectory)
        byte_codes.append(self.moveFlag)
        str_val = StrUtils.bytesToStr(byte_codes)
        print(str_val)
        ByteUtils.concatBytes(byte_codes, ByteUtils.int2bytes3(self.movePulse))
        ByteUtils.concatBytes(byte_codes, ByteUtils.int2bytes2(self.acceleratePulse))
        ByteUtils.concatBytes(byte_codes, ByteUtils.int2bytes2(self.deceleratePulse))
        crc = CrcUtils.GenModbusCRC8(byte_codes)
        byte_codes.append(crc)
        byte_codes.append(self.tail)
        return byte_codes


if __name__ == '__main__':
    ins = RealInstruction()
    ins.package()
