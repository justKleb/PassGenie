import os
import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
from utils.cpg_utils import fileUtils as fut
from utils.cpg_utils import percentage as percent
from utils.cpg_utils import crypting as crypt

fut.clearLog()
crypt.keyGen()

#crypt.updKey()

start = time.time()
#gen = pG.genRandomLetters(1000)
print(crypt.encrypt("Ass-ass-in"))
print("Run took %s seconds" % (time.time() - start))
