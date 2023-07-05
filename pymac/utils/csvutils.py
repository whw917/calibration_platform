#-*-encoding:utf-8-*-
import csv
import os
from datetime import datetime

from utils.dateUtils import DateUtils


class CsvUtils:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "\\..\\data\\sensor_list.csv"
        self.fileName = cfgFilePath

    def reset(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "\\..\\data\\sensor_list_"
        os.rename(self.fileName, cfgFilePath + self.now2fullName() + ".csv")

    def now2fullName(self):
        now = datetime.now()
        return now.strftime('%Y_%m_%d_%H_%M_%S')

    def readChannelList(self):
        #读取csv文件
        # with open("C:\\Users\\A9050031\\Desktop\\test.csv", "r") as f:
        rows = []
        with open(self.fileName, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                rows.append(row)
        # with end
        return rows

    def read(self, csv_file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "\\..\\data\\" + csv_file

        #读取csv文件
        # with open("C:\\Users\\A9050031\\Desktop\\test.csv", "r") as f:
        rows = []
        with open(cfgFilePath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                rows.append(row)
        # with end
        return rows

    def write(self, rows, csv_file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "\\..\\data\\" + csv_file

        # row = ['7', 'hanmeimei', '23', '81', '78', '78']
        out = open(cfgFilePath, "w", newline="")
        csv_writer = csv.writer(out, dialect="excel")
        csv_writer.writerows(rows)

    def writeChannelLis(self, rows):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "\\..\\data\\sensor_list.csv"
        # row = ['7', 'hanmeimei', '23', '81', '78', '78']
        out = open(cfgFilePath, "w+", newline="")
        csv_writer = csv.writer(out, dialect="excel")
        csv_writer.writerows(rows)

    def insertCalibrationRow(self, rows):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            cfgFilePath = current_dir + "\\..\\data\\calibration_" + DateUtils.dateFileName()+".csv"
            # row = ['7', 'hanmeimei', '23', '81', '78', '78']
            header = ""
            if not os.path.exists(cfgFilePath):
                # 1,99002310,COM19,1,35,1,2023/5/18 14:04,1.08461
                header = [['id', '节点号', '端口','地址', '传感器类型', '通道','标定时间', "测量值", "AD值", "参数值"]]

            out = open(cfgFilePath, "a+", newline="")

            csv_writer = csv.writer(out, dialect="excel")
            if header != "":
                csv_writer.writerows(header)

            csv_writer.writerows(rows)
            return True

        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    csvutils = CsvUtils()
    rows = csvutils.readChannelList()
    print(rows)
    # row = [['id', 'code', 'port', 'addr'],
    #        ['1', '90001001', 'COM10', '1'],
    #        ['2', '90001002', 'COM10', '2'],
    #        ['3', '90001003', 'COM10', '3'],
    #        ['4', '90001004', 'COM10', '4'],
    #        ['5', '90001005', 'COM10', '5'],
    #        ['6', '90001006', 'COM10', '6'],
    #        ['7', '90001007', 'COM10', '7'],
    #        ]
    # csvutils.write(row)



