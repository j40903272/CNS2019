chal.py
HAHAHAHAHAHAHAHHAHAHAHAAHA_the_first_flag_name_is_too_long_too_bad_you_cant_read_it_HAHAHAHAHAHAHAHAHAHAHAHAHA.py
b0nU5_FL4g_Y0U_F0unD_m3
run.sh

#!/usr/bin/env python2

import os
import sys
import shutil
import atexit
import signal
import base64
import hashlib
from subprocess32 import Popen, PIPE, TimeoutExpired

from HAHAHAHAHAHAHAHHAHAHAHAAHA_the_first_flag_name_is_too_long_too_bad_you_cant_read_it_HAHAHAHAHAHAHAHAHAHAHAHAHA import FLAG

def md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()

def intro():
    print '========================================='
    print '        Give me two python2 codes        '
    print '========================================='
    print '   1. One will output "MD5 is secure!"   '
    print '   2. One will output "Just kidding!"    '
    print '   3. MD5(code1) == MD5(code2)           '
    print '   4. code1 != code2                     '
    print '   5. len(code1) < 500                   '
    print '   6. len(code2) < 500                   '
    print '========================================='

def save_code(code1, code2, foldername):
    md5hash = md5(code1)
    filename1 = '{}/code1-{}.py'.format(foldername, md5hash)
    f = open(filename1, 'w')
    f.write(code1)
    f.close()

    md5hash = md5(code2)
    filename2 = '{}/code2-{}.py'.format(foldername, md5hash)
    f = open(filename2, 'w')
    f.write(code2)
    f.close()

    return filename1, filename2

def execute_code(filename):
    with Popen(['python2', filename], stdout=PIPE, preexec_fn=os.setsid) as process:
        try:
            output = process.communicate(timeout=1)[0].strip()
        except TimeoutExpired:
            os.killpg(process.pid, signal.SIGINT)
            print 'Failed to execute your code'
            exit(0)

    return output

def check_code_behavior(output1, output2):
    ans1 = 'MD5 is secure!'
    ans2 = 'Just kidding!'

    if (ans1 == output1 and ans2 == output2) or (ans1 == output2 and ans2 == output1):
        return True

    return False

def blacklist(code):
    bl = ['tcp', 'udp', 'socket', 'Socket', 'exec', 'Popen', 'popen', 'eval', 'sh', 'nc', 'ncat', 'bash', 'socat']

    for b in bl:
        if b in code:
            return True

    return False

def check_same_md5(code1, code2):
    if md5(code1) == md5(code2):
        return True

    print 'MD5(code1) != MD5(code2)'
    return False

def check_input(code):
    if len(code) > 0 and len(code) < 500:
        return True

    print 'Your code should be less than 500 bytes and not empty'
    return False

def get_input():
    code1 = raw_input('Input first base64-encoded python2 code: ').strip()
    print ''
    code2 = raw_input('Input second base64-encoded python2 code: ').strip()
    print ''

    return base64.b64decode(code1), base64.b64decode(code2)

def removeCreatedDir(foldername):
    shutil.rmtree(foldername, ignore_errors=True)

def init():
    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    foldername = '/tmp/{}'.format(os.urandom(16).encode('hex'))
    if os.path.exists(foldername):
        shutil.rmtree(foldername, ignore_errors=True)
    os.mkdir(foldername)

    atexit.register(removeCreatedDir, foldername)

    return foldername

def main():
    foldername = init()

    intro()
    code1, code2 = get_input()
    if not check_input(code1) or not check_input(code2):
        exit(0)
    if code1 == code2:
        print 'code1 == code2'
        exit(0)
    if not check_same_md5(code1, code2):
        exit(0)
    if blacklist(code1) or blacklist(code2):
        print 'HACKER!'
        exit(0)
    filename1, filename2 = save_code(code1, code2, foldername)
    print 'Executing your code......'
    output1 = execute_code(filename1)
    output2 = execute_code(filename2)
    print output1
    print output2

    if not check_code_behavior(output1, output2):
        print 'Failed!'
        exit(0)

    print 'Good job!'
    print FLAG

if __name__ == '__main__':
    main()
