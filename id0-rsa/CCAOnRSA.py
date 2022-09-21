c=int("912fcd40a901aa4b7b60ec37ce6231bb87783b0bf36f824e51fe77e9580ce1adb5cf894410ff87684969795525a63e069ee962182f3ff876904193e5eb2f34b20cfa37ec7ae0e9391bec3e5aa657246bd80276c373798885e5a986649d27b9e04f1adf8e6218f3c805c341cb38092ab771677221f40b72b19c75ad312b6b95eafe2b2a30efe49eb0a5b19a75d0b31849535b717c41748a6edd921142cfa7efe692c9a776bb4ece811afbd5a1bbd82251b76e76088d91ed78bf328c6b608bbfd8cf1bdf388d4dfa4d4e034a54677a16e16521f7d0213a3500e91d6ad4ac294c7a01995e1128a5ac68bfc26304e13c60a6622c1bb6b54b57c8dcfa7651b81576fc",16)


from Crypto.PublicKey import RSA

f = open(r'C:\Users\lukic\Desktop\CTF-Platforms\id0-rsa\new2.pem','r')
key = RSA.importKey(f.read())

n=key.n
e=key.e

print(n)
print(e)
print(c)
from pwn import *
import requests

C1=hex(n+c)

#we send c1 as (c+n)^d mod n == c^d mod n 

URL_encrypt='https://id0-rsa.pub/problem/rsa_oracle/13ad92dcdf4d3693a5f2efd899a8f4c2e3fef1a6fd80ef2f91ad95cee4d9e5e58ad6ee35abf5992f80c4ed30b6c35f2a2037664ae9de2287a824a6b3ca16045df93a8bd4a7f63d118f7c22767ad2c8fc3ea39525e0f4eacb51474091a60210c689fc89e0719ea77aab7b17cf9c1fb6feb0fef768934ac4301e66b23d4a6363f300a7cf1ade59a59368b23d4387108a734f54c5782bc4844352d9a8cae059262d21d90337718990725e2d4a9ae6e697b9c3a907574960a6ea324cd0fc557f325a624b2f4cf796e147db19284198a8274f52c7794d7437f1f71c8a25e50543c65cb7895c0d8810924a0ff1cb598917bb4e9888a149e05aa7f68c25ae3887506bef5'


r = requests.get(URL_encrypt)
print(r.text)