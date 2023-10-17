from configparser import ConfigParser


#print(config.get("locator","username"))
#print(config.get("basic info","testsiteurl"))

def readConfig(section,key):
    config = ConfigParser()
    config.read("..//ConfigurationData//config.ini")
    return config.get(section,key)



