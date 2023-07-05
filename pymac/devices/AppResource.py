# from service.threadCollect import ThreadCollect
import logging

logger = logging.getLogger('service.log')
class AppResource:
    __instance = None
    # def __new__(cls, ):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(AppResource, cls).__new__(cls)
    #     return cls.instance

    def __init__(self):
        if not AppResource.__instance:
            self.list_channel = []
            self.gApi = None
            self.bool_exit = False
            self.threadCollection = None
            self.window = None

    @classmethod
    def ins(cls):
        if not AppResource.__instance:
            cls.__instance = AppResource()

        return cls.__instance


    def setWindow(self, win):
        self.window = win

    def setGlobalApi(self, api):
        self.gApi = api

    def setThreadCollection(self, thrd):
        self.threadCollection = thrd

    def getApi(self):
        return self.gApi

    def addChannel(self, channel):
        self.list_channel.append(channel)

    def clearChannels(self):
        self.list_channel.clear()

    def getChannelList(self):
        return self.list_channel

    def updateChannelValue(self, chan_id, sensor_value):
        for channel in self.list_channel:
            if channel.id == chan_id:
                channel.sensorValue = sensor_value

    def updateChannelAdValue(self, chan_id, ad_value):
        for channel in self.list_channel:
            if channel.id == chan_id:
                channel.adValue = ad_value

    def startCollection(self):
        if self.threadCollection is not None:
            if not self.threadCollection.started:
                self.threadCollection.start()
            elif self.threadCollection.bool_pause:
                self.threadCollection.resume()
            #
            self.threadCollection.startCollecting()


    def stopCollection(self):
        if self.threadCollection.started:
            self.threadCollection.stopCollecting()

    def sendMessage(self, msg_content, msg_value):
        # if not isinstance( msg_value, "str"):
        #     msg_value = str(msg_value)

        logger.info("SEND MESSAGE: msg_content= " + msg_value + "msg_value=" + msg_value)
        strCmd = """var myEvent = document.createEvent('CustomEvent');myEvent.data = {msg: '"""
        # strCmd = """var myEvent.data = {msg: '"""
        strCmd += msg_content
        strCmd += """',value:'"""
        strCmd += msg_value
        strCmd += """'};myEvent.initEvent('pythonEvent',true,true);document.dispatchEvent(myEvent);"""
        # 在页面中执行脚本
        self.window.evaluate_js(strCmd)

    def sendLiveData(self, window, msgContent, msgValue):
        strCmd = """var myEvent = document.createEvent('CustomEvent');myEvent.data = {msg: '"""
        strCmd += msgContent
        strCmd += """',value:'"""
        strCmd += msgValue
        strCmd += """'};myEvent.initEvent('pyLiveData',true,true);document.dispatchEvent(myEvent);"""
        # 在页面中执行脚本
        window.evaluate_js(strCmd)