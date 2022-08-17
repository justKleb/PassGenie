#import utils.cpg_utils as cpgu
import time

from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
start = time.time()
neg = pG.genInBase64(1)
print(neg)
print("took %s seconds" % (time.time() - start))
