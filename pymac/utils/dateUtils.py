# coding=utf-8
from datetime import datetime


class DateUtils():
    def __init__(self):
        self.date = datetime.now()
    @staticmethod
    def now2full():
        now = datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')\

    @staticmethod
    def dateFileName():
        now = datetime.now()
        return now.strftime('%Y_%m_%d')


# if __name__ =='__main__':
#     # print ( DateUtils.now2full())
    