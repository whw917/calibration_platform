import time

import logging
from concurrent.futures import thread

from base.serialDevice import SerialDevice
from devices.threadStepmotor import ThreadStepmotor
from entities.realInstruction import RealInstruction
from utils.crcUtils import CrcUtils
from utils.strUtils import StrUtils
from utils.sysConfig import SysConfig

logger = logging.getLogger('service.log')


class Stepmotor:
    MOVE_DIRECTORY_PLUS = 0x01
    MOVE_DIRECTORY_MINUS = 0x02
    MOVE_DIRECTORY_STOP = 0x03

    STEP_SIZE_1 = 1
    STEP_SIZE_01 = 2
    STEP_SIZE_001 = 3
    STEP_SIZE_0001 = 4

    MOVE_MODE_1 = 1
    MOVE_MODE_01 = 2
    MOVE_MODE_001 = 3
    MOVE_MODE_0001 = 4
    MOVE_MODE_00001 = 5

    def __init__(self):
        self.config = SysConfig()
        self.config.load()
        self.port = self.config.getOption("STEP_MOTOR", "port")
        self.baudrate = self.config.getOption("STEP_MOTOR", "baudrate")
        self.serial = SerialDevice()

        self.moveMode = Stepmotor.MOVE_MODE_1  # 运行模式: 移动 1.0 整数售， 移动 0.1  整数售，移动 0.01  整数售，移动 0.001  整数售， 移动 0.0001  整数售，

        # 当前位置
        self.currentAngular = 0.0
        self.targetAngular = 0.0
        self.nTryChangeMoveMode = 0

        self.realInstruction = RealInstruction()
        # 初始化指令
        self.realInstruction.mode = RealInstruction.MODE_CLICK
        #  1  2  3  4 5  5  7  8  9  10 11 12 13 14 15 16 17
        # BA 02 F8 0C 00 03 01 30 00 63 9C 00 C8 00 C8 81 FE
        # BA 02 F8 0C 00 03 03 30 00 63 9C 00 C8 00 C8 83 FE
        # BA 02 F8 0C 02 03 01 30 00 63 9C 00 C8 00 C8 83 FE
        # BA 02 F8 0C 00 03 01 30 00 63 9C 00 C8 00 C8 81 FE
        '''
        加速脉冲数：10，减速脉冲数：10,距离50000,速度基数60000
            00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16
            BA 00 EA 60 00 03 02 31 00 C3 50 00 0A 00 0A 93 FE
        '''

        self.realInstruction.frequencyDivision = 0xEA60  # 60000
        self.realInstruction.controllerCode = 0x00  # 控制器编号
        self.realInstruction.moveTime = 0x03  # 移动次数，不用
        self.realInstruction.moveDirectory = 0x02  # 正运行
        self.realInstruction.moveFlag = 0x31
        self.realInstruction.movePulse = 0x00C350  # 移动的脉冲数 50000
        self.realInstruction.acceleratePulse = 0x000A  # 加速脉冲 10
        self.realInstruction.deceleratePulse = 0x000A  # 减速脉冲 10

        self.threadMoving = ThreadStepmotor(self)

    def isOpen(self):
        return self.serial.isOpen()

    def close(self):
        self.serial.close()

    def openSerial(self):
        return self.serial.openSerial(self.port, self.baudrate)

    def computePulseWithAngular(self, angular):
        return angular * 1000

    def moveStepAngular0(self, step_angular):
        # pulse_count = self.computePulseWithAngular(step_angular)
        # self.realInstruction.movePulse = pulse_count
        self.realInstruction.moveDirectory = Stepmotor.MOVE_DIRECTORY_PLUS
        arr_content = self.realInstruction.package()
        self.serial.writeBytes(arr_content)
        # 等待回应
        res_str = "timeout"
        res = bytearray()
        for i in range(10):
            time.sleep(0.5)
            if 0 < self.serial.readBytes(res):
                print(StrUtils.bytesToStr(res))
                res_str = StrUtils.bytesToStr(res)
                break
        return res_str

    def setCurrentAngular(self, current):
        self.currentAngular = current
        self.threadMoving.currentAngular = current

    def moveStepAngular(self, step_angular):
        if not self.isOpen():
            if not self.openSerial():
                return "FAILED TO OPEN"

        self.nTryChangeMoveMode = 0
        self.threadMoving.reset()
        self.targetAngular = step_angular
        # 等待回应
        res_str = self.checkMoveState()
        if res_str == "FAILED TO OPEN":
            return "FAILED TO OPEN"

        if res_str != 'END':
            if not self.threadMoving.started:
                self.threadMoving.start()
                # self.threadMoving.join()

        return res_str

    def writeInstruction(self):
        if not self.serial.isOpen():
            # 发出错误信息
            return "FAILED TO OPEN"

        arr_content = self.realInstruction.package()
        self.serial.writeBytes(arr_content)
        # 等待回应
        res_str = "timeout"
        res = bytearray()
        for i in range(10):
            time.sleep(0.5)
            if 0 < self.serial.readBytes(res):
                print(StrUtils.bytesToStr(res))
                res_str = StrUtils.bytesToStr(res)
                break
        if res == "timeout":
            logger.info("timeout when serial.readBytes()")
        return res_str

    def readFromMotor(self):
        # 等待回应
        res_str = "timeout"
        res = bytearray()
        if 2 < self.serial.readBytes(res):
            res_str = StrUtils.bytesToStr(res)
            logger.info("MOTOR SERIAL DATA " + res_str)
        return res_str

    def stopMoving(self):
        self.threadMoving.pause()
        self.realInstruction.moveDirectory = Stepmotor.MOVE_DIRECTORY_STOP
        arr_content = self.realInstruction.package()
        self.serial.writeBytes(arr_content)
        # 等待回应
        res_str = "timeout"
        res = bytearray()
        for i in range(10):
            time.sleep(0.5)
            if 0 < self.serial.readBytes(res):
                print(StrUtils.bytesToStr(res))
                res_str = StrUtils.bytesToStr(res)
                break
        return res_str

    def clearSerial(self):
        self.serial.readSerial()

    def close(self):
        self.serial.closeSerial()

    def setParams(self, run_mode):
        '''
        加速脉冲数：10，减速脉冲数：10,距离50000,速度基数60000
            00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16
            BA 00 EA 60 00 03 02 31 00 C3 50 00 0A 00 0A 93 FE
        '''
        if run_mode == Stepmotor.MOVE_MODE_1:
            self.realInstruction.deceleratePulse = 0x0001
            self.realInstruction.acceleratePulse = 0x0001
            self.realInstruction.frequencyDivision = 60000  # 60000

        elif run_mode == Stepmotor.MOVE_MODE_01:
            self.realInstruction.deceleratePulse = 0x0005
            self.realInstruction.acceleratePulse = 0x0005
            # self.realInstruction.frequencyDivision = 0x4E20  # 20000
            self.realInstruction.frequencyDivision = 30000  # 20000

        elif run_mode == Stepmotor.MOVE_MODE_001:
            self.realInstruction.deceleratePulse = 0x000A  # 50
            self.realInstruction.acceleratePulse = 0x000A  # 50
            # self.realInstruction.frequencyDivision = 0x2710  # 5000
            self.realInstruction.frequencyDivision = 20000  # 20000
        elif run_mode == Stepmotor.MOVE_MODE_0001:
            self.realInstruction.deceleratePulse = 0x32  # 100
            self.realInstruction.acceleratePulse = 0x32  # 100
            # self.realInstruction.frequencyDivision = 0x07D0  # 2000
            self.realInstruction.frequencyDivision = 10000  # 20000

        elif run_mode == Stepmotor.MOVE_MODE_00001:
            self.realInstruction.deceleratePulse = 200  # 100
            self.realInstruction.acceleratePulse = 200  # 100
            # self.realInstruction.frequencyDivision = 0x07D0  # 2000
            self.realInstruction.frequencyDivision = 5000  # 20000

    def setMoveDirectory(self, target_angular):
        if target_angular > self.currentAngular:
            self.realInstruction.moveDirectory = Stepmotor.MOVE_DIRECTORY_PLUS
        else:
            self.realInstruction.moveDirectory = Stepmotor.MOVE_DIRECTORY_MINUS

    def setMoveMode(self, target_angular):
        mode = self.getMoveMode(target_angular)
        self.moveMode = mode

    def setMovePulse(self, target_angular):
        diff = round(abs(target_angular - self.currentAngular), 5)
        if diff >= 2.0:
            self.realInstruction.movePulse = int(5000 * (int(diff)-0.5))
        elif diff >= 0.2:
            self.realInstruction.movePulse = int(500 * (int(diff*10)-0.5))
        elif diff >= 0.02:
            self.realInstruction.movePulse = int(50 * (int(diff*100)-0.5))
        elif diff >= 0.002:
            self.realInstruction.movePulse = int(5 * (int(diff*1000)-1))
        elif diff >= 0.0005:
            # 0.0005
            self.realInstruction.movePulse = 3
        else:
            # 0.0005
            self.realInstruction.movePulse = 1

    def getStepSize(self, target_angular):
        diff = round(abs(target_angular - self.currentAngular), 5)
        if diff >= 1.0:
            return Stepmotor.STEP_SIZE_1

        elif diff >= 0.1:
            return Stepmotor.STEP_SIZE_01
        elif diff >= 0.01:
            return Stepmotor.STEP_SIZE_01
        elif diff >= 0.001:
            return Stepmotor.STEP_SIZE_001
        else:
            return Stepmotor.STEP_SIZE_001

    def getMoveMode(self, target_angular):
        diff = round(abs(target_angular - self.currentAngular), 5)
        if diff >= 1.0:
            return Stepmotor.MOVE_MODE_1
        elif diff >= 0.1:
            return Stepmotor.MOVE_MODE_01
        elif diff >= 0.01:
            return Stepmotor.MOVE_MODE_001
        elif diff >= 0.001:
            return Stepmotor.MOVE_MODE_0001
        elif diff >= 0.0001:
            return Stepmotor.MOVE_MODE_00001
        else:
            return Stepmotor.MOVE_MODE_1

    def checkSameAngular(self, a, b):
        return int(a*1000) == int(b*1000) and abs(a - b) < 0.0005

    def checkMoveState(self):
        if self.checkSameAngular(self.currentAngular, self.targetAngular):
            print("ARRIVED AT THE TARGET CURRENT " + str(self.currentAngular) + ", TARGET " + str(self.targetAngular))
            return 'END'
        if self.nTryChangeMoveMode >= 100:
            print("CHANGED MOVE 100 TIMES")
            return 'END'
        time.sleep(0.5)
        diff = round(abs(self.currentAngular - self.targetAngular), 5)

        self.setMoveDirectory(self.targetAngular)
        self.setMoveMode(self.targetAngular)
        self.setParams(self.getMoveMode(self.targetAngular))
        self.setMovePulse(self.targetAngular)

        print("N " + str(self.nTryChangeMoveMode) + ",差异 " + str(diff) + ",加速 " + str(self.realInstruction.acceleratePulse) + ",距离 " + str(self.realInstruction.movePulse) + ",频率 " + str(self.realInstruction.frequencyDivision))

        # resume moving
        res = self.writeInstruction()
        if res == "FAILED TO OPEN":
            return "FAILED TO OPEN"
        self.nTryChangeMoveMode = self.nTryChangeMoveMode + 1
        return res

    def launchMoving(self):
        try:
            self.threadMoving.run()
        except Exception as ex:
            logger.error(ex.args[0])
        finally:
            logger.info("MOVING END")


if __name__ == "__main__":
    a = 0.1112
    b = 0.1110
    print( int(a*1000) == int(b*1000) and abs(a - b) < 0.0005)