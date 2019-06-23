import time
import random
import base64
import sys

base64_str = sys.argv[1]
encrypted = base64.b64decode(bytes(base64_str, 'ascii'))

for i in range(-100, 100):
    T = int(time.time())+i
    random.seed(T)
    decrypted = [i ^ random.randint(0, 255) for i in encrypted]
    flag = "".join([chr(i) for i in decrypted])
    if "BALSN" in flag:
        print(flag)