"we need to invert encryption operation ct=((123 * char + 18) % 256) which is easy x=(ct-18)*inv(123) mod 256"

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct="6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"

c=bytes.fromhex(ct)

#123*x+18 = ct mod 256  => 123*x= ct-18 mod 256  => x=(ct-18)*inv(123) mod 256

from Crypto.Util.number import inverse

def decryption(msg):
    pt=[]
    for char in msg:
        pt.append((char-18)*inverse(123,256) % 256)
    return bytes(pt)

pt=decryption(c)
print(pt)