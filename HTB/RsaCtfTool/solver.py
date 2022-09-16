from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse,long_to_bytes

f = open(r'C:\Users\lukic\Desktop\HTB\RsaCtfTool\pubkey.pem','r')
key = RSA.importKey(f.read())


p1=10410080216253956216713537817182443360779235033823514652866757961082890116671874771565125457104853470727423173827404139905383330210096904014560996952285911
p2=p1
p3=p1

phi=p1**3-p1**2

d=inverse(key.e,phi)


c="13822f9028b100e2b345a1ad989d9cdedbacc3c706c9454ec7d63abb15b58bef8ba545bb0a3b883f91bf12ca12437eb42e26eff38d0bf4f31cf1ca21c080f11877a7bb5fa8ea97170c932226eab4812c821d082030100030d84ebc63fd8767cde994e0bd1a1f905c27fb0d7adb55e3a1f101d8b5b997ba6b1c09a5e1cc65a9206906ef5e01f13d7beeebdf389610fb54676f76ec0afc51a304403d44bb3c739fd8276f0895c3587a710d15e43fc67284070519e6e0810caf86b134f02ec54018"

aesKey=long_to_bytes(pow(int(c,16),d,key.n))


print(len(aesKey))
print(aesKey)

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
  

    cipher = AES.new(aesKey, AES.MODE_ECB)
    plaintext = cipher.decrypt(pad(ciphertext,16))

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext

g=open(r"C:\Users\lukic\Desktop\HTB\RsaCtfTool\flag.txt.aes",'rb')

print(decrypt_flag(aesKey,0,g.readline()))
