import random
import base64
import string

class passwordGen:
    def genInBase64(leng: int):
        """Generates specified amount of randomly generated symbols (Numbers and letters)"""
        toConv = []
        for x in range(leng):
            toConv.append(random.randint(0,9))
            ConvStr = ''.join(str(y) for y in toConv)
            base64Conv = base64.b64encode(ConvStr.encode('ascii'))
            base64Conv = list(base64Conv.decode('utf-8'))
            if len(base64Conv) > leng:
                for i in range(len(base64Conv) - leng):
                    base64Conv.pop()
            base64Conv = ''.join(base64Conv)

        return base64Conv
    
    def mirror(toMirror: str):
        """Mirrors the input and returns it"""
        a = list(toMirror)
        out = []
        for x in range(len(a)):
            out.append(a[(len(toMirror) - 1)-x])
        return ''.join(out)
    
    def genRandomNums(leng: int):
        """Generates specified amount of randomly generated numbers"""
        nums = []
        for x in range(leng):
            nums.append(random.randint(0,9))
            convStr = ''.join(str(y) for y in nums)
        return convStr

    def genRandomLetters(leng: int):
        """Generates specified amount of randomly generated letters"""
        lets = []
        letsBase = list(string.ascii_lowercase)
        for x in range(leng):
            lets.append(letsBase[random.randint(0,25)])
            convStr = ''.join(lets)
        return convStr