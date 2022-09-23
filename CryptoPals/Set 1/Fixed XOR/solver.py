from pwn import xor

p1="1c0111001f010100061a024b53535009181c"
p2="686974207468652062756c6c277320657965"

print(xor(bytes.fromhex(p1),bytes.fromhex(p2)).hex())