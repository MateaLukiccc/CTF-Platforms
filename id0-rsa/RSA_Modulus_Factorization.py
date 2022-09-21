from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, inverse
from math import gcd #for gcd function (or easily implementable to avoid import)
import random #for random elements drawing in RecoverPrimeFactor
n=int("00cc0262c3764f6d1bfa485a88c0566a6d68cb89ac382fbbc577a4862bdbce111bb59960ea787f132e3fddb9c914d0d11d156dd433a2adab9084d48cf58f58b42804805966ecd318ad19218791e14e19a8d0cf3441e219e5e1395eb5dba1fba11d94321a34eb536c51f4c44c5987e74a467b5fe2eae8d2725d63f24feebfd9ca746de93b6fd74ed82fed7dbfc3a84b0a425f52503ab71908a13ac11a9d52211042290ae2886626f67935dc78b7d86ba76d3c5e085a003dff06f914187acc368f904613cbd3d52f36c8b0535f9dfeec2737744ad8be51f66e1d470261a7fd7c6da277dbd2f213b44d9e8242a8a5b121acc8710baed3d244004e4ca560d58e756ba7",16)


e=65537

d=int("0087803a2b0b44dbfa8e354a74b41371a2f3cce4c74f965cc85e9c1745c03bd15f2f320d8e0eb4907fd289a9a16642fff1aa4f0577ba6051a8aea12272e3600e60da0489dcf4058dc942fce337c0870841f956f6a59fd085c01f43c9d474755660f81283178d0a1ed31c98d9014a6414105657acb74c26a3316676062354a80a70335a670675f439dec08803def4892c4d99e20fbe1975d7673679ac6f16835307ce59971c865d71edeea9ed1a93c70a37e283f270dea8499271268d86f7fc4a1b4f64041833c62a057dfb0b48f1c4f6d351673238a3de3b4506eb2472aaf90b914e791c3a723464d9169d5eab8e0a3f8a42dedb065829e8b533a89dd3ba0a00a1",16)


def failFunction():
    	print("Prime factors not found")

def outputPrimes(a, n):
	p = gcd(a, n)
	q = int(n // p)
	if p > q:
		p, q = q, p
	print("Found factors p and q")
	print("p = {0}".format(str(p)))
	print("q = {0}".format(str(q)))
	return p,q


def RecoverPrimeFactors(n, e, d):
	"""The following algorithm recovers the prime factor
		s of a modulus, given the public and private
		exponents.
		Function call: RecoverPrimeFactors(n, e, d)
		Input: 	n: modulus
				e: public exponent
				d: private exponent
		Output: (p, q): prime factors of modulus"""

	k = d * e - 1
	if k % 2 == 1:
		failFunction()
		return 0, 0
	else:
		t = 0
		r = k
		while(r % 2 == 0):
			r = int(r // 2)
			t += 1
		for i in range(1, 101):
			g = random.randint(0, n) # random g in [0, n-1]
			y = pow(g, r, n)
			if y == 1 or y == n - 1:
				continue
			else:
				for j in range(1, t): # j \in [1, t-1]
					x = pow(y, 2, n)
					if x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
					elif x == n - 1:
						continue
					y = x
					x = pow(y, 2, n)
					if  x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
  
  
  
p, q = RecoverPrimeFactors(n, e, d) #if we need phi or p or q we can use this function
phi = (p-1) * (q-1)

print(min(p,q) % 100000007)