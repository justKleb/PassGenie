import random
import base64

class passwordCrypt:
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