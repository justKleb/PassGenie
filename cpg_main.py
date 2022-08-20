import os
import time
from utils.cpg_utils import passwordGen as pG
from utils.cpg_utils import utils as ut
from utils.cpg_utils import fileUtils as fut
from utils.cpg_utils import percentage as percent
from utils.cpg_utils import crypting as crypt

#f = open('passwords/01011-00101-11001', 'w')
#key = fnet.Fernet.generate_key()
#f.write(str(key))
#f.close()

start = time.time()
#neg = pG.genInBase64(10000)
#neg = pG.mirror(neg)
#print(neg)
gen = pG.genRandomLetters(1000)
print(os.listdir('passwords'))
fut.savePassword("vzlomZhopi123456", 'Lambda')
print("Run took %s seconds" % (time.time() - start))
