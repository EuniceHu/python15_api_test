# encoding=utf_8
# @Author  ： 豆子
from configparser import ConfigParser

from douzi_0323.commons import filepath


class ConfigsParse(object):
    def __init__(self):
        self.cp = ConfigParser()
        self.cp.read(filepath.config_dir, encoding='utf-8')

    def get(self, section, option):
        return self.cp.get(section, option)

    def getint(self, section, option):
        return self.cp.getint(section, option)

    def getboolean(self, section, option):
        return self.cp.getboolean(section, option)


if __name__ == '__main__':
    cp = ConfigsParse()
    a = cp.get('root', 'level')
    print(a)
