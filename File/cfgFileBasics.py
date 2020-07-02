import configparser

parser = configparser.ConfigParser()
text = parser.read("config.cfg")

#print sections
print(parser.sections())
print(parser.has_section("SECTION1"))

#read values
print(parser['DEFAULT']['ip'])
#converts into desirable data type
print(parser['DEFAULT'].getboolean('working'))


try:
    print(parser['DEFAULT']['TRIAL'])
except KeyError as err:
    print("YOu are trying to access TRIAL which is not available")

