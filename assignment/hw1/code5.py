
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *
import time
import random
import base64


# In[2]:


def encrypt_func():
    random.seed(int(time.time()))
    flag = secret.FLAG
    encrypted = [ord(i) ^ random.randint(0, 255) for i in flag]
    return str(base64.b64encode(bytes(encrypted)))[2:-1]


# In[3]:


con = remote("140.112.31.96", 10152)
text = con.recv()
print text


# In[4]:


from subprocess import call
call(['python3', 'otp1.py', text.strip()])