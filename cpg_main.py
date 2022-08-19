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
time.sleep(0.5)
fut.updatePassword(pG.genInBase64(12) + 'NegaBols' + pG.genRandomNums(10), "Lambda")
time.sleep(0.5)
fut.updatePassword("Before encrypting", 'Lambda')
time.sleep(0.5)
crypt.encryptPasswords()
crypt.decryptPasswords()
fut.deletePassword("Lambda")
#fut.updatePassword(pG.genInBase64(12), "Lakaka")
#print(ut.toDouble("10." + gen))
print("Run took %s seconds" % (time.time() - start))
