import configparser

class Config:

    def __init__(self,file):
        self.config=configparser.ConfigParser()
        self.config.read(file,encoding='utf-8')
        self.rawconfig=configparser.RawConfigParser()
        self.rawconfig.read(file,encoding='utf-8')

    def config_get(self,section,option):
        value=self.config.get(section,option)
        return value

    def rawconfig_get(self,section,option):
        value=self.rawconfig.get(section,option)
        return value

    def config_getint(self,section,option):
        value=self.config.getint(section,option)
        return value

    def config_getboolean(self,section,option):
        value=self.config.getboolean(section,option)
        return value

    def config_getsection(self):
        value=self.config.sections()
        return value

    def config_getoption(self,section):
        value=self.config.options(section)
        return value

    def config_getitem(self,section):
        value=self.config.items(section)
        return value


if __name__ == '__main__':

    data=Config('data.config')
    print(data.rawconfig_get('LOGGER','formatter'))
