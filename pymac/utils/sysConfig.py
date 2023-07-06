#coding=utf-8
import configparser
import os


class SysConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        return

    def load(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir+"/../config.ini"
        self.config.read(cfgFilePath)

    def save(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cfgFilePath = current_dir + "/../config.ini"
        try:
            with open(cfgFilePath, mode='w' ) as fp:
                self.config.write(fp)
            return True
        except OSError:
            print("Failed to write")
        return False

    def getOption(self, section, option):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        else:
            return None

    def getIntOption(self, section, option):
        if self.config.has_option(section, option):
            return int(self.config.get(section, option))
        else:
            return None

    def setOption(self, section, option, val):
        if not isinstance(val, str):
            val = str(val)
        self.config.set(section, option, val)
        self.save()


if __name__ == '__main__':    
    config = SysConfig()
    config.load()
    print(config.getOption("ANGULAR_ENCODER", "port"))
    config.setOption("ANGULAR_ENCODER", "baudrate", 115200)
    print(config.getIntOption("ANGULAR_ENCODER", "baudrate"))
