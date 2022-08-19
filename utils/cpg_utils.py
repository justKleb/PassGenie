from genericpath import isfile
import random
import base64
import string
from ctypes import windll, wintypes, byref
import numpy as np
import os

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

class fileUtils:
    def savePassword(toSave, saveName: str):
        """Saves password into '.pass' file."""
        if os.path.exists('passwords/' + saveName + '.pass'):
            print("Password name is used! Use update function instead!")
            return "Password name is used!"
        else:
            f = open('passwords/' + saveName + '.pass', 'w')
            f.write(str(toSave))
            f.close()

    def updatePassword(toSave, saveName):
        """Updates saved password file with new one"""
        if not os.path.exists('passwords/' + saveName + '.pass'):
            print("File doesn't exist! Use save function instead!")
            return "File doesn't exist!"
        else:
            f = open('passwords/' + saveName + '.pass', 'w')
            f.write(str(toSave))
            f.close()

    def deletePassword(delName):
        """Deletes saved password file"""
        if not os.path.exists('passwords/' + delName + '.pass'):
            print("File doesn't exist! Password should exist lol")
            return "File doesn't exist!"
        else:
            os.remove('passwords/' + delName + '.pass')

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

    def encryptPasswords():
        for b in os.listdir('passwords'):
            f = open('passwords/'+b, 'r')
            passx = f.read()
            print(passx)
            passxENC = base64.b16encode(passx.encode('utf-8'))
            passxENC = base64.b64encode(passxENC)
            print(passxENC)
        f.close()
    
    def decryptPasswords():
        for b in os.listdir('passwords'):
            f = open('passwords/'+b, 'rb')
            passx = f.read()
            print(passx)
            passxDEC = base64.b64decode(passx.decode('utf-8'))
            passxDEC = base64.b16decode('0'+passxDEC.decode('utf-8'))
            print(passxDEC)
        f.close()

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