import random
import base64
import string
#from ctypes import windll, wintypes, byref
import time
from datetime import datetime as dt
from itertools import product, chain

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
        raise FileExistsError("Log file not existing")

class utils:

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
                    if toConv[savePos] == '9':
                        toConv[savePos - 2] = int(toConv[savePos - 2]) + 1
                        toConv[savePos] = 0
                    else:
                        toConv[savePos] = int(toConv[savePos]) + 1
                    toConv[savePos + 1] = 0
                else:
                    if float(toConv[savePos + 2]) >= 5:
                        toConv[savePos + 1] = int(toConv[savePos + 1]) + 1
                toConv = toConv[:savePos + 2]
                toConv = ''.join(str(y) for y in toConv)
        return float(toConv)

    def allVars(chSet, maxleng):
        return (''.join(candidate)
            for candidate in chain.from_iterable(product(chSet, repeat=i)
            for i in range(1, maxleng + 1)))


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
        First: Specify Length (int)"""
        nums = []
        for x in range(leng):
            nums.append(random.randint(0,9))
            if len(nums) == leng:
                convStr = ''.join(str(y) for y in nums)
        return convStr

    def genRandomLetters(leng: int):
        """Generates specified amount of randomly generated letters
        
        Args:
        First: Specify Length (int)"""
        lets = []
        letsBase = list(string.ascii_lowercase)
        for x in range(leng):
            lets.append(letsBase[random.randint(0,25)])
            if len(lets) == leng:
                convStr = ''.join(lets)
        return convStr
    
class percentage:

    def AinB(a, b):
        """Returns how many percents is 'a' from 'b'"""
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
        toLog("Starting password testing")
        for attempt in utils.allVars(syms, 10):
            if attempt == toTest:
                toLog(f"Cracked in {time.time() - start} seconds or {(time.time() - start)//60} minutes.")
                return False, f"Cracked in {time.time() - start} seconds or {(time.time() - start)//60} minutes"
            if abs((time.time() - start) - timeInMinutes * 60) <= 0.1:
                toLog("That takes longer than specified, password check completed. Password wasn't cracked")
                return True, f"That takes longer than specified, password check completed. Password wasn't cracked"
