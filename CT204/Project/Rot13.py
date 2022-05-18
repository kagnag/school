from tkinter import *
from tkinter import messagebox


def rot13_encrypt(plaintext, ciphertext):
    plaintext = plaintext.get("1.0", "end-1c")
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    keytext = 13
    cipher_text = encrypt(plaintext, keytext)

    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)


def rot13_decrypt(plaintext, ciphertext):
    plaintext = plaintext.get("1.0", "end-1c").strip()
    keytext = 13
    cipher_text = decrypt(plaintext, keytext)
    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)


def encrypt(text, k):
    text = text.replace(" ", "")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result


def decrypt(text, k):
    text = text.replace(" ", "")
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - k - 65) % 26 + 65)
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)
    return result

# text = "ABCDE"
# k = 2
# print("Key = :", k)
# c = encrypt(text, k)
# print("Cipher text: ", c)
# print("Plain text: ", decrypt(c, k))
