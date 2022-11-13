import json
import secrets; srandom = secrets.SystemRandom()
import base64
import string
import time
from datetime import datetime as dt
from itertools import product, chain
from os import mkdir


def to_log(toWrite, _type=0):
    types = ["[INFO]", "[ERR]", "[WARN]", "[CRASH]"]
    chosen_type = types[_type]
    log = open('run/log.log', 'a')
    log.write(f'{dt.now().strftime("[%H:%M:%S]")} {chosen_type} {toWrite}\n')
    log.close()


def clear_log():
    try:
        with open('run/log.log', 'w') as log:
            log.write('')
    except:
        print("Couldn't open the log file")
        raise FileExistsError("Log file not existing")


class utils:

    def to_double(to_conv: float):
        """Converts input into a double with proper round-up"""
        to_return = str(to_conv)
        whereDot = 0
        pos = 0
        for x in to_return:
            pos += 1
            if x == '.':
                save_pos = pos
                to_return = list(to_return)
                if float(to_return[save_pos + 1]) + 1 >= 10:
                    if to_return[save_pos] == '9':
                        to_return[save_pos - 2] = int(to_return[save_pos - 2]) + 1
                        to_return[save_pos] = 0
                    else:
                        to_return[save_pos] = int(to_return[save_pos]) + 1
                    to_return[save_pos + 1] = 0
                else:
                    if float(to_return[save_pos + 2]) >= 5:
                        to_return[save_pos + 1] = int(to_return[save_pos + 1]) + 1
                to_return = to_return[:save_pos + 2]
                to_return = ''.join(str(y) for y in to_return)
        return float(to_return)

    def all_vars(ch_set, max_lenght):
        return (''.join(candidate)
                for candidate in chain.from_iterable(product(ch_set, repeat=i)
                                                     for i in range(1, max_lenght + 1)))


class passwordGen:
    def gen_random_syms(leng: int):
        """Generates specified amount of randomly generated symbols (Numbers and letters)"""
        if type(leng) != int:
            try:
                leng = int(leng)
            except ValueError: return "wrongType"
        to_conv = []
        base64_conv = ""
        for x in range(leng):
            to_conv.append(srandom.randint(0, 9))
            if len(to_conv) == leng:
                conv_str = ''.join(str(y) for y in to_conv)
                base64_conv = base64.b64encode(conv_str.encode('ascii'))
                base64_conv = base64_conv.decode('utf-8')
            if len(base64_conv) > leng:
                for i in range(len(base64_conv) - leng):
                    base64_conv = base64_conv[:-1]

        return base64_conv

    def mirror(to_mirror: str):
        """Mirrors the input and returns it"""
        a = list(to_mirror)
        a.reverse()
        """for x in range(len(a)):
            out.append(a[(len(toMirror) - 1) - x])"""  # Legacy
        return ''.join(a)

    def gen_random_nums(leng: int):
        """Generates specified amount of randomly generated numbers"""
        if type(leng) != int:
            try:
                leng = int(leng)
            except ValueError: return "wrongType"
        nums = []
        for x in range(leng):
            nums.append(srandom.randint(0, 9))
            if len(nums) == leng:
                conv_str = ''.join(str(y) for y in nums)
        return conv_str

    def gen_random_letters(leng: int):
        """Generates specified amount of randomly generated letters"""
        if type(leng) != int:
            try:
                leng = int(leng)
            except ValueError: return "wrongType"
        lets = []
        lets_base = list(string.ascii_lowercase)
        for x in range(leng):
            lets.append(lets_base[srandom.randint(0, 25)])
            if len(lets) == leng:
                convStr = ''.join(lets)
        return convStr

    def gen_random_words(leng: int):
        """Generates specified amount of randomly generated words"""
        if type(leng) != int:
            try:
                leng = int(leng)
            except ValueError:
                return "wrongType"
        with open('./res/words.txt', 'r') as words:
            wlist = words.read().split('\n'); wlist = [i.capitalize() for i in wlist]
        to_return = []
        for i in range(leng):
            to_return.append(wlist[srandom.randint(0, len(wlist))])
        return ''.join(to_return)

class percentage:

    def a_from_b(a, b):
        """Returns how many percents is 'a' from 'b'"""
        return (a / b) * 100

    def percents_of(a, b):
        """Returns 'a' percents from 'b' number"""
        return (b / 100) * a

    def fromPercent(a, b):
        """Returns number from how much percent is number from it"""
        return a * (100 / b)


class passwordUtils:

    def save_pass(to_save: str, pass_name: str):
        try:
            mkdir('./passwords')
            to_log('Passwords dir. isn`t present, created one')
        except FileExistsError:
            to_log('Passwords dir. is already present, canceled creation process')

        with open('./passwords/' + pass_name + '.json') as saving_pass:
            json.dumps({'name': pass_name,
                        'pass': '',
                        'icon': ''})

    def brute(to_test: str, time_in_minutes: float):
        """Simulates real brute-force attack on password, returns True if password did get cracked, False if didn't."""
        syms = str(list(string.ascii_lowercase) +
                   list(string.ascii_uppercase) +
                   list("""1234567890 =-_+/?\|'";:><,.*&7^%$#@!()[]{} """))
        start = time.time()
        to_log("Starting password testing")
        for attempt in utils.all_vars(syms, 10):
            if attempt == to_test:
                to_log(f"Cracked in {time.time() - start} seconds or {(time.time() - start) // 60} minutes.")
                return False, f"Cracked in {time.time() - start} seconds or {(time.time() - start) // 60} minutes"
            if abs((time.time() - start) - time_in_minutes * 60) <= 0.1:
                to_log("That takes longer than specified, password check completed. Password wasn't cracked")
                return True, f"That takes longer than specified, password check completed. Password wasn't cracked"
