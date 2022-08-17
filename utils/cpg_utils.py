import random
import base64
import string
from ctypes import windll, wintypes, byref
from time import sleep

class utils:

    def getCursorPosX():
        cursor = wintypes.POINT()
        windll.user32.GetCursorPos(byref(cursor))
        return cursor.x
    
    def getCursorPosY():
        cursor = wintypes.POINT()
        windll.user32.GetCursorPos(byref(cursor))
        return cursor.y

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
        toConv = str(base64.encode(toConv))
        return toConv

class mathFuncs:

    def percentage():
        pass #TODO: Add it.
