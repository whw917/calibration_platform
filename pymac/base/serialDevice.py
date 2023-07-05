# coding=utf-8
import logging
import threading
import time
import serial
import serial.tools.list_ports
from utils.strUtils import StrUtils
from utils.byteUtils import ByteUtils

logger = logging.getLogger('service.log')

class SerialDevice:
    def __init__(self):
        print('SerialDevice init')
        self.port = ""
        self.baudrate = 0
        self.serial = serial.Serial()
        self.lock = threading.Lock()

    def Serial(self):
        return self.serial

    def isOpen(self):
        return self.serial.isOpen()

    def close(self):
        self.serial.close()

    # 打开串口
    def openSerial(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.lock.acquire()
        ret = False
        if self.serial.isOpen():
            self.serial.close()
            time.sleep(0.1)
        else:
            try:
                self.serial.port = port
                self.serial.baudrate = baudrate
                self.serial.open()
                ret = self.serial.isOpen()
                print("serial opened successfully")
                logger.info("serial opened successfully: comport=" + self.serial.port + ",baudrate=" + str(baudrate) )
            except serial.SerialException as e:
                print(e)
                logger.error("SerialException")
                logger.error(e)
                ret = False
            except Exception as e:
                logger.error("SerialException")
                print(e)
                logger.error(e)
                ret = False
            finally:
                print('openSerial end')
                logger.info("openSerial end")
        self.lock.release()
        return ret

    # 写入
    def writeSerial(self, data):
        print("write port")
        self.lock.acquire()
        ret = {
            'code': -1,
            'msg': "serial is closed"
        }
        if not self.serial.isOpen():
            ret = {
                'code': -1,
                'msg': "serial is closed"
            }
        else:
            try:
                bytesStr = StrUtils.strToBytes(data)
                logger.info("WRITE BYTES:" + bytesStr)
                n = self.serial.write(bytesStr)
                print("write data lenght = ", n)
                ret = {
                    'code': n,
                    'msg': "OK"
                }
            except serial.SerialException as e:
                logger.error("WRITE ERROR")
                logger.error(e)
                print(e)
                ret = {
                    'code': -1,
                    'msg': e
                }
            except Exception as e:
                logger.error("WRITE ERROR")
                logger.error(e)
                print(e)
                ret = {
                    'code': -1,
                    'msg': e
                }
                return ret
            finally:
                pass
                # print("writeSerial completed")
        self.lock.release()

    # 写入
    def writeHex(self, data):
        try:
            bytesStr = StrUtils.strToBytes(data)
            n = self.serial.write(bytesStr)
            # print("write data length = ", n)
            ret = {
                'code': n,
                'msg': "OK"
            }
            return ret
        except serial.SerialException as e:
            print(e)
            ret = {
                'code': -1,
                'msg': e
            }
            return ret
        except Exception as e:
            print(e)
            ret = {
                'code': -1,
                'msg': e
            }
            return ret
        # finally:
        #     print("writeSerial completed")

    # 关闭串口
    def closeSerial(self):
        print("close serial")
        if not self.serial.isOpen():
            return True

        self.lock.acquire()
        ret = False
        try:
            self.serial.close()
            ret = True
        except serial.SerialException as e:
            print(e)
            ret = False
        except Exception as e:
            print(e)
            ret = False
        finally:
            print('closeseSerial end')
        self.lock.release()
        return ret

    # 读数据
    def readBytes(self, buffer):
        if buffer is None:
            return -1
        if not self.serial.isOpen():
            return 0

        result = -1
        self.lock.acquire()
        try:
            if self.serial.readable:
                # print("data is readable")
                bytesData = self.serial.read_all()
                if len(bytesData) > 0:
                    ByteUtils.concatBytes(buffer, bytesData)
                    result = len(bytesData)
                    logger.info("READ BYTES: " + StrUtils.bytesToStr(bytesData))
        except serial.SerialException as e:
            logger.error("SerialException")
            logger.error(e)
            print(e)
        except Exception as e:
            logger.error("SerialException")
            logger.error(e)
            print(e)
        finally:
            # print('readSerial end')
            self.lock.release()
        return result


    # 写入
    def writeBytes(self, arr_byte):
        result = 0
        print(StrUtils.bytesToStr(arr_byte))
        logger.info("WRITE BYTES: " + StrUtils.bytesToStr(arr_byte))
        try:
            self.lock.acquire()
            n = self.serial.write(arr_byte)
            result = n
        except serial.SerialException as e:
            logger.error("SerialException")
            logger.error(e)
            print(e)
        except Exception as e:
            logger.error("SerialException")
            logger.error(e)
            print(e)
        finally:
            logger.info("writeSerial completed")
            self.lock.release()
        # try-end
        return result

    # 读数据
    def readSerial(self):
        # print("read port")
        if not self.serial.isOpen():
            ret = {
                'code': -1,
                'data': "serial is closed"
            }
            return ret

        self.lock.acquire()
        ret = {
            'code': 0,
            'data': ""
        }
        try:
            if self.serial.readable:
                print("data is readable")
                bytesData = self.serial.read_all()
                if bytesData != b'':
                    ''' 地址	命令	    数据
                        03	    04	    00	00	03	02
                        0	    1	    2	3	4	5
                    '''
                    if (len(bytesData) >= 6):
                        val = ByteUtils.bytesToFloat(bytesData[2], bytesData[3], bytesData[4], bytesData[5])
                        ret = {
                            'code': len(bytesData),
                            'data': StrUtils.bytesToStr(bytesData),
                            'value': val
                        }
                    else:
                        print("Length is less then 6 :" + StrUtils.bytesToStr(bytesData))
                else:
                    print("Empty data")

        except serial.SerialException as e:
            print(e)
            ret = {
                'code': -1,
                'data': e
            }
        except Exception as e:
            print(e)
            ret = {
                'code': -1,
                'data': e.args
            }
        # finally:
        #     print('readSerial end')

        self.lock.release()
        return ret

    # 读数据
    def readFromHeidenhain(self):
        # print("read port")
        if not self.serial.isOpen():
            ret = {
                'code': -1,
                'data': "serial is closed"
            }
            return ret

        self.lock.acquire()
        ret = {
            'code': 0,
            'data': ""
        }
        try:
            if self.serial.readable:
                # print("data is readable")
                bytesData = self.serial.read_all()
                if bytesData != b'':
                    if (len(bytesData) >= 6):
                        ret = {
                            'code': len(bytesData),
                            'data': StrUtils.byeHexToStr(bytesData),
                            'value': StrUtils.parseFloat(StrUtils.byeToNumber(bytesData))
                        }
                    # else:
                        # print("Length is less then 6 :" + StrUtils.bytesToStr(bytesData))
                # else:
                    # print("Empty data")

        except serial.SerialException as e:
            print(e)
            ret = {
                'code': -1,
                'data': e
            }
        except Exception as e:
            print(e)
            ret = {
                'code': -1,
                'data': e.args
            }
        # finally:
        #     print('readSerial end')

        self.lock.release()
        return ret