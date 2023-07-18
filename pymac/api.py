# coding:utf-8
import json
import sys
import serial
import serial.tools.list_ports
from base.serialDevice import SerialDevice
from devices.AppResource import AppResource
from devices.angularEncoder import AngularEncoder
from devices.stepmotor import Stepmotor
from utils.csvutils import CsvUtils
from utils.sysConfig import SysConfig

import pandas as pd
import json



class Api:
    def __init__(self):
        self.comDevice = SerialDevice()
        self.angularEncoder = AngularEncoder()
        self.stepmotor = Stepmotor()

        self.config = SysConfig()
        self.config.load()



    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')

    def on_error(self, error):
        print(error)

    def getSerialList(self):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            response = {
                'message': ''
            }
            return ""
        else:
            lstCom = []
            for com in plist:
                item = {
                    "name": com.name,
                    "title": com.name
                }
                lstCom.append(item)
            response = {
                'message': 'ok',
                'list': lstCom
            }
            print(lstCom)
            return response

    def openSerial(self, port, baudrate):
        return self.comDevice.openSerial(port, baudrate)

    def closeseSerial(self):
        return self.comDevice.closeseSerial()

    def writeSerial(self, data):
        return self.comDevice.writeSerial(data)

    def readSerial(self):
        return self.comDevice.readSerial()

    def getParam(self, paramName):
        print(paramName)
        param = self.sysParamService.getParam(paramName)
        if (param):
            response = {
                'code': 200,
                'message': 'ok',
                'paramValue': param.get('param_value')
            }
        else:
            response = {
                'code': 201,
                'message': 'no data',
                'paramValue': ''
            }
        print(response)
        return response

    def setSensorList(self, sensor_list):
        csvutils = CsvUtils()
        json_rows = json.loads(sensor_list)
        csvutils.writeChannelLis(json_rows)
        response = {
            'code': 200,
            'message': 'OK'
        }
        return response

    def insertCalibrationRow(self, sensor_list):
        csvutils = CsvUtils()
        json_rows = json.loads(sensor_list)
        if csvutils.insertCalibrationRow(json_rows):
            response = {
                'code': 200,
                'message': 'OK'
            }
        else:
            response = {
                'code': 201,
                'message': '保存失败'
            }
        return response

    def getSensorList(self):
        csvutils = CsvUtils()
        rows = csvutils.readChannelList()
        response = {
            'code': 200,
            'message': 'OK',
            'result': rows
        }
        return response

    def getOption(self, section, option_name):
        if not self.config.config.has_option(section, option_name):
            print("no the option")
            return ""
        return self.config.getOption(section, option_name)

    def setOptions(self, section, option_name, param_value):
        if not self.config.config.has_option(section, option_name):
            response = {
                'code': 201,
                'message': 'no the option',
                'result': ""
            }
            print(response)
            return response
        else:
            self.config.setOption(section, option_name, param_value)
            response = {
                'code': 200,
                'message': 'ok',
                'result': ""
            }
            print(response)
            return response

    def setParam(self, paramName, paramValue):
        print("setparam" + paramName + ":" + paramValue)
        result = self.sysParamService.setParam(paramName, paramValue)
        response = {
            'code': 200,
            'message': 'ok',
            'result': result
        }
        print(response)
        return response

    def setPassword(self, params):
        try:
            json_params = json.loads(params)
            oldPassword = json_params['oldPassword']
            newPassword = json_params['newPassword']
            print("setPassword " + oldPassword + ":" + oldPassword)
            savedPwd = self.config.getOption("ADMIN_PWD", "pwd")
            if savedPwd == oldPassword:
                self.config.setOption("ADMIN_PWD", "pwd", newPassword)
                self.config.save()  # Save changes
                response = {
                    'code': 200,
                    'message': 'ok',
                    'result': ""
                }
                return response
            else:
                response = {
                    'code': 201,
                    'message': '密码错误',
                    'result': ""
                }
                return response
        except Exception as e:
            response = {
                'code': 201,
                'message': e.args[0],
                'result': ""
            }
            return response

    def checkPassword(self, params):
        try:
            json_params = json.loads(params)
            print(json_params['password'])
            password = json_params['password']
            print("checkPassword " + password )
            oldPwd = self.config.getOption("ADMIN_PWD", "pwd")
            if oldPwd == password:
                response = {
                    'code': 200,
                    'message': 'ok',
                    'result': ""
                }
                return response
            else:
                response = {
                    'code': 201,
                    'message': '密码错误',
                    'result': ""
                }
                return response
        except Exception as e:
            response = {
                'code': 201,
                'message': e.args[0],
                'result': ""
            }
            return response

    def getPassword(self,):
        print("getPassword ")
        oldPwd = self.config.getOption("ADMIN_PWD", "pwd")
        response = {
            'code': 200,
            'message': 'ok',
            'result': oldPwd
        }
        return response

    def gotoAngular0(self, params):
        json_params = json.loads(params)
        print(json_params['targetAngular'])
        n_angular = float(json_params['targetAngular'])
        n_angular = 10
        res = self.stepmotor.moveStepAngular(n_angular)
        response = {
            'code': 200,
            'message': res
        }
        return response

    def gotoAngular(self, params):
        json_params = json.loads(params)
        print(json_params['targetAngular'])
        n_angular = float(json_params['targetAngular'])
        res = self.stepmotor.moveStepAngular(n_angular)
        code = 200
        if res == "FAILED TO OPEN" or res == "ERROR":
            code = 201

        response = {
            'code': code,
            'message': res
        }
        return response

    def stopMotor(self, params):
        json_params = json.loads(params)
        # print(json_params['targetAngular'])
        # n_angular = float(json_params['targetAngular'])
        # n_angular = 10
        res = self.stepmotor.stopMoving()
        response = {
            'code': 200,
            'message': res
        }
        return response

    def startCollection(self):
        appResource = AppResource().ins()
        res = appResource.startCollection()
        response = {
            'code': 200,
            'message': res
        }
        return response

    def stopCollection(self):
        appResource = AppResource().ins()
        res = appResource.stopCollection()
        response = {
            'code': 200,
            'message': res
        }
        return response

    def get_log_data(self):
        mock_data = [
            {
                'index': 1,
                'time': '2021-12-21 13:45:00',
                'operation': '倒入传感器',
                'parameter': 'mock parameter',
                'content': 'mock content'
            },

        ]
        response = {
            'code': 200,
            'message': 'OK',
            'result': mock_data
        }
        return response

    def read_flow_data(self, file_name, columns):
        csv_utils = CsvUtils()
        data = csv_utils.read(file_name)

        # Convert list of lists to DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Convert DataFrame to JSON
        json_data = json.loads(df.to_json(orient='records', indent=4))
        return df

    def queryFlow(self, params):
        json_params = json.loads(params)
        keyword = json_params['keyword']
        column = json_params['column']
        orderby = json_params['orderby']

        columns = ['id', 'flow_name', 'flow_type', 'driver', 'sensor_protocol', 'device_name', 'device_protocol',
                   'move_seconds', 'wait_seconds',
                   'read_times', 'calcuate_method', 'precise', 'sensor_sum', 'sensor_name', 'scale_list']

        df = self.read_flow_data('flow_data.csv', columns)

        # notes: add filter and sort data based on the parameters
        #
        #

        json_data = json.loads(df.to_json(orient='records', indent=4))

        response = {
            'code': 200,
            'message': 'OK',
            'result': json_data
        }

        return response

    def editFlow(self, flow_data):
        flow_data = json.loads(flow_data)
        flow_id = flow_data.get('id')

        columns = ['id', 'flow_name', 'flow_type', 'driver', 'sensor_protocol', 'device_name', 'device_protocol',
                   'move_seconds', 'wait_seconds',
                   'read_times', 'calcuate_method', 'precise', 'sensor_sum', 'sensor_name', 'scale_list']
        df = self.read_flow_data('flow_data.csv', columns)

        # find the row with id
        row_to_edit = df.loc[df['id'] == flow_id]
        # return an error if no row was found,
        if row_to_edit.empty:
            response = {
                'code': 404,
                'message': 'No flow found with that id.'
            }
            return response

        # Update the row ( update csv for now)
        for key, value in flow_data.items():
            if key in df.columns:
                df.loc[df['id'] == flow_id, key] = value

        csv_utils = CsvUtils()
        new_data = df.values.tolist()
        csv_utils.write(new_data, 'flow_data.csv')

        # notes: more states needed
        response = {
            'code': 200,
            'message': 'Flow data updated successfully.'
        }
        return response

    def getFlow(self, flow_id):
        columns = ['id', 'flow_name', 'flow_type', 'driver', 'sensor_protocol', 'device_name', 'device_protocol',
                   'move_seconds', 'wait_seconds',
                   'read_times', 'calcuate_method', 'precise', 'sensor_sum', 'sensor_name', 'scale_list']
        df = self.read_flow_data('flow_data.csv', columns)

        # find the row with id
        row_to_fetch = df.loc[df['id'] == flow_id]

        # return an error if no row was found
        if row_to_fetch.empty:
            response = {
                'code': 404,
                'message': 'No flow found with that id.'
            }
        else:
            response = {
                'code': 200,
                'message': 'Flow fetched successfully.',
                'result': row_to_fetch.to_dict(orient='records')[0]  # Convert the DataFrame row to a dictionary
            }
        return response

    def addFlow(self, flow_data):
        flow_data = json.loads(flow_data)

        columns = ['id', 'flow_name', 'flow_type', 'driver', 'sensor_protocol', 'device_name', 'device_protocol',
                   'move_seconds', 'wait_seconds', 'read_times', 'calcuate_method', 'precise', 'sensor_sum',
                   'sensor_name', 'scale_list']
        df = self.read_flow_data('flow_data.csv', columns)

        # Convert the 'id' column to integer type
        df['id'] = df['id'].astype(int)

        # Now it's safe to find the max id and add 1 to create a new id
        new_id = df['id'].max() + 1

        # Assign the new id to the flow_data dictionary
        flow_data['id'] = str(new_id)

        # Create a new DataFrame for the new flow data
        new_flow_df = pd.DataFrame([flow_data])

        # Concatenate the original DataFrame with the new DataFrame
        df = pd.concat([df, new_flow_df], ignore_index=True)

        csv_utils = CsvUtils()
        new_data = df.values.tolist()
        csv_utils.write(new_data, 'flow_data.csv')

        response = {
            'code': 200,
            'message': 'Flow data added successfully.'
        }
        return response

    def deleteFlow(self, flow_id):
        columns = ['id', 'flow_name', 'flow_type', 'driver', 'sensor_protocol', 'device_name', 'device_protocol',
                   'move_seconds', 'wait_seconds', 'read_times', 'calcuate_method', 'precise', 'sensor_sum',
                   'sensor_name', 'scale_list']
        df = self.read_flow_data('flow_data.csv', columns)

        # Check if the flow_id exists in the DataFrame
        if flow_id not in df['id'].values:
            response = {
                'code': 404,
                'message': 'No flow found with that id.'
            }
            return response

        # Remove the row with the specified flow_id
        df = df[df['id'] != flow_id]

        csv_utils = CsvUtils()
        new_data = df.values.tolist()
        csv_utils.write(new_data, 'flow_data.csv')

        response = {
            'code': 200,
            'message': 'Flow data deleted successfully.'
        }
        return response


if __name__ == '__main__':
    str_item = '[["1","99002310","COM20","1"],["2","99002311","COM20","2"],["3","99002312","COM20","3"],["4","99002313","COM20","4"],["5","99002314","COM20","5"],["6","99002315","COM20","6"],["7","99002316","COM20","7"],["8","99002317","COM20","8"],["9","99002318","COM20","9"],["10","99002319","COM20","10"],["11","99002320","COM20","11"],["12","99002321","COM20","12"],["13","99002322","COM20","13"],["14","99002323","COM20","14"],["15","99002324","COM20","15"],["16","99002325","COM20","16"]]'
    #str_item = '{"a": 1234}'
    json_item = json.loads(str_item)
    #print(json_item)

    api = Api()  # Create an instance of the Api class

    # Test queryFlow method
    # Define some dummy params
    params = {
        "keyword": "some keyword",
        "column": "some column",
        "orderby": "desc"
    }
    result = api.queryFlow(json.dumps(params))
    print(result)









