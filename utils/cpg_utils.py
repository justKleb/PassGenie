import random
import base64

class passwordCrypt:
    def inBase64(leng: int):
        #x = 0
        #print(leng)
        toConv = []
        for x in range(leng):
            #x += 1
            #print(x)
            toConv.append(random.randint(0,9))
            #print(toConv)
            ConvStr = ''.join(str(y) for y in toConv)
            #print(ConvStr)
            base64Conv = base64.b64encode(ConvStr.encode('ascii'))
            base64Conv = list(base64Conv.decode('utf-8'))
            if len(base64Conv) > leng:
                for i in range(len(base64Conv) - leng):
                    base64Conv.pop()
            base64Conv = ''.join(base64Conv)

        return base64Conv#.decode('utf-8')
    
    def mirrored(toMirror: str):
        a = list(toMirror)
        out = []
        for x in range(len(a)):
            out.append(a[(len(toMirror) - 1)-x])
        return ''.join(out)