
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('env', 'TERMINFO=/usr/share/terminfo')
#get_ipython().run_line_magic('env', 'PWNLIB_NOTERM=true')
from pwn import *


# In[2]:


N_list = list()
c_list = list()

for i in range(3):
    con = remote("140.112.31.96", 10155)
    text = con.recv()
    e, N, c, _ = [i[4:] for i in text.split('\n')]
    N_list.append(N)
    c_list.append(c)



EXPONENT = 3


def chinese_remainder_theorem(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m

    # Make sure we return the canonical solution.
    return result % N


def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return (lastx, lasty, a)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def get_value(filename):
    return open(filename).readline()
    

C1, C2, C3 = [int(i) for i in c_list]
ciphertexts = [C1, C2, C3]

N1, N2, N3 = [int(i) for i in N_list]
modulus = [N1, N2, N3]

C = chinese_remainder_theorem([(C1, N1), (C2, N2), (C3, N3)])
print(C)


# In[5]:


import gmpy2
gmpy2.get_context().precision = 4096

from binascii import unhexlify
from gmpy2 import root


M = int(root(C, 3))
M = hex(M)[2:]
print(unhexlify(M).decode('utf-8'))




