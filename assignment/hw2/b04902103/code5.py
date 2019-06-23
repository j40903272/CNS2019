
# coding: utf-8

# In[ ]:


### certificate
'''
-----BEGIN CERTIFICATE-----
MIIDFDCCAfygAwIBAgIUZyUb0qt/VqFMGlyguyqqBPmhjA4wDQYJKoZIhvcNAQEL
BQAwRDELMAkGA1UEBhMCVFcxDTALBgNVBAcMBFIzMDcxDjAMBgNVBAoMBUJBTFNO
MRYwFAYDVQQDDA13d3cuYmFsc24uY29tMB4XDTE5MDUwNjExMDgzM1oXDTIwMDUw
NTExMDgzM1owRDELMAkGA1UEBhMCVFcxDTALBgNVBAcMBFIzMDcxDjAMBgNVBAoM
BUJBTFNOMRYwFAYDVQQDDA13d3cuYmFsc24uY29tMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAmu3lq6qBMWyl0IsbMaa4mVYuExndn+GL7fImnFBYFnAD
NvXS3jxF3dB9QcsWVA8AXMs00d9Umqwwqo9Nly8JRg7xE9QzwoG+JiQAh7LuwWpJ
GnQEjNke+hWENduM3/jdN6e45yOsE/iFHqtLloQdhOpyBH5e7FWbulDkT0IlDo78
Xbv2hiJIEB0KhoifLGfz4fcpNXFQgXusIU+yWgt6NreH/zTlHWTBpX4AcoiGBpRC
tTunzqSp/cJMBbUHdkc1VqDNWP+SC4Kw6ejQ3oBwraiHN9rJI3q+4wvfbhMoE88y
P1bkEIrXN6MRiDuNfukGc3E6rTooYy7Z0CokKOrg/QIDAQABMA0GCSqGSIb3DQEB
CwUAA4IBAQAZSU58Wy9DmXWCLgLVlBvAzuKevE0g5Db3s96jDSFEIyXvHozMA24W
w/V7/mZT8c0vC3QBJXcbLqrF8pkS8wc/CHUwl2PPfmsbkCr+nqEVsz7bC+68Hr0Y
UhTg40DULRW4aIc3q/voglqKkun6SOmxb03IK6J5lrLoKKINm1bO+GsbsOGkpSXf
rOfpRXzTFtypgPsaSnXhnkjQ/N985senG67donbZrwLzYP9JRPaWB9Wo/En5a0um
OO4uxTwkJT4ULscMYsjFkclki83nC+B+2xy6eLYGpRyPnLXIXnj1DgXBCPOmJCwd
AN/sriW/GFDuda7iYjm/yfWHujHUUCnZ
-----END CERTIFICATE-----
'''
# extract public key (N, e) with https://8gwifi.org/PemParserFunctions.jsp


# In[13]:


def isqrt(n):
    x=n
    y=(x+n//x)//2
    while(y<x):
        x=y
        y=(x+n//x)//2
    return x

def fermat(n):
    t0=isqrt(n)+1
    counter=0
    t=t0+counter
    temp=isqrt((t*t)-n)
    while((temp*temp)!=((t*t)-n)):
        counter+=1
        t=t0+counter
        temp=isqrt((t*t)-n)
    s=temp
    p=t-s
    q=t+s
    return p,q


# In[15]:


N = 19558010422024221505610640393261429501039329302569018548599729011172241983514506526982755091054220574677910256793100755845920047651650839282213398640429572226212335678345480440342993743254195043032638380155563244584013147781153198792269937719985292147125976666034188430931507496465409365910574400115825676486295663819647078236039378282412941384246231274483183160716753419359053536998036988996660973170695455583447207727521389174006503006466729910734558349343780263872231532049523821639654661438891569514109682058427025285110834558256671527333916708139328850387187588551181178493326389582702512746958593223182114283773
e = 65537

public_key = (N, e)
p,q=fermat(N)
print("p:",int(p))
print("q:",int(q))


print N == p * q
r = (p-1)*(q-1)


# In[16]:


def xgcd(a, b):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

_, d, _ = xgcd(e, r)
print(d)


# In[17]:


(d*e)%r


# In[18]:


from Crypto.PublicKey import RSA
rsa = RSA.construct((N, long(e), d, p, q, long(0)))


# In[19]:


print(rsa.exportKey())

