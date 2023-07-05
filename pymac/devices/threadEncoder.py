import logging
import threading
import time
from base.serialDevice import SerialDevice
from devices.AppResource import AppResource
from utils.sysConfig import SysConfig
logger = logging.getLogger('service.log')


class ThreadEncoder(threading.Thread):
    def __init__(self, window):
        self.bool_exit = False
        self.bool_pause = False
        self.serialDevice = None
        self.window = window
        threading.Thread.__init__(self)

    def run(self):
        bExit = False
        self.openSerial()

        while not bExit:
            if AppResource.ins().bool_exit:
                print("Encoder thread exited")
                logger.info("Encoder thread exited")
                break
            time.sleep(0.5)
            if not self.serialDevice.isOpen():
                if not self.openSerial():
                    print("ENCODER DEVICE IS NOT READY")
                    logger.info("ENCODER DEVICE IS NOT READY")
                    time.sleep(5)

            self.serialDevice .writeHex("02")
            data = self.serialDevice .readFromHeidenhain()
            if data['code'] > 0:
                AppResource.ins().getApi().stepmotor.setCurrentAngular(data['value'])
                value_to_send = str(round(data['value'], 5))
                AppResource.ins().sendLiveData(self.window, "currentAngularValue", value_to_send)
            else:
                time.sleep(0.1)
            # end else
        # end else
        logger.info("THREAD ENCODER EXITED")

    def openSerial(self):
        if self.serialDevice is not None:
            self.serialDevice.closeSerial()
        else:
            self.serialDevice = SerialDevice()

        config = SysConfig()
        config.load()
        comName = config.getOption("ANGULAR_ENCODER", "port")
        baudrate = config.getIntOption("ANGULAR_ENCODER", "baudrate")
        return self.serialDevice.openSerial(comName, baudrate)


    def pause(self):
        self.bool_pause = True

    def resume(self):
        self.bool_pause = False

    def stop(self):
        self.bool_exit = False
