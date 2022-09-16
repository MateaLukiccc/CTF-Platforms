from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse,long_to_bytes,bytes_to_long
from base64 import b64decode, b64encode

from Crypto.Util.number import long_to_bytes    
import gmpy2
from libnum import *

def common_modulus(e1, e2, c1, c2, N):
    # Extended Euclidean algorithm
    a, b, d = xgcd(e1,e2)
    
    # Invert negative factor
    if b < 0:
        c2 = invmod(c2, N)
        b = -b
    if a < 0:
        c1 = invmod(c1, N)
        a = -a
    
    # Get the message (c1^a * c2^b) % N
    m = (pow(c1,a,N) * pow(c2,b,N)) % N
    return [m, a, b, d]
    
def pad(m, d, i, N):
    if -d*4*i < 0:
        f = pow(invmod(2, N), d*4*i, N)
    else:
        f = pow(2, -d*4*i, N)
    return m * f % N


N  =159585438595361133899064403925313292667610248442224647036010416034404442435484082119072280998365880338094856422539258182775650390275467245220889658519967161024328438435172539308214675409812619551677486472775899848638646965296072081488882895091126604300133127385230432039457448806852888531171023105985971330139
c1 =110953775612596011874905374542775389944500542184416291633839968557016713046219922611984320317763287043782189338396647679666671575220593955057426609724007800004114681750952538009760776460143352501448669571774840980125581187527821082599401263212601399779992453897197015498154091717383298226283055856598515648996
c2 =162854817250880230553353099752472866859698713131585890463318687334856834405688144348194288458414248635471268010256094751836956584242487060704141947180325553252490211872664567015095154070461589308347613351207283461558258837445421876575773622809612073855235241880763009236902882452976519984777181084494417709

f=open(r"C:\Users\lukic\Desktop\HTB\TwoForOne\message1","r")
c1=bytes(f.readline().encode())


f=open(r"C:\Users\lukic\Desktop\HTB\TwoForOne\message2","r")
c2=bytes(f.readline().encode())

f = open(r'C:\Users\lukic\Desktop\HTB\TwoForOne\key1.pem','r')
key = RSA.importKey(f.read())

N=key.n
e1=key.e

print(e1)

f = open(r'C:\Users\lukic\Desktop\HTB\TwoForOne\key2.pem','r')
key = RSA.importKey(f.read())

n2=key.n
e2=key.e

print(n2,e2)
c1 = int.from_bytes(b64decode(c1), 'big')
c2 = int.from_bytes(b64decode(c2), 'big')



m, _, _, _ = common_modulus(e1,e2,c1,c2,N)
flag = n2s(m)
print(flag)
