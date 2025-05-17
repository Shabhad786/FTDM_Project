import configparser
config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
       URL= config.get('common info','Ftdm_URL' )
       return URL

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password