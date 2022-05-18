from tkinter import *
from tkinter import messagebox
# ham tim nghich dao
def mod_inverse(x, m):
    for n in range(m):
        if (x*n)%m == 1:
            return n
            break
        elif n == m - 1:
            return "NULL"
        else:
            continue

class Affine(object):
    DIE = 26
    KEY = (7, 3, mod_inverse(7, 26)) #nghich dao
    
    def __init__(self):
        pass
    def encryptChar(self, char):
        K1, K2, KI = self.KEY
        if str.isupper(char):
            return chr((K1* (ord(char)-65) + K2) % self.DIE + 65)
        return chr((K1* (ord(char)-97) + K2) % self.DIE + 97)
    def encrypt(self, string):
        return "".join(map(self.encryptChar, string))
    def decryptChar(self, char):
        K1, K2, KI = self.KEY
        if str.isupper(char):
            return chr(KI* ((ord(char) - 65) - K2) % self.DIE + 65)
        return chr(KI* ((ord(char) - 97) - K2) % self.DIE + 97)
    def decrypt(self, string):
        return "".join(map(self.decryptChar, string))

affine  = Affine()
# plain = input("Nhap vao chuoi can ma hoa: ")
# crypt = affine.encrypt(plain)
# print(affine.KEY)
# print("Chuoi da ma hoa: ", crypt)
# print("Giai ma chuoi ma hoa: ", affine.decrypt('axg'))

def affine_encrypt(plaintext, key_a, key_b, ciphertext, test, key_a_nghich_dao):
    plaintext = plaintext.get("1.0", "end-1c")
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    else:
        a = (key_a.get())
        b = (key_b.get())
        if len(a) ==0 or len(b) == 0:
            messagebox.showerror("Lỗi", "Khóa rỗng!")
            return
        else:
            a = int(a)
            b = int(b)
    affine = Affine()
    if mod_inverse(a, 26) == "NULL":
        messagebox.showerror("Lỗi", "Không tìm thấy nghịch đảo của a!")
        ciphertext.delete("1.0", END)
        return
    print(mod_inverse(a, 26))
    key_a_nghich_dao.delete(0, END)
    key_a_nghich_dao.insert(0, mod_inverse(a, 26))
    affine.KEY = (a, b, mod_inverse(a, 26))
    cipher_text = affine.encrypt(plaintext)

    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == cipher_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")

def affine_decrypt(plaintext, key_a, key_b, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    a = int(key_a.get())
    b = int(key_b.get())
    affine = Affine()
    affine.KEY = (a, b, mod_inverse(a, 26))
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
    cipher_text = affine.decrypt(plaintext)
    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)
    print(affine.KEY)
    print(cipher_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == cipher_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")