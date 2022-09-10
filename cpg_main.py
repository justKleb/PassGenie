import json
import time
from utils.cpg_utils import log
from utils.cpg_utils import passwordUtils as pU
from utils.cpg_utils import passwordGen as pG
from os import path, system
import _curses as curses
import curses as crs
import pyperclip

log.clearLog()
start = time.time()

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"

def settings():
    try:
        system('cpg_settings.exe 1')
    except:
        system('cpg_settings.py 1')


if not path.exists('./settings.json'):
    configFile = open('settings.json', 'w')
    fillEmptyConfig = json.dumps({"Settings":{"runTimeTimer": True,"launchTimeTimer": True,"attemptKeyGenOnStart": False,"appIcon": "icon.ico","appTitle": "Customizable Password Generator","background": "#110f1f","drawWindow": False}})
    configFile.write(fillEmptyConfig)
    configFile.close()
afterwardCheck = open('./settings.json', 'w+')
if path.exists('./settings.json') and afterwardCheck.read() == '':
    fillEmptyConfig = json.dumps({"Settings":{"runTimeTimer": True,"launchTimeTimer": True,"attemptKeyGenOnStart": False,"appIcon": "icon.ico","appTitle": "Customizable Password Generator","background": "#110f1f","drawWindow": False}})
    afterwardCheck.write(fillEmptyConfig)
    afterwardCheck.close()
cfg = []
def cfgGet():
    settingsFile = open('./settings.json')
    settings = json.load(settingsFile)
    settingsFile.close()
    toLogSETTINGS = []
    for i in settings["Settings"]:
        toLogSETTINGS.append(f'{i} is set to {settings["Settings"][i]}\n    ')
        cfg.append(settings["Settings"][i])
    log.toLog(f"Settings: {', '.join(toLogSETTINGS)}")

cfgGet()

if cfg[1]:
    log.toLog("Launch took %s seconds" % (time.time() - start))

print(f"{RED}CPG - 0.1a{RESET}")
print(f"{CYAN}/help{RESET} for commands!\n")
gens = ['/ranSyms', '/ranNums', '/ranLetters', '/mirrorPrev']
current_pass = []
while True:
    inp = input(f"{CYAN}Add to password(STRING/KEYWORD): {RESET}")
    if inp == gens[0]:
        symbol_amount = input(f'{GREEN}Amount(INT): {RESET}')
        current_pass.append(pG.genInBase64(int(symbol_amount)))
    elif inp == gens[1]:
        symbol_amount = input(f'{GREEN}Amount(INT): {RESET}')
        current_pass.append(pG.genRandomNums(int(symbol_amount)))
    elif inp == gens[2]:
        symbol_amount = input(f'{GREEN}Amount(INT): {RESET}')
        current_pass.append(pG.genRandomLetters(int(symbol_amount)))
    elif inp == gens[3]:
        current_pass.append(pG.mirror(current_pass[-1]))
    elif inp == '/passwordEnd':
        def menu(title, classes, color = 'white'):
            def char(stdscr, ):
                attrs = {}
                opt = {
                    1:'red',
                    2:'green',
                    3:'yellow',
                    4:'blue',
                    5:'magenta',
                    6:'cyan',
                    7:'white'
                }
                col = {v: k for k, v in opt.items()}
                bg = curses.COLOR_BLACK
                curses.init_pair(1, 7, bg)
                attrs['normal'] = curses.color_pair(1)
                curses.init_pair(2, col[color], bg)
                attrs['highlighted'] = curses.color_pair(2)
                c = 0
                option = 0
                while c != 10:

                    stdscr.erase()

                    stdscr.addstr(f"{title}\n", curses.color_pair(1))

                    for i in range(len(classes)):
                        if i == option:
                            attr = attrs['highlighted']
                        else:
                            attr = attrs['normal']

                        stdscr.addstr(f'> ', attr)
                        stdscr.addstr(f'{classes[i]}' + '\n', attr)
                    c = stdscr.getch()

                    if c == curses.KEY_UP and option > 0:
                        option -= 1
                    elif c == curses.KEY_DOWN and option < len(classes) - 1:
                        option += 1
                return option
            return crs.wrapper(char)
        ans = menu('\nPassword have been made. Please choose an option, what to do now?', ['Copy to clipboard','Print-out here', 'Exit without saving'], 'magenta')
        if ans == 0:
            pyperclip.copy(''.join(current_pass))
        elif ans == 1:
            print('\n' + ''.join(current_pass) + '\n')
        elif ans == 2:
            print(f"This will remove {RED}EVERYTHING{RESET} added/generated in password!")
            f = input('Proceed? [Yes/no] : ')
            if f == 'Yes':
                current_pass = []
                print('Done.')
                break
            elif f == 'no':
                a = input("Ok! What to do with it then? [print/copy] : ")
                if a == "print":
                    print(''.join(current_pass))
                elif a == "copy":
                    pyperclip.copy(''.join(current_pass))
                else:
                    print("Didn't recognize option. Aborting.")
                    break
    elif inp == '/exit':
        print('Bye!')
        time.sleep(1)
        break
    elif inp == '/help':
        print(f"""\n{BLUE}Currently aviable commands:{RESET}
        {CYAN}/ranSyms{RESET} - Generates specified amount of random symbols
        {CYAN}/ranNums{RESET} - Generates specified amount of random numbers
        {CYAN}/ranLetters{RESET} - Generates specified amount of random letters
        {CYAN}/mirrorPrev{RESET} - Mirrors previous part of password
        {CYAN}/passwordEnd{RESET} - Ends password creation process with options
        {CYAN}/passTest{RESET} - Test your password on a "brute-force"-like attack
        {CYAN}/settings{RESET} - Open settings dialog
        {CYAN}/exit{RESET} - Exit the programm without saving
        {CYAN}/help{RESET} - Show this message
        {RED}Just type{RESET} to add your stuff in password\n""")
    elif inp == '/passTest':
        is_cracked, string = pU.brute(''.join(current_pass), int(input(f'{RED}Limit time for testing (In minutes) : {RESET}')))
        print(string)
    elif inp == '/settings':
        settings()
    else:
        current_pass.append(inp)
    

if cfg[0]:
    if time.time() - start >= 60:
        log.toLog(f"Program was running for {(time.time() - start)//60} minutes and {(time.time() - start) - (((time.time() - start)//60) * 60)} seconds")
    else:
        log.toLog(f"Program was running for {time.time() - start} seconds")