import json
import time
from utils.cpg_utils import clear_log, to_log
from utils.cpg_utils import utils
from os import path, mkdir

if not path.exists('run/'):
    mkdir('run')

clear_log()
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
    with open('settings.json', 'w') as nonexistent_config_file:
        createConfig = json.dumps({"Settings": {"runTimeTimer": True, "launchTimeTimer": True,
                                                   "drawWindow": True, "DEV": False}})
        nonexistent_config_file.write(createConfig)

with open('./settings.json', 'r') as check_after:
    if path.exists('./settings.json') and check_after.read() == '':
        with open("./settings.json", "w") as empty_config:
            fill_empty = json.dumps({"Settings": {"runTimeTimer": True, "launchTimeTimer": True,
                                                       "drawWindow": True, "DEV": False}})
            empty_config.write(fill_empty)

def cfg_get():
    global cfg
    with open('./settings.json') as cfg_file:
        cfgs = json.load(cfg_file)
        cfg = [*cfgs["Settings"].values()]
    to_log(f"Settings: {', '.join(str(i) for i in cfg)}")
    return cfg


cfg = cfg_get()

if cfg[1]:
    to_log("Launch took %s seconds" % utils.to_double((time.perf_counter() - start) + 0.001))

if cfg[2]:
    if cfg[3]:
        try:
            import cpg_gui
        except:
            import traceback as tb
            tbck = tb.format_exc()
            to_log(tbck, 3)
    else:
        try:
            with open('./passgenie-gui') as gui_exec:
                    exec(gui_exec.read())
        except:
            import traceback as tb
            tbck = tb.format_exc()
            to_log(tbck, 3)

    if cfg[0]:
        to_log("Program was running for %s seconds" % utils.to_double((time.perf_counter() - start) + 0.001))
