
ct1="f5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da"


from Crypto.PublicKey import RSA

f = open(r'C:\Users\lukic\Desktop\CTF-Platforms\id0-rsa\Ps and Qs\key1.pem','r')
key = RSA.importKey(f.read())

n1=key.n
e=key.e

f = open(r'C:\Users\lukic\Desktop\CTF-Platforms\id0-rsa\Ps and Qs\key2.pem','r')
key = RSA.importKey(f.read())

n2=key.n


from math import gcd
from Crypto.Util.number import long_to_bytes
p=gcd(n1,n2)
q=n1//p

phi=(p-1)*(q-1)

d=pow(e,-1,phi)

print(hex(pow(int(ct1,16),d,n1)))

