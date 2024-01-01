"""
Settings module, reads the settings from a settings.json file. If it does not exist or a new setting
has appeared it will creat from the defaults in the initialise function.
"""
import json
from datetime import datetime

VERSION = '2.0.2'


def writesettings():
    """Write settings to json file"""
    settings['LastSave'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('settings.json', 'w', encoding='utf-8') as outfile:
        json.dump(settings, outfile, indent=4, sort_keys=True)


def initialise():
    """These are the default values written to the settings.json file the first time the app is run"""
    isettings = {'LastSave': '01/01/2000 00:00:01',
                 'cputemp': '/sys/class/thermal/thermal_zone0/temp',
                 'gunicornpath': './logs/',
                 'ion-length': 16,
                 'ion-port': '/dev/ttyUSB2',
                 'ion-speed': 9600,
                 'ion-start': 9,
                 'ion-string1': 'fiAwNSAwQiAwMA0=',  # base64 encoded
                 'logappname': 'Pumpreader-Py',
                 'logfilepath': './logs/pumpreader.log',
                 'pyro-laseroff': 'pQCl',  # base64 encoded
                 'pyro-laseron': 'pQGk',  # base64 encoded
                 'pyro-port': '/dev/ttyUSB3',
                 'pyro-speed': 115200,
                 'pyro-readlaser': 'JQ==',  # base64 encoded
                 'pyro-readtemp': 'AQ==',  # base64 encoded
                 'tank-length': 16,
                 'tank-port': '/dev/ttyUSB1',
                 'tank-speed': 9600,
                 'tank-start': 5,
                 'tank-string1': 'UFIxDQ==',  # base64 encoded
                 'tank-string2': 'BQ==',  # base64 encoded
                 'turbo-length': 16,
                 'turbo-port': '/dev/ttyUSB0',
                 'turbo-speed': 9600,
                 'turbo-start': 5,
                 'turbo-string1': 'UFIxDQ==',  # base64 encoded
                 'turbo-string2': 'BQ=='  # base64 encoded
                 }
    return isettings

def readsettings():
    """Read the json file"""
    try:
        with open('settings.json', 'r', encoding='utf-8') as json_file:
            jsettings = json.load(json_file)
            return jsettings
    except FileNotFoundError:
        print('File not found')
        return {}

def loadsettings():
    """Replace the default settings with thsoe from the json files"""
    global settings
    settingschanged = 0
    fsettings = readsettings()
    for item in settings.keys():
        try:
            settings[item] = fsettings[item]
        except KeyError:
            print('settings[%s] Not found in json file using default', item)
            settingschanged = 1
    if settingschanged == 1:
        writesettings()


settings = initialise()
loadsettings()
