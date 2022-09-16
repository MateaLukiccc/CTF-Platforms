#!/usr/bin/python3
from Crypto.Util.number import getPrime, long_to_bytes, inverse
from gmpy2 import iroot
#flag = open('flag.txt', 'r').read().strip().encode()
flag=bytes.fromhex("05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965")

class RSA:
    def __init__(self):
        self.p = getPrime(512)
        self.q = getPrime(512)
        self.e = 3
        self.n = self.p * self.q
        self.d = inverse(self.e, (self.p-1)*(self.q-1))
    def encrypt(self, data: bytes) -> bytes:
        pt = int(data.hex(), 16)
        ct = pow(pt, self.e, self.n)
        print(self.n)
        return long_to_bytes(ct)
    def decrypt(self, data: bytes) -> bytes:
        ct = int(data.hex(), 16)
        pt = pow(ct, self.d, self.n)
        return pt

def main():
    crypto = RSA()
    #print ('Flag:', crypto.encrypt(flag))
    p=iroot(crypto.decrypt(flag),3)[0]                 #since n> m^e then => m^3 mod n=m^e so we just take 3rd root
    print(p)
    #p=9208566198168854769137135900129825812636831889153009607082441577495048346488797274341323901
    print(long_to_bytes(p))

if __name__ == '__main__':
    main()
