import json
import time
from utils.cpg_utils import clearLog, toLog
from utils.cpg_utils import passwordUtils as pU
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils
from os import path, system, mkdir
import _curses as curses
import curses as crs
import pyperclip

if not path.exists('run/'):
    mkdir('run')

clearLog()
start = time.time()

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"


def settings():
    NotImplemented


if not path.exists('./settings.json'):
    configFile = open('settings.json', 'w')
    fillEmptyConfig = json.dumps({"Settings": {"runTimeTimer": True, "launchTimeTimer": True,
                                               "attemptKeyGenOnStart": False, "appIcon": "icon.ico",
                                               "appTitle": "empty", "background": "#110f1f", "drawWindow": False}})
    configFile.write(fillEmptyConfig)
    configFile.close()
afterwardCheck = open('./settings.json', 'w+')
if path.exists('./settings.json') and afterwardCheck.read() == '':
    fillEmptyConfig = json.dumps({"Settings": {"runTimeTimer": True, "launchTimeTimer": True,
                                               "attemptKeyGenOnStart": False, "appIcon": "icon.ico",
                                               "appTitle": "empty", "background": "#110f1f", "drawWindow": False}})
    afterwardCheck.write(fillEmptyConfig)
    afterwardCheck.close()
cfg = []


def cfgGet():
    settingsFile = open('./settings.json')
    setts = json.load(settingsFile)
    settingsFile.close()
    toLogSETTINGS = []
    for i in setts["Settings"]:
        toLogSETTINGS.append(f'{i} is set to {setts["Settings"][i]}\n    ')
        cfg.append(setts["Settings"][i])
    toLog(f"Settings: {', '.join(toLogSETTINGS)}")


cfgGet()

if cfg[1]:
    toLog("Launch took %s seconds" % utils.toDouble((time.time() - start) + 0.001))

