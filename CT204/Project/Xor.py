from tkinter import messagebox
from tkinter import *
from itertools import cycle
import base64
import binascii


def xor_encrypt_string(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data,
                                                           cycle(key)))
    xored = xored.encode('ascii')
    # xored = base64.encodestring(xored).strip()
    # xored = xored.hex()
    return xored


def xor_decrypt_string(data, key):
    # data = base64.decodestring(data)
    data = data.decode('ascii')
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data,
                                                           cycle(key)))
    return xored


key = 'ka'
secret_data = "GoodLife"
c = xor_encrypt_string(secret_data, key)
# print("The cipher text is")
# print(c)
# print("The plain text fetched")
# print(xor_decrypt_string(c, key))


def xor_encrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return
    cipher_text = xor_encrypt_string(plaintext, keytext)
    cipher_text = cipher_text.hex()

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


def xor_decrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return
    plaintext = binascii.unhexlify(plaintext)
    cipher_text = xor_decrypt_string(plaintext, keytext)

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
