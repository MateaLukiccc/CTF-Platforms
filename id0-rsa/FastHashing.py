from ast import Index
from hashlib import sha256


f=open(r"C:\Users\lukic\Desktop\CTF-Platforms\id0-rsa\rockyou.txt", encoding="latin1")

lines=f.readlines()

min=int(sha256(lines[0].strip().encode()).hexdigest(),16)
max=int(sha256(lines[0].strip().encode()).hexdigest(),16)

for i,line in enumerate(lines):
    hashed=int(sha256(line.strip().encode()).hexdigest(),16)
    if hashed >= max:
        max=hashed
        indexMAX=i
    if hashed <= min:
        min=hashed
        indexMIN=i
        
print(lines[indexMAX],lines[indexMIN])




