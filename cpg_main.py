import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import crypting as crypt
from utils.cpg_utils import percentage as percent

start = time.time()
#neg = pG.genInBase64(10000)
#neg = pG.mirror(neg)
#print(neg)
print(crypt.toDouble(percent.fromPercent(10, 19)))
print(crypt.toDouble(3234.294))
print("took %s seconds" % (time.time() - start))
