import json
import time
import tkinter as tk
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

# Window draw
win = tk.Tk()
win.title(cfg[4])
win.geometry('1080x720')
win.iconbitmap(cfg[3])
win['bg'] = cfg[5]
win.mainloop()

if cfg[0]:
    if time.time() - start >= 60:
        log.toLog(f"Program was running for {(time.time() - start)//60} minutes and {(time.time() - start) - (((time.time() - start)//60) * 60)} seconds")
    else:
        log.toLog(f"Program was running for {time.time() - start} seconds")