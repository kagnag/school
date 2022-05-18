from tkinter import *
from tkinter import messagebox
def encrypt(plaintext, key):
    # plaintext = plaintext.upper()
    # key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext
def decrypt(ciphertext, key):
    # ciphertext = ciphertext.upper()
    # key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext
# # p = "THISCRYPTOSYSTEMISNOTSECURE"
# # k = "CIPHER"
# p = input('Nhap plain: ')
# k = input('Nhap key: ')
# c = encrypt(p,k)
# print (c)
# print (decrypt(c,k))

def vingenere_encrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return
    if keytext.islower():
        keytext = keytext.upper()
    if plaintext.islower():
        cipher_text = encrypt(plaintext.upper(), keytext)
        cipher_text = cipher_text.lower()

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

def vingenere_decrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return
    if keytext.islower():
        keytext = keytext.upper()
    if plaintext.islower():
        cipher_text = decrypt(plaintext.upper(), keytext)
        cipher_text = cipher_text.lower()

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