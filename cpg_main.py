#import utils.cpg_utils as cpgu
from utils.cpg_utils import passwordCrypt as cpgu
neg = cpgu.genInBase64(19)
print(neg)
#print(len(cpgu.inBase64(19)))
print(cpgu.mirror(neg))