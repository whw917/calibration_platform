# coding:utf-8
import logging
import time
import webview
from api import Api
from base.serialDevice import SerialDevice
from devices.AppResource import AppResource
from devices.threadEncoder import ThreadEncoder
from protocol.channelEntity import ChannelEntity
from service.threadCollect import ThreadCollect
from utils.csvutils import CsvUtils
from utils.dateUtils import DateUtils
from utils.sysConfig import SysConfig

global gApi
global bExit
global gWindow
bExit = False

logger = logging.getLogger('service.log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('service.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.info('SERVICE STARTED')


def on_closed():
    print('pywebview window is closed')
    global bExit
    bExit = True
    appResource = AppResource.ins()
    appResource.bool_exit = True
    time.sleep(2)


def on_closing():
    print('pywebview window is closing')
    global bExit
    bExit = True
    appResource = AppResource.ins()
    appResource.bool_exit = True
    time.sleep(2)


def on_shown():
    print('pywebview window shown')


def on_loaded():
    print('DOM is ready')

    # unsubscribe event listener
    webview.windows[0].loaded -= on_loaded


#    //webview.windows[0].load_url('https://google.com')


def python_main(win):
    appResource = AppResource.ins()
    appResource.setThreadCollection(ThreadCollect())
    # appResource.startCollection()
    #
    # csvutils = CsvUtils()
    # list_channel = csvutils.readChannelList()
    # for chan in list_channel:
    #     # 1	99002310	COM19	1	35	1
    #     item = ChannelEntity()
    #     item.id = int(chan[0])
    #     item.nodeNum = int(chan[1])
    #     item.port = chan[2]
    #     item.slaveAddr = int(chan[3])
    #     item.sensorType = int(chan[4])
    #     item.channel = int(chan[5])
    #     appResource.addChannel(item)

    # 测试模式不开始线程
    # threadEncoder = ThreadEncoder(win)
    # threadEncoder.start()

    # threadEncoder.join()
    while not appResource.bool_exit:
        print(DateUtils.now2full())
        time.sleep(1)


if __name__ == '__main__':
    api = Api()
    gApi = api
    app = AppResource.ins()
    app.setGlobalApi(gApi)

    window = webview.create_window('角度标定', 'http://localhost:8080', js_api=api, confirm_close=True)
    # window = webview.create_window('自动标定', './home/index.html', js_api=api, confirm_close=True)
    window.events.closed += on_closed
    app.setWindow(window)
    # window.events.closed += on_closed
    # window.events.closing += on_closing
    # window.events.shown += on_shown
    # window.events.loaded += on_loaded
    # gWindow = window
    # webview.start(python_main, window, debug=False)

    webview.start(python_main, window, debug=True, http_server=True, gui='edgechromium')
    # webview.start(python_main, window, debug=True, http_server=True, gui='mshtml')