from pwn import xor

################################################################################################################################
leaked="414396a5358b65be17abb54d256816821402083349dbeed5e96a2fd2f807c76165a5a991a9324c899db9eedf90040199"
msg = 'logged_username=' + 'admin' +'&password=' + 'g0ld3n_b0y'
our = 'logged_username=' + 'admir' +'&password=' + 'g0ld3n_b0y'

text=b'r'  #taking only the initial block... since that's only required
forge_text=b'n'  #we put the block we want to replace old one admin=>admir
print(xor(text,forge_text).hex())

#logged_username=admi r

b1=bytes.fromhex(leaked[:32])
b2=bytes.fromhex(leaked[32:64]) #admir....
b3=bytes.fromhex(leaked[64:96])


b1_new=b1[:4]+xor(b1[4],xor(text,forge_text))+b1[5:]
print((bytes(b1_new)+b2+b3).hex())



###############################################################################################################################################################
msg = 'logged_username=' + 'admin' +'&password=' + 'g0ld3n_b0y'
leaked="414396a5358b65be17abb54d25681682cd55b4eb58b9fa90e5fe7dab460239e689e2a1defaf6079e2a4e5f906fb98b4a"

our = 'logged_username=' + 'bdmin' +'&password=' + 'g0ld3n_b0y'
b1=bytes.fromhex(leaked[:32])
b2=bytes.fromhex(leaked[32:64])
b3=bytes.fromhex(leaked[64:96])

b1_new = []
flipped_byte = (b1[0] ^ ord('a') ^ ord('b')).to_bytes(1,"big")
b1_new = flipped_byte + b1[1:]
print((bytes(b1_new)+b2+b3).hex())


##############################################################################################################
msg = 'logged_username=' + 'admin' +'&password=' + 'g0ld3n_b0y'


xor = ord('r') ^ ord('s')
cipher="553a55dedfbd8734772a13c14de110846bd5bc2b21289f5485e642c43f4e47183fe687a2dd67d4f334a20f89e7754b7d312a2b5f39a6af8e471896d1753da926"
print(len(cipher))
cipher = cipher[:16] + hex(int(cipher[16:18], 16) ^ xor)[2:] + cipher[18:]
print(cipher)

#name=admin&parsword=g0ld3n_b0y
#pass=g0ld3n_b0y'


#HTB{b1t_fl1pp1ng_1s_c00l} 
