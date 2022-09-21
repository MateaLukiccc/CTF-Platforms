C1 = int("94f145679ee247b023b09f917beea7e38707452c5f4dc443bba4d089a18ec42de6e32806cc967e09a28ea6fd2e683d5bb7258bce9e6f972d6a30d7e5acbfba0a85610261fb3e0aac33a9e833234a11895402bc828da3c74ea2979eb833cd644b8ab9e3b1e46515f47a49ee602c608812241e56b94bcf76cfbb13532d9f4ff8ba",16)
N1 = int("a5d1c341e4837bf7f2317024f4436fb25a450ddabd7293a0897ebecc24e443efc47672a6ece7f9cac05661182f3abbb0272444ce650a819b477fd72bf01210d7e1fbb7eb526ce77372f1aa6c9ce570066deee1ea95ddd22533cbc68b3ba20ec737b002dfc6f33dcb19e6f9b312caa59c81bb80cda1facf16536cb3c184abd1d5",16)
C2 = int("5ad248df283350558ba4dc22e5ec8325364b3e0b530b143f59e40c9c2e505217c3b60a0fae366845383adb3efe37da1b9ae37851811c4006599d3c1c852edd4d66e4984d114f4ea89d8b2aef45cc531cfa1ab16c7a2e04d8884a071fed79a8d30af66edf1bbbf695ff8670b9fccf83860a06e017d67b1788b19b72d597d7d8d8",16)
N2 = int("af4ed50f72b0b1eec2cde78275bcb8ff59deeeb5103ccbe5aaef18b4ddc5d353fc6dc990d8b94b3d0c1750030e48a61edd4e31122a670e5e942ae224ecd7b5af7c13b6b3ff8bcc41591cbf2d8223d32eeb46ba0d7e6d9ab52a728be56cd284842337db037e1a1da246ed1da0fd9bdb423bbe302e813f3c9b3f9414b25e28bda5",16)
C3 = int("8a9315ee3438a879f8af97f45df528de7a43cd9cf4b9516f5a9104e5f1c7c2cdbf754b1fa0702b3af7cecfd69a425f0676c8c1f750f32b736c6498cac207aa9d844c50e654ceaced2e0175e9cfcc2b9f975e3183437db73111a4a139d48cc6ce4c6fac4bf93b98787ed8a476a9eb4db4fd190c3d8bf4d5c4f66102c6dd36b73",16)
N3 = int("5ca9a30effc85f47f5889d74fd35e16705c5d1a767004fec7fdf429a205f01fd7ad876c0128ddc52caebaa0842a89996379ac286bc96ebbb71a0f8c3db212a18839f7877ebd76c3c7d8e86bf6ddb17c9c93a28defb8c58983e11304d483fd7caa19b4b261fc40a19380abae30f8d274481a432c8de488d0ea7b680ad6cf7776b",16)


from binascii import unhexlify
from functools import reduce
from gmpy2 import root
import gmpy2
gmpy2.get_context().precision = 4096
from itertools import combinations
from Crypto.Util.number import long_to_bytes

EXPONENT = 3

CIPHERTEXT_1 = "ciphertext.1"
CIPHERTEXT_2 = "ciphertext.2"
CIPHERTEXT_3 = "ciphertext.3"

MODULUS_1 = "modulus.1"
MODULUS_2 = "modulus.2"
MODULUS_3 = "modulus.3"


def chinese_remainder_theorem(items):
    # Determine N, the product of all n_i
    N = 1
    for a, n in items:
        N *= n

    # Find the solution (mod N)
    result = 0
    for a, n in items:
        m = N // n
        r, s, d = extended_gcd(n, m)
        if d != 1:
            raise "Input not pairwise co-prime"
        result += a * s * m

    # Make sure we return the canonical solution.
    return result % N


def extended_gcd(a, b):
    x, y = 0, 1
    lastx, lasty = 1, 0

    while b:
        a, (q, b) = b, divmod(a, b)
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y

    return (lastx, lasty, a)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_value(filename):
    with open(filename) as f:
        value = f.readline()
    return int(value, 16)

if __name__ == '__main__':
    c = [C1, C2, C3]
    n = [N1, N2, N3]
    for i,j,k in combinations(range(3),3):
        C = chinese_remainder_theorem([(c[i], n[i]), (c[j], n[j]), (c[k], n[k])])
    try:
        M = int(root(C, 3))
    except ValueError:
        pass
    else:
        print(long_to_bytes(M))    
    
