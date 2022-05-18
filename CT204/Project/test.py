def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue

def encryptChar(char, K1):
    return chr((K1 * (ord(char)-65) ) % 26 + 65)
def encrypt(string, KEY):
    return "".join(encryptChar(c,KEY) for c in string)
def decryptChar(char, KI):
    return chr(KI * ((ord(char)-65) ) % 26 + 65)
def decrypt(string, KEY):
    KI = mod_inverse (KEY,26)
    return "".join(decryptChar(c,KI) for c in string)
p = 'ONAUGUST'


KEY = 7
c = encrypt(p,KEY)
print (c)
print(decrypt(c,KEY))