from pwn import xor

p="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
k="ICE"

print(xor(p.encode(),k.encode()).hex())