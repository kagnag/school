import random
import sys
from tkinter import *
from tkinter import messagebox


def thayTheDonMaHoa(plaintext, keytext, test, ciphertext):
    plaintext = plaintext.get('1.0', "end-1c").strip().replace(" ", "-")
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi!", "Văn bản rỗng!")

    # XU LY KEY
    # key = key.get().strip()
    cipher_text = encrypt(plaintext, keytext)
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


def thayTheDonGiaiMa(ciphertext, keytext, test, plaintext):
    ciphertext = ciphertext.get('1.0', "end-1c").strip().replace(" ", "-")
    if len(ciphertext) == 0:
        messagebox.showerror("Lỗi!", "Văn bản rỗng!")

    keytext = keytext.upper()
    plain_text = decrypt(ciphertext, keytext)
    plaintext.delete("1.0", END)
    # ciphertext = cipher_text.strip()
    plaintext.insert("end", plain_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == plain_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")


def encrypt(message, key):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated


def decrypt(message, key):
    translated = ''
    charsB = LETTERS
    charsA = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated


def getRandomKey():
    randomList = list(LETTERS)
    random.shuffle(randomList)
    s = ''.join(randomList)
    return s


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# message = 'defend the east wall of the castle'
# key = ''
# key = input("Enter 26 ALPHA key (blank for random key): ")
# if key == '':
#     key = getRandomKey()

# translated = encrypt(message, key)
# print('Using key: %s' % (key))
# print('Cipher: ' + translated)
# print('Plain: ' + decrypt(translated, key))
