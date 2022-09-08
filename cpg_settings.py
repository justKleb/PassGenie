import tkinter as tk
import json
import sys

try:
    f = open('./settings.json', 'r')
except:
    print("Couldn't open settings file. Ff you haven't yet, run main file first!")
cfg = json.loads(f.read())
f.close()

def apply_changes(toChange, toWhat):
    cfg["Settings"][toChange] = toWhat
def get_current(toGet):
    return cfg["Settings"][toGet]
def save_cfg():
    f = open('./settings.json', 'w')
    json.dump(cfg,f)
    f.close()
w = tk.Tk()
w.config(width=1000, height=500)
w.resizable(width=False, height=False)
if len(sys.argv) > 1:
    if sys.argv[1]:
        w.title("Config - CPG")
else:
    w.title("Configure")
w.iconbitmap('./icon.ico')
offsetL = tk.Label(w, text="                                   ").grid(column=0)
offsetR = tk.Label(w, text="                                   ").grid(column=2)
SettingsLabel = tk.Label(w, text="Settings").grid(column=1, row=0)

b0 = tk.Button(w, command=lambda : apply_changes('runTimeTimer', not get_current('runTimeTimer')))
b0.grid(column=1, row=1)
b1 = tk.Button(w, command=lambda : apply_changes('launchTimeTimer', not get_current('launchTimeTimer')))
b1.grid(column=1, row=2)
b2 = tk.Button(w, command=lambda : apply_changes('drawWindow', not get_current('drawWindow')))
b2.grid(column=1, row=3)
offsetD = tk.Label(w, text="\n").grid(column=1, row=4)
saveB = tk.Button(w, text='Save', command=save_cfg).grid(column=1,row=5)


def update():
    b0.config(text=f"Runtime Timer: {get_current('runTimeTimer')}")
    b1.config(text=f"Launch Time Timer: {get_current('launchTimeTimer')}")
    b2.config(text=f"Draw Window: {get_current('drawWindow')}", state=tk.DISABLED)
    w.after(100, update)
w.after(100, update)
w.mainloop()