import logging
import threading
import time

from devices.AppResource import AppResource

logger = logging.getLogger('service.log')


class ThreadStepmotor(threading.Thread):

    def __init__(self, stepmotor):
        self.bool_pause = False
        self.stepmotor = stepmotor

        # 当前位置
        self.currentAngular = 0.0
        self.targetAngular = 0.0
        self.lastPositionAngular = 0.0
        self.bool_exit = False
        self.nSameAngular = 0
        self.started = False
        self.nArrived = 0

        threading.Thread.__init__(self)

    def reset(self):
        self.lastPositionAngular = 0.0
        self.bool_pause = False
        self.bool_exit = False
        self.nSameAngular = 0
        self.nArrived = 0

    def pause(self):
        self.bool_pause = True

    def resume(self):
        self.bool_pause = False

    def stop(self):
        self.bool_exit = False

    def run(self):
        self.started = True
        check_result = ""
        while not self.bool_exit:
            if AppResource.ins().bool_exit:
                print("Stepmotor thread exited")
                logger.info("Stepmotor thread exited")
                break
            if self.bool_pause:
                if self.stepmotor.isOpen():
                    self.stepmotor.close()
                # end if
                time.sleep(1)
                continue
            time.sleep(0.5)
            if self.lastPositionAngular == self.currentAngular:
                self.nSameAngular = self.nSameAngular + 1
                print("ANGULAR " + str(self.currentAngular))
                logger.info("ANGULAR " + str(self.currentAngular))
            else:
                print("MOVE " + str(abs(self.lastPositionAngular - self.currentAngular)))
                logger.info("MOVE " + str(abs(self.lastPositionAngular - self.currentAngular)))
                self.lastPositionAngular = self.currentAngular

            if check_result == "END" or (check_result != "" and check_result.find("B0") >= 0):
                check_result = ""
                check_result = self.checkMovingStatus(check_result)
            elif check_result == "ARRIVED":
                check_result = self.checkMovingStatus(check_result)
                continue
            else:
                res = "timeout"
                res = self.stepmotor.readFromMotor()
                if (res != "" and res.find("B0") >= 0) or self.nSameAngular >= 3:
                    if self.nSameAngular >= 3:
                        self.stepmotor.stopMoving()
                    check_result = self.checkMovingStatus(check_result)
                    if check_result == "FAILED TO OPEN" or check_result == "ERROR":
                        self.bool_pause = True
                        AppResource.ins().sendMessage("STEPMOTOR_STOP", "ERROR")
                    # end if
                # end if
            # end else
        # end while
        logger.info("THREAD STEPMOTOR EXITED")

    def checkMovingStatus(self, check_result):
        self.nSameAngular = 0
        # 重新选择运动参数
        # 'B000B100B000'
        check_result = self.stepmotor.checkMoveState()
        print("CHECK MOVING STATE " + check_result)
        logger.info("CHECK MOVING STATE " + check_result)
        if check_result == 'END':
            print("MOTOR ARRIVED, nArrived=" + str(self.nArrived) )
            logger.info("MOTOR ARRIVED, nArrived=" + str(self.nArrived) )
            self.nArrived = self.nArrived + 1
            if self.nArrived >= 3:
                self.bool_pause = True
                print("MOTOR STOP AND SEND STEPMOTOR_STOP TO USER")
                logger.info("MOTOR STOP AND SEND STEPMOTOR_STOP TO USER")
                AppResource.ins().sendMessage("STEPMOTOR_STOP", "OK")
            else:
                return "ARRIVED"


        else:
            self.nArrived = 0
            print("CHANGE MOVE MODE")
            logger.info("CHANGE MOVE MODE")
            self.bool_pause = False
        return check_result


