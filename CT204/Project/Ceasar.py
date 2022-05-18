from tkinter import *
from tkinter import messagebox


def ceasar_encrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c")
    keytext = keytext.get()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
        return
    elif (len(keytext) == 0):
        messagebox.showerror("Lỗi", "Khóa rỗng!")
        return

    else:
        keytext = int(keytext)
    cipher_text = encrypt(plaintext, keytext)

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


def ceasar_decrypt(plaintext, keytext, ciphertext, test):
    plaintext = plaintext.get("1.0", "end-1c").strip()
    keytext = keytext.get()
    keytext = int(keytext)
    cipher_text = decrypt(plaintext, keytext)
    print(cipher_text)
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
    print('ket thuc ham')


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
