'''
Hash the string id0-rsa.pub with sha256, then hash the hex string output with md5, and submit the lowercase hex result.
'''
import hashlib

s="id0-rsa.pub"

s=hashlib.sha256(s.encode()).hexdigest()
s=hashlib.md5(s.encode()).hexdigest()

print(s)


