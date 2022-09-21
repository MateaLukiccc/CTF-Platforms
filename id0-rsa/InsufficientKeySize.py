from Crypto.PublicKey import RSA

f = open(r'C:\Users\lukic\Desktop\CTF-Platforms\id0-rsa\keySize.pem','r')
key = RSA.importKey(f.read())

n=key.n
e=key.e

from factordb.factordb import FactorDB

f=FactorDB(n)
f.connect()
p=min(f.get_factor_list())
q=n//p

d=pow(e,-1,(p-1)*(q-1))

print(hex(d))