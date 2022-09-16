from Crypto.PublicKey import RSA

f = open(r'C:\Users\lukic\Desktop\Ringzero\Public key recovery\key.pem','r')
key = RSA.importKey(f.read())

print(key.d)

#priv key n,e

print(key.n,key.e)
n=key.n
e=key.e
d=key.d

from Crypto.PublicKey import RSA


privateKey = RSA.construct((n, e, d))
privateKeyPem = privateKey.exportKey(pkcs=8) # export in PKCS#8 format

publicKey = RSA.construct((n, e))
publicKeyPem = publicKey.exportKey() # export in X.509/SPKI format

print(privateKeyPem.decode('utf8'))
print(publicKeyPem.decode('utf8'))

s="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDwkrxVrZ+KCl1cX27SHDI7EfgnFJZ0qTHUD6uEeSoZsiVkcu0/XOPbz1RtpK7xxpKMSnH6uDc5On1IEw3A127wW4Y3Lqqwcuhgypd3Sf/bH3z4tC25eqr5gA1sCwSaEw+yBxdnElBNOXxOQsST7aZGDyIUtmpouI1IXqxjrDx2SQIDAQAB"

import hashlib

print(hashlib.md5(s.encode()).hexdigest())