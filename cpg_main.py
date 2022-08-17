#import utils.cpg_utils as cpgu
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
neg = pG.genInBase64(19)
#x, y = pG.genViaMouse()
print(neg)
#print(len(cpgu.inBase64(19)))
print(pG.mirror(neg))
print(pG.genRandomLetters(10))
print(pG.genRandomNums(10))
print(pG.genViaMouse(10))