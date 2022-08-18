import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
from utils.cpg_utils import percentage as percent

start = time.time()
#neg = pG.genInBase64(10000)
#neg = pG.mirror(neg)
#print(neg)
print(ut.toDouble(10.2115424))
print("took %s seconds" % (time.time() - start))
