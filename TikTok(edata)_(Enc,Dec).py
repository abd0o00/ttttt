import base64
import secrets

#BY : @maho_s9 
class Cha:
    def __init__(self, key: bytes, nonce: bytes, counter: int = 0):
        if len(key) != 32 or len(nonce) != 12:
            raise ValueError("Invalid key or nonce length")
        self.k = key
        self.n = nonce
        self.c = counter
    @staticmethod
    def _r(v, n): return ((v << n) & 0xFFFFFFFF) | (v >> (32 - n))
    @staticmethod
    def _qr(s, a, b, c, d):
        s[a] = (s[a] + s[b]) & 0xFFFFFFFF; s[d] ^= s[a]; s[d] = Cha._r(s[d], 16)
        s[c] = (s[c] + s[d]) & 0xFFFFFFFF; s[b] ^= s[c]; s[b] = Cha._r(s[b], 12)
        s[a] = (s[a] + s[b]) & 0xFFFFFFFF; s[d] ^= s[a]; s[d] = Cha._r(s[d], 8)
        s[c] = (s[c] + s[d]) & 0xFFFFFFFF; s[b] ^= s[c]; s[b] = Cha._r(s[b], 7)
    def _block(self, ctr: int):
        s = [0x61707865, 0x3320646e, 0x79622d32, 0x6b206574]
        s += [int.from_bytes(self.k[i*4:(i+1)*4], "little") for i in range(8)]
        s.append(ctr & 0xFFFFFFFF)
        s += [int.from_bytes(self.n[i*4:(i+1)*4], "little") for i in range(3)]
        w = s[:]
        for _ in range(10):
            self._qr(w, 0,4,8,12); self._qr(w, 1,5,9,13)
            self._qr(w, 2,6,10,14); self._qr(w,3,7,11,15)
            self._qr(w,0,5,10,15); self._qr(w,1,6,11,12)
            self._qr(w,2,7,8,13); self._qr(w,3,4,9,14)
        return b''.join(( (w[i]+s[i]) & 0xFFFFFFFF ).to_bytes(4,'little') for i in range(16))

    def _ks(self):
        ctr = self.c
        while True:
            block = self._block(ctr)
            ctr = (ctr +1) & 0xFFFFFFFF
            for b in block: yield b

    def _p(self, data: bytes) -> bytes:
        ks = self._ks()
        return bytes([b ^ next(ks) for b in data])


class edata:
    FLAG = b'\x01'
    @staticmethod
    def encrypt(txt: str) -> str:
        d = txt.encode('utf-8')
        k = secrets.token_bytes(32)
        n = secrets.token_bytes(12)
        c = Cha(k,n,0)
        ct = c._p(d)
        raw = edata.FLAG + k + n + ct
        return base64.b64encode(raw).decode()

    @staticmethod
    def decrypt(txt: str) -> str:
        raw = base64.b64decode(txt)
        if len(raw)<1+32+12:
            raise ValueError("Invalid edata")
        k = raw[1:33]; n = raw[33:45]; ct = raw[45:]
        c = Cha(k,n,0)
        plain = c._p(ct)
        return plain.decode('utf-8',errors='replace')




# Example 
enc = edata.encrypt("""{"code":200,"data":null,"message":"اكتمل التحقق","msg_code":"200","msg_sub_code":"success"}""")
print(enc)

dec = edata.decrypt("AZrj92N/wnRbPC7HymWSskzaZnTGr7xXmytjr6lQOb0MqZgRKqifUJp6ew7r9a+si4Ns0mnz3iaOrRTZ2If08BZvP1P6Z1g3vHHauL6Kjsp94l1FvfsOVwYxCo2ZZcwL5o38/5jd0vAwhzF7mD6X+uUOVMyNKrTvo+4sFa+VsTb2ajwjnLY5KZXdS9RvJh9qpidD")
print(dec)