import json
import time
from utils.cpg_utils import clearLog, toLog
from utils.cpg_utils import utils
from os import path, mkdir

if not path.exists('run/'):
    mkdir('run')

clearLog()
start = time.perf_counter()

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
                                               "attemptKeyGenOnStart": False, "appIcon": -1,
                                               "appTitle": -1, "background": "#110f1f", "drawWindow": True, "DEV": False}})
    configFile.write(fillEmptyConfig)
    configFile.close()
afterwardCheck = open('./settings.json', 'w+')

if path.exists('./settings.json') and afterwardCheck.read() == '':
    fillEmptyConfig = json.dumps({"Settings": {"runTimeTimer": True, "launchTimeTimer": True,
                                               "attemptKeyGenOnStart": False, "appIcon": -1,
                                               "appTitle": -1, "background": "#110f1f", "drawWindow": True, "DEV": False}})
    afterwardCheck.write(fillEmptyConfig)
    afterwardCheck.close()

def cfgGet():
    cfg = []
    settingsFile = open('./settings.json')
    setts = json.load(settingsFile)
    settingsFile.close()
    toLogSETTINGS = []
    for i in setts["Settings"]:
        toLogSETTINGS.append(f'{i} is set to {setts["Settings"][i]}\n    ')
        cfg.append(setts["Settings"][i])
    toLog(f"Settings: {', '.join(toLogSETTINGS)}")
    return cfg


cfg = cfgGet()

if cfg[1]:
    toLog("Launch took %s seconds" % utils.toDouble((time.perf_counter() - start) + 0.001))

if cfg[6]:
    if not cfg[7]:
        import cpg_gui
    else:
        with open('./passgenie-gui') as gui_exec:
            exec(gui_exec.read())
    if cfg[0]:
        toLog("Program was running for %s seconds" % utils.toDouble((time.perf_counter() - start) + 0.001))
