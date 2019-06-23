
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *
import hashpumpy
import base64


# In[2]:


hidden_token = "{0.__ne__.__doc__[18]}"
hidden_token += "{0.__init__.__doc__[29]}"
hidden_token += "{0.ljust.__doc__[91]}"
hidden_token += "{0.__mod__.__doc__[19]}"
hidden_token += "{0.format.__doc__[9]}"
#len(hidden_token), hidden_token.format('')


# In[3]:


def exploit(balsn, L=random.randint(40, 50)):
    global hidden_token
    a = hashpumpy.hashpump(balsn, "10", "&BALSN_Coin=2147483648&hidden_flag="+hidden_token, 16+L)
    return base64.b64encode(a[1]), a[0]


# In[4]:


con = remote("140.112.31.96", 10154)
text = con.recv()
print text
text = con.recv()
print text

con.send('2\n')
text = con.recv()
print text
text = con.recv()
print text

con.send('10\n')
text = con.recv()
print text
text = con.recv()
print text

token = text.split('\n')[2][7:]
print token


# In[5]:


for i in range(40, 50):
    a, b = exploit(token, i)
    con.send('3\n')
    print con.recv()
    print con.recv()
    con.send(a+'\n')
    print con.recv()
    print con.recv()
    con.send(b+'\n')
    text = con.recv()
    print text
    print con.recv()
    if 'Valid' in text:
        break

