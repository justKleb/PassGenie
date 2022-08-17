import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut

start = time.time()
#neg = pG.genInBase64(10000)
#neg = pG.mirror(neg)
#print(neg)
print(pG.genViaMouse(12))
print("took %s seconds" % (time.time() - start))
