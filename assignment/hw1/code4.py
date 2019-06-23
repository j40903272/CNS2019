
# coding: utf-8

# In[1]:


#import sys
#sys.executable, sys.version


# In[2]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *


# In[3]:


words = []
for line in open('/usr/share/dict/words'):
    words.append(line.lower().strip())
words = set(words)
print len(words)


# In[4]:


def upper(s1, s2):
    out = ""
    for i in range(len(s1)):
        if s1[i].isupper():
            out += s2[i].upper()
        else:
            out += s2[i]
    return out


# In[5]:


def caesar_cipher(c1):
    print "\n######## start crack ########"
    print c1
    org = c1

    c1 = c1.lower()
    for i in xrange(ord('a') - ord(c1[0]), ord('z') - ord(c1[0])):
        #print i
        data = []
        for j in c1:
            if not j.isalpha():
                data.append(j)
            else:
                tmp = ord(j)+i
                if tmp < ord('a'):
                    tmp += 26
                elif tmp > ord('z'):
                    tmp -= 26
                data.append(chr(tmp))
            
        data = "".join(data)
        #print data
        cnt = 0
        for token in data.split():
            if token.translate(None, string.punctuation) in words:
                cnt += 2
            if cnt > len(data.split())*0.7:
                data = upper(org, data)
                print data
                return data


# In[6]:


con = remote("140.112.31.96", 10151)
print con.recv()
con.send("2\n")
text = con.recv()
print text
con.send(text.split('\n')[4][11:]+'\n')
text = con.recv()
print text
token = text.split('\n')
c1 = token[4][9:]
con.send(caesar_cipher(c1)+'\n')
text = con.recv()
print text
token = text.split('\n')
c1 = token[5][9:]
m1 = token[6][9:]
c2 = token[7][9:]


# In[7]:


pattern = [0]*7
cnt = 0

for i, j in zip(c1, m1):
    #print i, j, (ord(i)-ord(j)), (ord(i)-ord(j))%26
    #a.add((ord(i)-ord(j))%26)
    
    if pattern[cnt%7] == 0:
        pattern[cnt%7] = (ord(i)-ord(j))%26
    
    cnt += 1
    if 0 not in pattern:
        break
        
print pattern

for cnt in range(len(pattern)):
    tmp = ""
    idx = cnt
    for i in c1.lower():
        if not i.isalpha():
            tmp += i
            cnt += 1
            continue
        
        c = ord(i) - pattern[cnt%len(pattern)]
        while c>ord('z'):
            c -= 26
        while c<ord('a'):
            c += 26
        
        tmp += chr(c)
        cnt += 1
        
    if tmp == m1.lower():
        print idx, tmp
        break


# In[8]:


cnt = idx
tmp = ""
for i in c2.lower():
    if not i.isalpha():
        tmp += i
        cnt += 1
        continue

    c = ord(i) - pattern[cnt%len(pattern)]
    while c>ord('z'):
        c -= 26
    while c<ord('a'):
        c += 26

    tmp += chr(c)
    cnt += 1

print tmp
print c2

con.send(upper(c2, tmp) + "\n")
text = con.recv()
print text
token = text.split('\n')
c1 = token[6][9:]
m1 = token[7][9:]
c2 = token[8][9:]


# In[9]:


def Rail_fence_solver(S):
    global words
    def Rail_fence_decrypt(s,n):
        fence = [[] for i in range(n)]
        rail  = 0
        var   = 1

        for char in s:
            fence[rail].append(char)
            rail += var

            if rail == n-1 or rail == 0:
                var = -var

        rFence = [[] for i in range(n)]

        i = 0
        l = len(s)
        s = list(s)
        for r in fence:
            for j in range(len(r)):
                rFence[i].append(s[0])
                s.remove(s[0])
            i += 1

        rail = 0
        var  = 1
        r = ''
        for i in range(l):
            r += rFence[rail][0]
            rFence[rail].remove(rFence[rail][0])
            rail += var

            if rail == n-1 or rail == 0:
                var = -var

        return r
    
    for i in range(2, 15):
        tmp = Rail_fence_decrypt(S, i)
        cnt = 0
        for j in tmp.lower().split():
            if j in words:
                cnt += 1
        if cnt >= len(tmp.split())-1:
            return tmp


# In[10]:


x = Rail_fence_solver(c2)
print x
con.send(x+'\n')
text = con.recv()
print text


# In[12]:


import base64
m = base64.b64decode(text.split('\n')[4][9:])
print m
con.send(m+'\n')
text = con.recv()
print text

