import json
import time
import tkinter as tk
from utils.cpg_utils import log
from utils.cpg_utils import passwordUtils as pU
from utils.cpg_utils import passwordGen as pG
from os import path

log.clearLog()
start = time.time()

if not path.exists('settings.json'):
    configFile = open('settings.json', 'w')
    fillEmptyConfig = json.dumps({"Settings":{"runTimeTimer": True,"launchTimeTimer": True,"attemptKeyGenOnStart": False,"appIcon": "icon.ico","appTitle": "Customizable Password Generator","background": "#110f1f","drawWindow": False}})
    configFile.write(fillEmptyConfig)
    configFile.close()

cfg = []
def cfgGet():
    settingsFile = open('settings.json')
    settings = json.load(settingsFile)
    settingsFile.close()
    toLogSETTINGS = []
    for i in settings["Settings"]:
        toLogSETTINGS.append(f'{i} is set to {settings["Settings"][i]}\n    ')
        cfg.append(settings["Settings"][i])
    log.toLog(f"Settings: {', '.join(toLogSETTINGS)}")

cfgGet()

pU.brute(pG.genInBase64(10), 1)

#print(pG.genRandomLetters(1000000))

if cfg[1]:
    log.toLog("Launch took %s seconds" % (time.time() - start))
    print("Launch took %s seconds" % (time.time() - start))
# Window draw
if cfg[6]:

    win = tk.Tk()
    canvas = tk.Canvas(win, width=1080, height=720)
    canvas.grid(columnspan=10, rowspan=10)
    win.title(cfg[4])
    win.iconbitmap(cfg[3])
    win.resizable(width=False, height=False)
    canvas['bg'] = cfg[5]
    options = ['Custom', 'Random Symbols', 'Random Numbers', 'Random Letters', 'Random Through Mouse', 'Mirror Prev. Part']
    optionsVar = tk.StringVar(win)
    optionsVar.set('None')
    label = tk.Label(win, text="Customizable Password Generator", font='Arial 24 bold', bg=cfg[5], fg='#FFFFFF')
    label.grid(column=0, row=0)
    menu = tk.OptionMenu(win, optionsVar, *options)
    menu.grid(column=0, row=5)
    menu.configure(relief=tk.FLAT)
    buttonAdd = tk.Button(win, text="ADD")
    buttonAdd.grid(column=6, row=5)
    win.mainloop()

if cfg[0]:
    if time.time() - start >= 60:
        log.toLog(f"Program was running for {(time.time() - start)//60} minutes and {(time.time() - start) - (((time.time() - start)//60) * 60)} seconds")
    else:
        log.toLog(f"Program was running for {time.time() - start} seconds")