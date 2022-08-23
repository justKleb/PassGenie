import json
import time
from utils.cpg_utils import log

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
    log.toLog("Launch took %s seconds" % (time.time() - start))
    print("Launch took %s seconds" % (time.time() - start))
