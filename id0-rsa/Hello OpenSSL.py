from Crypto.PublicKey import RSA
from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes


f = open('new.pem','r')
key = RSA.importKey(f.read())

print(key.n,key.e)

f=FactorDB(key.n)
f.connect()
p=f.get_factor_list()[0]
q=f.get_factor_list()[1]

phi=(p-1)*(q-1)

d=pow(key.e,-1,phi)

c=int("6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42",16)

print(hex(pow(c,d,key.n)))
