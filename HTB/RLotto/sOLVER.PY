import time
import random
from pwn import *


conn = remote('167.99.202.193', 30683)


shit = conn.recvuntil(b'numbers:')
print(shit)

seed = int(time.time())         #if we put this up a line we will find seed before we establish a connection which we dont want

nums=shit[-100:-86]      #legit just guessing for 5 min
nums=(nums.strip()).split(b" ")
nums2=[]
for i in nums:
    nums2.append(int(i.decode()))
print(nums2)                         #making a list of numbers from bytes


ans = [1, 2, 3, 4, 5]
while ans != nums2:
    ans = []
    random.seed(seed)
    while len(ans) < 5:
        r1 = random.randint(1, 90)
        if(r1 not in ans):
            ans.append(r1)
    print(seed, ans)
    seed -= 1

ans = []
while len(ans) < 5:
    r1 = random.randint(1, 90)
    if(r1 not in ans):
        ans.append(r1)

print(ans)


conn.sendline((str(ans[0])+" "+str(ans[1])+" "+str(ans[2])+" "+str(ans[3])+" "+str(ans[4])).encode())
data = conn.recvall()
print(data)
