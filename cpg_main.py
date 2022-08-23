import json
import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
from utils.cpg_utils import fileUtils as fut
from utils.cpg_utils import percentage as percent
from utils.cpg_utils import crypting as crypt
from utils.cpg_utils import log
from cryptography.fernet import Fernet as fnet

log.clearLog()

start = time.time()

cfg = []
def cfgGet():
    settingsFile = open('settings.json')
    settings = json.load(settingsFile)
    settingsFile.close()
    toLogSETTINGS = []
    for i in settings["Settings"]:
        toLogSETTINGS.append(f'{i} is set to {settings["Settings"][i]}')
        cfg.append(settings["Settings"][i])
        log.toLog(f"Settings: {', '.join(toLogSETTINGS)}")

cfgGet()

if cfg[1]:
    log.toLog("Run took %s seconds" % (time.time() - start))
    print("Run took %s seconds" % (time.time() - start))
