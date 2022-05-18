import string
from tkinter import *
from tkinter import messagebox


def split_len(seq, length):
    return [seq[i: i+length] for i in range(0, len(seq), length)]


def doiChoMaHoa(plaintext, key, ciphertext, test, funtion):
    plaintext = plaintext.get('1.0', "end-1c").strip()
    key = key.get().strip()
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi!", "Văn bản rỗng!")

    else:
        if len(key) == 0:
            messagebox.showerror("Lỗi!", "Khóa rỗng!")


    cipher_text = funtion(plaintext, key)
    ciphertext.delete("1.0", END)
    # ciphertext = cipher_text.strip()
    ciphertext.insert("end", cipher_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == cipher_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")


def doiChoGiaiMa(plaintext, key, ciphertext, test):
    plaintext = plaintext.get('1.0', "end-1c").strip()
    if len(plaintext) == 0:
        mes = messagebox.showerror("Lỗi!", "Văn bản rỗng!")

    key = key.get().strip()

    cipher_text = doicho_decrypt(plaintext, key)
    ciphertext.delete("1.0", END)
    # ciphertext = cipher_text.strip()
    ciphertext.insert("end", cipher_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == cipher_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")


def doicho_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                ciphertext += 'Z'
                # continue
    return ciphertext


def doicho_decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "")
    order = {
        int(val): num for num, val in enumerate(key)
    }
    plaintext = ''
    n = int(len(ciphertext)/len(key))
    for index in sorted(order.keys()):
        for part in split_len(ciphertext, n):
            try:
                plaintext += part[order[index]]
            except IndexError:
                continue
    return plaintext
# k = "12345"
# c = encrypt("HELLOWORLDLOVES", k)
# print(c)
# print(decrypt(c, k))
