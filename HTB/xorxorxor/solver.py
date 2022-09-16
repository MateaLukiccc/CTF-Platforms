import os
flag = bytes.fromhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9")

class XOR:
    def __init__(self):
        self.key = bytes.fromhex("5b1eb49a")       #first step is xor with HTB{.encode()
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored
    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    
    dec=b''
    while True:
        crypto = XOR()
        dec=crypto.encrypt(flag)
        print(dec)   #in first part we print dec.hex()[0:16] so we get first 4 bytes

#from pwn import xor
if __name__ == '__main__':
    main()
