from Crypto.Util.number import getPrime, long_to_bytes, inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
#from secret import FLAG


class RNG:

    def __init__(self, seed):
        self.e = 0x10001
        self.s = seed

        self.r = getPrime(768)
        while True:
            self.p, self.q = getPrime(768), getPrime(768)
            if self.p < self.r and self.q < self.r:
                break

        self.n = self.p * self.q * self.r
        phi = (self.p - 1) * (self.q - 1) * (self.r - 1)
        self.d = inverse(self.e, phi)

    def next(self):
        self.s = (self.s * self.p + self.q) % self.r
        return self.s


def main():
    rng = RNG(getPrime(512))
    rns = [rng.next() for _ in range(5)]

    key = sha256(long_to_bytes(rng.d)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    enc_flag = cipher.encrypt(pad(FLAG, 16)).hex()

    with open('output.txt', 'w') as f:
        f.write(f'n = {rng.n}\n')
        f.write(f's = {rns}\n')
        f.write(f'enc_flag = {enc_flag}\n')


if __name__ == "__main__":
    p=894446245510925900757859218978228942794252337676198559768107950260678987733529823340885254193604339932972486658396833844024474787422962270607186965094559134722178099791320470738178233762259364213340978694468588119134919693759610053
    q=906733274052529276109592299297997707435365596776010684213565378608820566280655233518772810060517362344918531956429564180076441739921005749502457162256034890280334645973185184863364876570734016299914442372810566038540388164095793981
    r=1175319410653790713318161315597014087606020658360287700168819990622753451616704400432418300009958541178974736666240265702120596805253727238317148553986872464800708521002965176311173263861008683624274661261421906954267093414402220131
    n=953212452632162415623854742466108898886257018761981737488515480124784784754313403541058723530771941185648440076953890845364164881753643355212476926626742101375422468157394494383915186197027584298810203766388023131196821200163753827759350781726289328080241887775877824351482527440834821313689834438591567613042759531267263403394331824891899899505726815540209695860955058659042180466101027165453544129867565132811217413181292156021136184504130428910065116301275284964237087553827437109939035287527986380535446925078275313404977210504275217640523278087762041948497195357622678060873426815474421439984697128135689500335385151376561597600186415289317989920506634067994928935237389715706143172780083
    phi=(p-1)*(q-1)*(r-1)
    
    d=pow(65537,-1,phi)
    key = sha256(long_to_bytes(d)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    enc_flag = cipher.decrypt(bytes.fromhex("d3587442177b157fa0cecb6dd880872d86e15a50e3f05ecfeea8b90f5cfca22835a59d9c4f23e87a68317d4ccabe1bf3aa2e6cdf0a9ef1ada0a2e83d8da0bff2b739cf0e2b2b779958d9b1154a6f3698"))
    print(enc_flag)

#file:///C:/Users/lukic/AppData/Local/Temp/Rar$EXb12376.18919/embryonic-plant/README.html