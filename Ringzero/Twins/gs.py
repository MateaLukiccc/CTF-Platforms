n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899

e = 65537

c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

from sympy.ntheory.primetest import is_square
from Crypto.Util.number import long_to_bytes,inverse
import sympy
def fermat(n):
    a = int(sympy.sqrt(n)) # Fermat's Algorithm
    b = (a*a) - n
    while not is_square(b):
        a += 1
        b = (a*a) - n
    else:
        p = int(a - (sympy.sqrt(b)))
        q = n//p
        if p * q == n:
            return p,q
        else:
            return "No Luck"
        
p,q = fermat(n)
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m).decode('ascii'))