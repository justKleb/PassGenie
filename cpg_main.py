import os
import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
from utils.cpg_utils import fileUtils as fut
from utils.cpg_utils import percentage as percent
from utils.cpg_utils import crypting as crypt
from utils.cpg_utils import log
from cryptography.fernet import Fernet as fnet

start = time.time()

log.clearLog()
crypt.keyGen()



print("Run took %s seconds" % (time.time() - start))
