import random
import base64
import string
from ctypes import windll, wintypes, byref
import time
import numpy as np
import os
from cryptography.fernet import Fernet as fnet
from datetime import datetime as dt
from itertools import product, chain

class log:

    def toLog(toWrite):
        log = open('run/log.log', 'a')
        log.write(f'{dt.now().strftime("[%H:%M:%S]")} {toWrite}\n')
        log.close()
    
    def clearLog():
        try:
            log = open('run/log.log', 'w')
            log.write('')
            log.close()
        except:
            print("Couldn't open the log file")

class utils:

    def getCursorPosX():
        cursor = wintypes.POINT()
        windll.user32.GetCursorPos(byref(cursor))
        return cursor.x
    
    def getCursorPosY():
        cursor = wintypes.POINT()
        windll.user32.GetCursorPos(byref(cursor))
        return cursor.y

    def toDoubleNP(toConv):
        """Converts input into a double using Numpy"""
        toConv = list(x for x in str(toConv))
        toConv = np.array(toConv)
        whereDot = np.where(toConv == '.')[0]
        whereDot = str(whereDot).replace("[", "")
        whereDot = str(whereDot).replace("]", "")
        whereDot = int(whereDot)
        toConv = toConv[:whereDot + 2]
        toConv = np.ndarray.tolist(toConv)
        toConv = ''.join(toConv)
        return float(toConv)

    def toDouble(toConv):
        """Converts input into a double with proper round-up"""
        toConv = str(toConv)
        whereDot = 0
        pos = 0
        for x in toConv:
            pos += 1
            if x == '.':
                savePos = pos
                toConv = list(toConv)
                if float(toConv[savePos + 1]) + 1 >= 10:
                    #toConv = list(toConv)
                    toConv[savePos] = int(toConv[savePos]) + 1
                    toConv[savePos + 1] = 0
                else:
                    if float(toConv[savePos + 2]) >= 5:
                        #toConv = list(toConv)
                        toConv[savePos + 1] = int(toConv[savePos + 1]) + 1
                toConv = toConv[:savePos + 2]
                toConv = ''.join(str(y) for y in toConv)
        return float(toConv)

    def allVars(chSet, maxleng):
        return (''.join(candidate)
            for candidate in chain.from_iterable(product(chSet, repeat=i)
            for i in range(1, maxleng + 1)))

class fileUtils:

    def savePassword(toSave, saveName: str):
        """Saves password into '.pass' file."""
        log.toLog(f"Saving to: {saveName}")
        if os.path.exists('passwords/' + saveName + '.pass'):
            log.toLog(f"{saveName} save name is used.")
            print("Password name is used! Use update function instead!")
            return "Password name is used!"
        else:
            log.toLog(f"{saveName} saved")
            f = open('passwords/' + saveName + '.pass', 'w')
            f.write(str(toSave))
            f.close()

    def updatePassword(toSave, saveName):
        """Updates saved password file with new one"""
        log.toLog(f"Updating save: {saveName}")
        if not os.path.exists('passwords/' + saveName + '.pass'):
            log.toLog(f"{saveName} save doesn't exist")
            print("File doesn't exist! Use save function instead!")
            return "File doesn't exist!"
        else:
            log.toLog(f"{saveName} save updated")
            f = open('passwords/' + saveName + '.pass', 'w')
            f.write(str(toSave))
            f.close()

    def deletePassword(delName):
        """Deletes saved password file"""
        log.toLog(f"Deleting save: {delName}")
        if not os.path.exists('passwords/' + delName + '.pass'):
            log.toLog(f"{delName} save doesn't exist")
            print("File doesn't exist! Password should exist lol")
            return "File doesn't exist!"
        else:
            os.remove('passwords/' + delName + '.pass')
            log.toLog(f"{delName} is deleted")

class passwordGen:
    def genInBase64(leng: int):
        """Generates specified amount of randomly generated symbols (Numbers and letters)
        
        Args:
        First: Specifiy Length (int)"""
        toConv = []
        base64Conv = ""
        for x in range(leng):
            toConv.append(random.randint(0,9))
            if len(toConv) == leng:
                ConvStr = ''.join(str(y) for y in toConv)
                base64Conv = base64.b64encode(ConvStr.encode('ascii'))
                base64Conv = base64Conv.decode('utf-8')
            if len(base64Conv) > leng:
                for i in range(len(base64Conv) - leng):
                    base64Conv = base64Conv[:-1]
            #base64Conv = ''.join(base64Conv)

        return base64Conv
    
    def mirror(toMirror: str):
        """Mirrors the input and returns it

        Args:
        First: String to mirror"""
        a = list(toMirror)
        out = []
        for x in range(len(a)):
            out.append(a[(len(toMirror) - 1)-x])
        return ''.join(out)
    
    def genRandomNums(leng: int):
        """Generates specified amount of randomly generated numbers

        Args:
        First: Specifiy Length (int)"""
        nums = []
        for x in range(leng):
            nums.append(random.randint(0,9))
            if len(nums) == leng:
                convStr = ''.join(str(y) for y in nums)
        return convStr

    def genRandomLetters(leng: int):
        """Generates specified amount of randomly generated letters
        
        Args:
        First: Specifiy Length (int)"""
        lets = []
        letsBase = list(string.ascii_lowercase)
        for x in range(leng):
            lets.append(letsBase[random.randint(0,25)])
            if len(lets) == leng:
                convStr = ''.join(lets)
        return convStr

    def genViaMouse(leng: int):
        """Generates specified amount of randomly generated letters using mouse coordinates.\n
        Takes (length ÷ 10) seconds to generate.\n
        Move mouse while generating, since it's based on it's coordinates, if mouse isn't moving - after 6 characters numbers are going to repeat.
        
        Args:
        First: Specifiy Length (int)"""
        posArray = ['']
        for i in range(leng):
            if len(posArray) >= 2:
                while utils.getCursorPosY() == posArray[-1]:
                    l = 0
                while utils.getCursorPosX() == posArray[-2]:
                    l = 0
            x = utils.getCursorPosX()
            y = utils.getCursorPosY()
            posArray.append(x)
            posArray.append(y)
        posArrayStr = ''.join(str(i) for i in posArray)
        if len(posArray) > leng:
            for i in range(len(posArrayStr) - leng):
                posArrayStr = posArrayStr[:-1]
            
        return posArrayStr
class crypting:
    
    def toBase64(toConv):
        """Converts input into Base64 format"""
        toConv = str(base64.b64encode(toConv))
        return toConv

    def toBase16(toConv):
        toConv = str(base64.b16encode(toConv))
        return toConv

    def keyGen():
        if not os.path.exists('passwords/keyGen'):
            f = open('passwords/keyGen', 'wb')
            f.write(fnet.generate_key())
            f.close()
            #print(dt.now().strftime("[%H:%M:%S]") + " Generated key")
            log.toLog("Generated key")
            return True
        else:
            #print(dt.now().strftime("[%H:%M:%S]") + " Key is already generated!")
            log.toLog("Key is already generated!")
            return False

    def updKey():
        print("This will completly overwrite you current generated key, you will loose access to all of your saved passwords\nProceed?")
        ans = input("[Y/n]: ")
        if ans == 'Y':
            print("Overwriting key...")
            f = open('passwords/keyGen', 'wb')
            f.write(fnet.generate_key())
            f.close()
            log.toLog("Key was overwritten!")

        elif ans == 'n':
            print("Canceled.")
            log.toLog("Key overwrite canceled.")
        
        else:
            print(f"There's no {ans} option, reverting operation.")
            log.toLog("Key overwrite canceled. (Wrong option chosen)")
class percentage:

    def AinB(a, b):
        """Returns how much percents is 'a' from 'b'"""
        return (a / b) * 100

    def fromA(a, b):
        """Returns specified percents from 'a' number"""
        return (a/100) * b

    def fromPercent(a, b):
        """Returns number from how much percent is number from it"""
        return a * (100/b)

class passwordUtils:
    def brute(toTest: str, timeInMinutes: float):
        """Simulates real brute-force attack on password, returns True if password did get cracked, False if didn't."""
        syms = str(list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("""1234567890 =-_+/?\|'";:><,.*&7^%$#@!()[]{} """))
        start = time.time()
        log.toLog("Starting password testing")
        for attempt in utils.allVars(syms, 10):
            if attempt == toTest:
                log.toLog(f"Cracked in {time.time() - start} seconds or {(time.time() - start)//60} minutes.")
                return False, f"Cracked in {time.time() - start} seconds or {(time.time() - start)//60} minutes"
            if abs((time.time() - start) - timeInMinutes * 60) <= 0.1:
                log.toLog("That takes longer than specified, password check completed. Password wasn't cracked")
                return True, f"That takes longer than specified, password check completed. Password wasn't cracked"
