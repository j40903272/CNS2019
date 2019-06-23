
# coding: utf-8

# In[1]:


import sys
sys.executable, sys.version


# In[2]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *


# In[3]:


from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

def encrypt(msg, iv, key):
    msg = pad(msg, 16)
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    ciphertext = aes.encrypt(msg)
    return b64encode(ciphertext)

def decrypt(msg, iv, key):
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    msg = b64decode(msg)
    plaintext = aes.decrypt(msg)
    plaintext = unpad(plaintext, 16)
    return bytes(plaintext)


# In[28]:


# Initial Authentication

con = remote("140.112.31.97", 10158)
text = con.recv()
print text
IV_AB = b64decode(text.split(":")[1].strip())
print con.recv()

# select initial authentication
con.send("1\n")
print con.recv()
print con.recv()

# send user and nonce
Na = "A"*32
print(Na)
A2B = "A||" + b64encode(Na) + "\n"
con.send(A2B)
text = con.recv()
print text
B, Nb, ANaTb_Kbs = text.split(":")[1].strip().split("||")


text = con.recv()
print text
Nb = text.split('\n')[0].split(":")[1].strip()
AKabTb_Kbs = text.split('\n')[1].split(":")[1].strip()
BNaKabTn_Kas = text.split('\n')[2].split(":")[1].strip()


Nb_Na = encrypt(b64decode(Nb), IV_AB, Na)
con.send(Nb_Na+"||"+ANaTb_Kbs+"\n")
text = con.recv()
print text

flag = eval(text.split(":")[1].strip())
print(decrypt(flag, IV_AB, Na))


# In[39]:


# Subsequent Authentication

con = remote("140.112.31.97", 10158)
text = con.recv()
print text
IV_AB = text.split(":")[1].strip()
print con.recv()


con.send("2\n")
print con.recv()
print con.recv()

A2B = "A||" + AKabTb_Kbs + "\n"
con.send(A2B)
text = con.recv()
print text

Nb = text.split(':')[1].strip()

text = con.recv()
print text




con2 = remote("140.112.31.97", 10158)
text = con2.recv()
print text
IV_AB = text.split(":")[1].strip()
print con2.recv()

con2.send("2\n")
print con2.recv()
print con2.recv()

A2B = Nb + "||" + AKabTb_Kbs + "\n"
con2.send(A2B)
text = con2.recv()
print text
text = con2.recv()
print text
Nb_Kab = text.split(":")[1].strip()

con.send(Nb_Kab + "\n")
print con.recv()
print con.recv()

