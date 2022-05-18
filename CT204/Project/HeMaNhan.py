from tkinter import *
from tkinter import messagebox
def mod_inverse(x, m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break
        elif n == m - 1:
            return "Null"
        else:
            continue


def encryptChar(char, K1):
    return chr((K1 * (ord(char)-65)) % 26 + 65)


def encrypt(string, KEY):
    return "".join(encryptChar(c, KEY) for c in string)


def decryptChar(char, KI):
    return chr(KI * ((ord(char)-65)) % 26 + 65)


def decrypt(string, KEY):
    KI = mod_inverse(KEY, 26)
    return "".join(decryptChar(c, KI) for c in string)


# p = 'ONAUGUST'


# KEY = 7
# c = encrypt(p, KEY)
# print(c)
# print(decrypt(c, KEY))

def nhan_encrypt(plaintext, keytext, ciphertext):
    plaintext = plaintext.get("1.0", "end-1c").upper()
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return
    else:
        keytext = int(keytext)
    if  mod_inverse(keytext, 26) == 'Null':
        messagebox.showerror("Lỗi", "Khóa và 26 có ước chung lớn nhất là 1!")
        return
    cipher_text = encrypt(plaintext, keytext)

    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)



def nhan_decrypt(plaintext, keytext, ciphertext):
    plaintext = plaintext.get("1.0", "end-1c").strip()
    keytext = keytext.get()
    keytext = int(keytext)
    cipher_text = decrypt(plaintext, keytext)
    print(cipher_text)
    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)

