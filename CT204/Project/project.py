import string
from argparse import FileType
from cProfile import label
from email import message
from fileinput import filename
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tokenize import String
from turtle import bgcolor, color, width
from tkinter import ttk
from click import command, edit, open_file
from matplotlib.pyplot import fill, grid, text

import MaDaoNguoc_ReverseCipher
from DES import *
from MaDoiCho import *
from MaThayTheDon import *
import RSA as rsa
from Ceasar import *
from Affine import *
from Vingenere import *
from Hill import *
from base_64 import *
from Xor import *
from Rot13 import *
from HeMaNhan import *

root = Tk()
root.title("An toàn và Bảo mật thông tin")
root.geometry("800x600")

my_menu = Menu(root)
root.config(menu=my_menu)


def our_command():
    pass

# XU LY CAC HAM MA HOA

# TODO: Viet ham xu ly Ma Dao Nguoc


def mahoa_reverse(plaintext, ciphertext, test, funtion):
    plaintext = plaintext.get("1.0", "end-1c")
    if len(plaintext) == 0:
        messagebox.showerror("Lỗi", "Văn bản rỗng!")
    cipher_text = funtion(plaintext)
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

# DES
# TODO: Viet ham ma hoa HE MA DES


def pad(text):
    n = len(text) % 8
    n = 8-n
    while (n >= 1):
        text += ' '
        n -= 1
    return text


def des_ma_hoa(plaintext, key, ciphertext, test, funtion):
    plaintext = plaintext.get('1.0', "end-1c").strip().upper()
    key = key.get().strip().upper()
    # print(len(plaintext))
    if len(plaintext) == 0:
        mes = messagebox.showerror("Lỗi!", "Văn bản rỗng!")
    elif len(key) == 0:
        mes = messagebox.showerror("Lỗi!", "Khóa rỗng!")

    if checkHex(plaintext.upper()) == False:
        plaintext = pad(plaintext)
        plaintext = plaintext.encode('utf-8').hex().upper()
    else:
        plaintext = plaintext[:16]
    # XU LY KEY
    # key = key.encode("utf-8").hex().upper()
    if checkHex(key) == False:
        key = key.encode('utf-8').hex().upper()
    if checkHex(plaintext.upper()) == False or checkHex(key) == False:
        messagebox.showerror(
            'Lỗi!', 'Văn bản và khóa phải ở dạng thập lục phân!')
    else:
        if (len(plaintext) < 16 or len(key) < 16):
            messagebox.showerror(
                'Lỗi!', 'Độ dài văn bản và khóa tối thiểu 64 bit')
    # Sinh khoa
    key = hex2bin(key)

    # Bang PC1
    keyp = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

    # Qua bang PC1 lay 56 bit tu 64 bit cua khoa
    key = permute(key, keyp, 56)

    # So luong bit dich vong
    shift_table = [1, 1, 2, 2,
                   2, 2, 2, 2,
                   1, 2, 2, 2,
                   2, 2, 2, 1]

    # Bang PC2: Nen 56 bit thanh 48 bit
    # Bảng PC2: Nén 56 bit thành 48 bit
    key_comp = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]
    # Phan chia khoa thanh nua trai va nua phai
    left = key[0:28]
    right = key[28:56]

    rkb = []
    rk = []
    for i in range(0, 16):
        # Dich vong trai theo so luong bit cua vong
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        # ket hop nua trai va nua phai
        combine_str = left + right

        # quan PC2: nen 56 bit thanh 48 bit
        round_key = permute(combine_str, key_comp, 48)

        rkb.append(round_key)
        rk.append(bin2hex(round_key))
    cipher_text = bin2hex(funtion(plaintext, rkb, rk))
    cipher_text = ''
    n = len(plaintext)/16
    i = 0
    while (i < n):
        plaintext_temp = plaintext[i*16: i*16 + 16]
        print(len(plaintext_temp))
        cipher_text += bin2hex(funtion(plaintext_temp, rkb, rk))
        i += 1
    ciphertext.delete("1.0", END)
    ciphertext.insert("end", cipher_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == cipher_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")

# TODO: Viet ham giai ma HE MA DES


def des_giai_ma(ciphertext, key, plaintext, test, funtion):
    ciphertext = ciphertext.get('1.0', "end-1c").strip()
    # plaintext = plaintext.encode('utf-8').hex()
    if len(ciphertext) == 0:
        mes = messagebox.showerror("Lỗi!", "Văn bản rỗng!")
    # XU LY KEY
    key = key.get().strip().upper()

    if checkHex(ciphertext) == False:
        ciphertext = ciphertext.encode('utf-8').hex().upper()
        ciphertext = pad(ciphertext)

    # key = key.encode("utf-8").hex().upper()
    if checkHex(key) == False:
        key = key.encode('utf-8').hex().upper()

    if checkHex(ciphertext) == False or checkHex(key) == False:
        messagebox.showerror(
            'Lỗi!', 'Văn bản và khóa phải ở dạng thập lục phân!')
    if (len(ciphertext) < 16 or len(key) < 16):
        messagebox.showerror(
            'Lỗi!', 'Độ dài văn bản và khóa tối thiểu 64 bit')
    # Sinh khoa
    # key = key.encode("utf-8").hex()
    key = hex2bin(key)

    # Bang PC1
    keyp = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

    # Qua bang PC1 lay 56 bit tu 64 bit cua khoa
    key = permute(key, keyp, 56)

    # So luong bit dich vong
    shift_table = [1, 1, 2, 2,
                   2, 2, 2, 2,
                   1, 2, 2, 2,
                   2, 2, 2, 1]

    # Bang PC2: Nen 56 bit thanh 48 bit
    # Bảng PC2: Nén 56 bit thành 48 bit
    key_comp = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]
    # Phan chia khoa thanh nua trai va nua phai
    left = key[0:28]
    right = key[28:56]

    rkb = []
    rk = []
    for i in range(0, 16):
        # Dich vong trai theo so luong bit cua vong
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        # ket hop nua trai va nua phai
        combine_str = left + right

        # quan PC2: nen 56 bit thanh 48 bit
        round_key = permute(combine_str, key_comp, 48)

        rkb.append(round_key)
        rk.append(bin2hex(round_key))

    # plain_text = bin2hex(funtion(ciphertext, rkb[::-1], rk[::-1]))
    plain_text = ''
    n = len(ciphertext)/16
    i = 0
    while (i < n):
        ciphertext_temp = ciphertext[i*16: i*16 + 16]
        plain_text += bin2hex(funtion(ciphertext_temp, rkb[::-1], rk[::-1]))
        i += 1
    try:
        plain_text = bytes.fromhex(plain_text).decode('utf-8')
    except UnicodeDecodeError:
        pass
    plaintext.delete("1.0", END)
    plaintext.insert("end", plain_text)

    testtext = test.get("1.0", "end-1c")
    if len(testtext) != 0:
        if testtext == plain_text:
            test.configure(bg="spring green")
        else:
            test.configure(bg="orange red")
    else:
        test.configure(bg="white")

# TODO:Ham reset


def reset(plaintext, ciphertext, testtext):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    testtext.delete("1.0", END)
    testtext.configure(bg="white")

# TODO: Ham Reset  voi cac doi so


def reset_with_key(plaintext, ciphertext, keytext, testtext):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    testtext.delete("1.0", END)
    keytext.delete(0, END)
    testtext.configure(bg="white")


def reset_with_key_a_b(plaintext, ciphertext, a, b):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    a.delete(0, END)
    b.delete(0, END)


def reset_with_key_a_b_a(plaintext, ciphertext, a, b, c):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)

def reset_with_key_a_b_c_d(plaintext, ciphertext, a, b, c, d):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)
    d.delete(0, END)


def reset_rsa(plaintext, ciphertext, textpublic, textpri):
    plaintext.delete("1.0", END)
    ciphertext.delete("1.0", END)
    textpublic.delete("1.0", END)
    textpri.delete("1.0", END)


# TODO: Ham mo file
def open_file(plaintext):
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    try:
        data = open(filename, "r")
    except FileNotFoundError:
        return
    datatext = data.read()
    plaintext.delete("1.0", END)
    plaintext.insert("end-1c", datatext)
    data.close()


# TODO: Viet ham Random Key
key_random = 'p h q g i u m e a y l n o f d x j k r c v s t z w b'.replace(
    ' ', '')


def randomKey(key_frame_ma_hoa, key_frame_giai_ma):
    global key_random
    key_random = getRandomKey()
    key = key_random
    for i in range(len(key)):
        e = Entry(key_frame_ma_hoa, width=1)
        e.delete(0, END)
        e.insert(0, key[i].lower())
        e.grid(column=i, row=1)
    s = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.replace(' ', '')
    for i in range(len(key)):
        e = Entry(key_frame_giai_ma, width=1)
        e.delete(0, END)
        e.insert(0, s[key.lower().index(s[i])])
        e.grid(column=i, row=1)


def save_file(ciphertext):
    ciphertext = ciphertext.strip()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:
        return
    # text2save = str(ciphertext.get(1.0, END))
    f.write(ciphertext)
    f.close()


# an tat ca cac frame
def hide_all_frame():
    reverse_cipher.pack_forget()
    for widgets in reverse_cipher.winfo_children():
        widgets.destroy()
    des_menu.pack_forget()
    for widgets in des_menu.winfo_children():
        widgets.destroy()
    doicho_Frame.pack_forget()
    for widgets in doicho_Frame.winfo_children():
        widgets.destroy()
    thaythedon_Frame.pack_forget()
    for widgets in thaythedon_Frame.winfo_children():
        widgets.destroy()
    RSA_Frame.pack_forget()
    for widgets in RSA_Frame.winfo_children():
        widgets.destroy()
    Ceasar_Frame.pack_forget()
    for widgets in Ceasar_Frame.winfo_children():
        widgets.destroy()
    Affine_Frame.pack_forget()
    for widgets in Affine_Frame.winfo_children():
        widgets.destroy()
    Vingenere_Frame.pack_forget()
    for widgets in Vingenere_Frame.winfo_children():
        widgets.destroy()    
    Hill_Frame.pack_forget()
    for widgets in Hill_Frame.winfo_children():
        widgets.destroy()
    Base_Frame.pack_forget()
    for widgets in Base_Frame.winfo_children():
        widgets.destroy()
    Rot13_Frame.pack_forget()
    for widgets in Rot13_Frame.winfo_children():
        widgets.destroy()
    Nhan_Frame.pack_forget()
    for widgets in Nhan_Frame.winfo_children():
        widgets.destroy()
    Xor_Frame.pack_forget()
    for widgets in Xor_Frame.winfo_children():
        widgets.destroy()



def checkHex(s):
    return all(c in string.hexdigits for c in s)


# TODO: TAO MENU CHO HE DAO NGUOC
def reverse_cipher():
    hide_all_frame()
    reverse_cipher.pack(fill=BOTH, expand=True)
    my_label = Label(reverse_cipher, text="Hệ mã đảo ngược - Reverse Cipher",
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(reverse_cipher)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text="Mã hóa")
    tabControl.add(giai_ma, text="Giải mã")
    tabControl.pack(expand=True, fill="both", side="top")

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    test_label.grid(column=0, row=1, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    testtext.grid(column=1, row=1, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=3, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=3, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=3, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: mahoa_reverse(
        plaintext, ciphertext, testtext, MaDaoNguoc_ReverseCipher.ma_dao_nguoc_encrypt))
    btn_ma_hoa.grid(column=1, row=2)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset(
        plaintext, ciphertext, testtext))
    btn_reset.grid(column=1, row=4, pady=20)

    # GIAI MA
    # cipher = StringVar()
    # cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, text="Ciphertext: ", width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open_giai_ma = Button(
        giai_ma, text="Open file", command=lambda: open_file(ciphertext_giai_ma))
    btn_open_giai_ma.grid(column=2, row=0, padx=20)

    test_label = Label(giai_ma, text="Test kết quả: ")
    test_label.grid(column=0, row=1, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    testtext_giai_ma.grid(column=1, row=1, pady=10)

    cipher_label = Label(giai_ma, text='Plaintext: ')
    cipher_label.grid(column=0, row=3, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=3, pady=10)
    btn_save_giai_ma = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get('1.0', END)))
    btn_save_giai_ma.grid(column=2, row=3, padx=20)

    btn_giai_ma = Button(giai_ma, text="Giải mã", command=lambda: mahoa_reverse(
        ciphertext_giai_ma, plaintext_giai_ma, testtext_giai_ma, MaDaoNguoc_ReverseCipher.ma_dao_nguoc_decrypt))
    btn_giai_ma.grid(column=1, row=2)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset(
        plaintext_giai_ma, ciphertext_giai_ma, testtext_giai_ma,))
    btn_reset.grid(column=1, row=4, pady=20)


def des_menu():
    hide_all_frame()
    des_menu.pack(fill=BOTH, expand=True)
    my_label = Label(des_menu, text='Hệ mã DES',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(des_menu)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: des_ma_hoa(
        plaintext, keytext, ciphertext, testtext, DES_encrypt))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher_giai_ma = StringVar()
    cipher_giai_ma.set("Ciphertext: ")
    label_cipher_giai_ma = Label(
        giai_ma, textvariable=cipher_giai_ma, width=15)
    label_cipher_giai_ma.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open_giai_ma = Button(giai_ma, text='Openfile',
                              command=lambda: open_file(ciphertext_giai_ma))
    btn_open_giai_ma.grid(column=2, row=0, padx=20)

    keytext_lable_giai_ma = Label(giai_ma, text="Nhập khóa:")
    keytext_lable_giai_ma.grid(column=0, row=1, padx=50)
    keytext_giai_ma = StringVar()
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test_giai_ma = StringVar()
    test_giai_ma.set("Test kết quả: ")
    test_label_giai_ma = Label(giai_ma, textvariable=test)
    # test_label_giai_ma.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain_giai_ma = StringVar()
    plain_giai_ma.set("Plaintext: ")
    label_plain_giai_ma = Label(giai_ma, textvariable=plain)
    label_plain_giai_ma.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save_giai_ma = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_giai_ma = Button(giai_ma, text="Giải mã", command=lambda: des_giai_ma(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma, DES_encrypt))
    btn_giai_ma.grid(column=1, row=3, pady=10)

    btn_reset_giai_ma = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset_giai_ma.grid(column=1, row=5, pady=20)

# TODO: TAO MENU CHO HE DOI CHO


def doiChoMenu():
    hide_all_frame()
    doicho_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(doicho_Frame, text='Hệ mã Đổi chỗ',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(doicho_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: doiChoMaHoa(
        plaintext, keytext, ciphertext, testtext, doicho_encrypt))
    btn_ma_hoa.grid(column=1, row=3)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher_giai_ma = StringVar()
    cipher_giai_ma.set("Ciphertext: ")
    label_cipher_giai_ma = Label(
        giai_ma, textvariable=cipher_giai_ma, width=15)
    label_cipher_giai_ma.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open_giai_ma = Button(giai_ma, text='Openfile',
                              command=lambda: open_file(ciphertext_giai_ma))
    btn_open_giai_ma.grid(column=2, row=0, padx=20)

    keytext_lable_giai_ma = Label(giai_ma, text="Nhập khóa:")
    keytext_lable_giai_ma.grid(column=0, row=1, padx=50)
    keytext_giai_ma = StringVar()
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test_giai_ma = StringVar()
    test_giai_ma.set("Test kết quả: ")
    test_label_giai_ma = Label(giai_ma, textvariable=test)
    test_label_giai_ma.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain_giai_ma = StringVar()
    plain_giai_ma.set("Plaintext: ")
    label_plain_giai_ma = Label(giai_ma, textvariable=plain)
    label_plain_giai_ma.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save_giai_ma = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_giai_ma = Button(giai_ma, text="Giải mã", command=lambda: doiChoGiaiMa(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_giai_ma.grid(column=1, row=3)

    btn_reset_giai_ma = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset_giai_ma.grid(column=1, row=5, pady=20)

# TODO: TAO MENU CHO HE MA THAY THE DON


def thayTheDonMenu():
    hide_all_frame()
    thaythedon_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(thaythedon_Frame, text='Hệ mã Thay thế đơn',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(thaythedon_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    key_frame = Frame(ma_hoa, width=200)
    key_frame.grid(column=1, row=1)
    s = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    t = 'p h q g i u m e a y l n o f d x j k r c v s t z w b'
    s = s.replace(" ", "")
    t = t.replace(" ", "")

    for i in range(len(s)):
        e = Label(key_frame, width=1, text=s[i])
        e.grid(column=i, row=0)
    for i in range(len(t)):
        e = Entry(key_frame, width=1)
        e.insert(0, t[i])
        e.grid(column=i, row=1)
    # keytext = 'p h q g i u m e a y l n o f d x j k r c v s t z w b'
    # keytext = keytext.replace(' ', '')
    btn_random = Button(ma_hoa, text='Random',
                        command=lambda: randomKey(key_frame, key_frame_giai_ma))
    btn_random.grid(column=2, row=1, padx=20)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    # keytext = key_random
    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: thayTheDonMaHoa(
        plaintext, key_random, testtext, ciphertext))
    btn_ma_hoa.grid(column=1, row=3)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset(
        plaintext, ciphertext, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher_giai_ma = StringVar()
    cipher_giai_ma.set("Cipher: ")
    label_cipher_giai_ma = Label(
        giai_ma, textvariable=cipher_giai_ma, width=15)
    label_cipher_giai_ma.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open_giai_ma = Button(giai_ma, text='Openfile',
                              command=lambda: open_file(ciphertext_giai_ma))
    btn_open_giai_ma.grid(column=2, row=0, padx=20)

    keytext_lable_giai_ma = Label(giai_ma, text="Khóa:")
    keytext_lable_giai_ma.grid(column=0, row=1, padx=50)
    key_frame_giai_ma = Frame(giai_ma, width=200)
    key_frame_giai_ma.grid(column=1, row=1)
    # s = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    # t = 'p h q g i u m e a y l n o f d x j k r c v s t z w b'
    # s = s.replace(" ", "")
    # t = t.replace(" ", "")

    for i in range(len(s)):
        e = Label(key_frame_giai_ma, width=1, text=s[i])
        e.grid(column=i, row=0)
    for i in range(len(t)):
        e = Entry(key_frame_giai_ma, width=1)
        e.insert(0, s[t.index(s[i])])
        e.grid(column=i, row=1)
    # keytext = 'p h q g i u m e a y l n o f d x j k r c v s t z w b'
    # keytext = keytext.replace(' ', '')
    # btn_random_giai_ma = Button(giai_ma, text='Random',
    #                     command=lambda: randomKey(key_frame_giai_ma))
    # btn_random_giai_ma.grid(column=2, row=1, padx=20)

    test_giai_ma = StringVar()
    test_giai_ma.set("Test kết quả: ")
    test_label_giai_ma = Label(giai_ma, textvariable=test_giai_ma)
    test_label_giai_ma.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain_giai_ma = StringVar()
    plain_giai_ma.set("Plaintext: ")
    label_plain_giai_ma = Label(giai_ma, textvariable=plain_giai_ma)
    label_plain_giai_ma.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save_giai_ma = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_giai_ma = Button(giai_ma, text="Giải mã", command=lambda: thayTheDonGiaiMa(
        ciphertext_giai_ma, key_random, testtext_giai_ma, plaintext_giai_ma))
    btn_giai_ma.grid(column=1, row=3)

    btn_reset_giai_ma = Button(giai_ma, text=' Reset ', command=lambda: reset(
        plaintext_giai_ma, ciphertext_giai_ma, testtext_giai_ma))
    btn_reset_giai_ma.grid(column=1, row=5, pady=20)

# TODO: TAO MENU CHO HE MA RSA


def rsa_menu():
    hide_all_frame()
    RSA_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(RSA_Frame, text='Hệ mã RSA', font=(
        "Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(RSA_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    label_cong_khai = Label(ma_hoa, text='Khóa công khai').grid(
        column=0, row=2, pady=10)
    text_cong_khai = scrolledtext.ScrolledText(ma_hoa, width=40, height=3)
    text_cong_khai.grid(column=1, row=2)

    label_bi_mat = Label(ma_hoa, text='Khóa bí mật').grid(
        column=0, row=3, pady=20)
    text_bi_mat = scrolledtext.ScrolledText(ma_hoa, width=40, height=3)
    text_bi_mat.grid(column=1, row=3)

    tao_khoa = Button(ma_hoa, text='Tạo khóa',
                      command=lambda: rsa.taoKhoa(text_cong_khai, text_bi_mat))
    tao_khoa.grid(column=1, row=1, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=5, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=5, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=5, padx=20)

    mahoa = Button(ma_hoa, text='Mã hóa',
                   command=lambda: rsa.ma_hoa_RSA(ciphertext, plaintext))
    mahoa.grid(column=1, row=4, pady=20)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_rsa(
        plaintext, ciphertext, text_bi_mat, text_cong_khai))
    btn_reset.grid(column=1, row=6, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher_giai_ma = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher_giai_ma.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    label_cong_khai = Label(giai_ma, text='Khóa công khai').grid(
        column=0, row=2, pady=10)
    text_cong_khai_giai_ma = scrolledtext.ScrolledText(
        giai_ma, width=40, height=3)
    # text_cong_khai_giai_ma
    text_cong_khai_giai_ma.grid(column=1, row=2)

    label_bi_mat_giai_ma = Label(giai_ma, text='Khóa bí mật').grid(
        column=0, row=3, pady=20)
    text_bi_mat_giai_ma = scrolledtext.ScrolledText(
        giai_ma, width=40, height=3)
    text_bi_mat_giai_ma.grid(column=1, row=3)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=5, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=5, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=5, padx=20)

    giaima = Button(giai_ma, text='Giải mã',
                    command=lambda: rsa.giai_ma_RSA(ciphertext_giai_ma, plaintext_giai_ma))
    giaima.grid(column=1, row=4, pady=20)

    tao_khoa = Button(ma_hoa, text='Tạo khóa',
                      command=lambda: rsa.taoKhoa(text_cong_khai, text_bi_mat, text_cong_khai_giai_ma, text_bi_mat_giai_ma))
    tao_khoa.grid(column=1, row=1, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_rsa(
        plaintext_giai_ma, ciphertext_giai_ma, text_bi_mat_giai_ma, text_cong_khai_giai_ma))
    btn_reset.grid(column=1, row=6, pady=20)


def ceasar_menu():
    hide_all_frame()
    Ceasar_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Ceasar_Frame, text='Hệ mã CEASAR',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Ceasar_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: ceasar_encrypt(
        plaintext, keytext_entry, ciphertext, testtext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: ceasar_decrypt(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)


def affine_menu():
    hide_all_frame()
    Affine_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Affine_Frame, text='Hệ mã AFFINE',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Affine_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    # keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    # keytext_entry.grid(column=1, row=1)
    keytext_Frame = Frame(ma_hoa)
    keytext_Frame.grid(row=1, column=1)
    a = StringVar()
    b = StringVar()
    key_a_label = Label(keytext_Frame, text='a =  ').grid(row=0, column=0)
    key_a_entry = Entry(keytext_Frame, width=5, textvariable=a)
    key_a_entry.grid(row=0, column=1, padx=10)
    key_b_label = Label(keytext_Frame, text='b = ').grid(row=0, column=3)
    key_b_entry = Entry(keytext_Frame, width=5, textvariable=b)
    key_b_entry.grid(row=0, column=4, padx=10)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)
    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: affine_encrypt(
        plaintext, key_a_entry, key_b_entry,  ciphertext, testtext, key_a_nghich_dao_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key_a_b(
        plaintext, ciphertext, key_a_entry_giai_ma, key_b_entry_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

    # Giai ma
    cipher = StringVar()
    cipher.set("Plaintext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    # keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    # keytext_entry_giai_ma.grid(column=1, row=1)
    keytext_Frame_giai_ma = Frame(giai_ma)
    keytext_Frame_giai_ma.grid(row=1, column=1)
    key_a_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='a =  ').grid(row=0, column=0)
    key_a_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=a)
    key_a_entry_giai_ma.grid(row=0, column=1, padx=10)
    key_b_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='b = ').grid(row=0, column=3)
    key_b_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=b)
    key_b_entry_giai_ma.grid(row=0, column=4, padx=10)
    Label(keytext_Frame_giai_ma, text='a^-1 = ').grid(row=0, column=5, padx=10)
    key_a_nghich_dao_giai_ma = Entry(keytext_Frame_giai_ma, width=5)
    key_a_nghich_dao_giai_ma.grid(row=0, column=6)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Ciphertext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: affine_decrypt(
        ciphertext_giai_ma, key_a_entry_giai_ma, key_b_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key_a_b_a(
        plaintext_giai_ma, ciphertext_giai_ma, key_a_entry_giai_ma, key_b_entry_giai_ma, key_a_nghich_dao_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)


def vingenere_menu():
    hide_all_frame()
    Vingenere_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Vingenere_Frame, text='Hệ mã VINGENERE',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Vingenere_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: vingenere_encrypt(
        plaintext, keytext_entry, ciphertext, testtext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: vingenere_decrypt(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

def hill_menu():
    hide_all_frame()
    Hill_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Hill_Frame, text='Hệ mã HILL',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Hill_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    # keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    # keytext_entry.grid(column=1, row=1)
    keytext_Frame = Frame(ma_hoa)
    keytext_Frame.grid(row=1, column=1)
    a = StringVar()
    b = StringVar()
    c = StringVar()
    d = StringVar()
    key_a_label = Label(keytext_Frame, text='a =  ').grid(row=0, column=0)
    key_a_entry = Entry(keytext_Frame, width=5, textvariable=a)
    key_a_entry.grid(row=0, column=1, padx=10)
    key_b_label = Label(keytext_Frame, text='b = ').grid(row=0, column=3)
    key_b_entry = Entry(keytext_Frame, width=5, textvariable=b)
    key_b_entry.grid(row=0, column=4, padx=10)

    key_c_label = Label(keytext_Frame, text='c =  ').grid(row=1, column=0)
    key_c_entry = Entry(keytext_Frame, width=5, textvariable=c)
    key_c_entry.grid(row=1, column=1, padx=10)
    key_d_label = Label(keytext_Frame, text='d = ').grid(row=1, column=3)
    key_d_entry = Entry(keytext_Frame, width=5, textvariable=d)
    key_d_entry.grid(row=1, column=4, padx=10)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)
    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: hill_encrypt(
        plaintext, key_a_entry, key_b_entry,  key_c_entry, key_d_entry,ciphertext, testtext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key_a_b_c_d(
        plaintext, ciphertext, key_a_entry, key_b_entry, key_c_entry, key_d_entry))
    btn_reset.grid(column=1, row=5, pady=20)

    # Giai ma
    cipher = StringVar()
    cipher.set("Plaintext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    # keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    # keytext_entry_giai_ma.grid(column=1, row=1)
    keytext_Frame_giai_ma = Frame(giai_ma)
    keytext_Frame_giai_ma.grid(row=1, column=1)
    key_a_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='a =  ').grid(row=0, column=0)
    key_a_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=a)
    key_a_entry_giai_ma.grid(row=0, column=1, padx=10)
    key_b_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='b = ').grid(row=0, column=3)
    key_b_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=b)
    key_b_entry_giai_ma.grid(row=0, column=4, padx=10)

    key_c_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='c = ').grid(row=1, column=0)
    key_c_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=c)
    key_c_entry_giai_ma.grid(row=1, column=1, padx=10)

    key_d_label_giai_ma = Label(
        keytext_Frame_giai_ma, text='d = ').grid(row=1, column=3)
    key_d_entry_giai_ma = Entry(keytext_Frame_giai_ma, width=5, textvariable=d)
    key_d_entry_giai_ma.grid(row=1, column=4, padx=10)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Ciphertext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: hill_decrypt(
        ciphertext_giai_ma, key_a_entry_giai_ma, key_b_entry_giai_ma, key_c_entry_giai_ma, key_d_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key_a_b_c_d(
        plaintext_giai_ma, ciphertext_giai_ma, key_a_entry_giai_ma, key_b_entry_giai_ma, key_c_entry_giai_ma, key_d_entry_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

def base_menu():
    hide_all_frame()
    Base_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Base_Frame, text='Hệ mã BASE64',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Base_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    # keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    # keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: base_encrypt(
        plaintext, ciphertext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset(
        plaintext, ciphertext, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    # keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    # keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: base_decrypt(
        ciphertext_giai_ma,  plaintext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: resety(
        plaintext_giai_ma, ciphertext_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

def xor_menu():
    hide_all_frame()
    Xor_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Xor_Frame, text='Hệ mã XOR',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Xor_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: xor_encrypt(
        plaintext, keytext_entry, ciphertext, testtext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: xor_decrypt(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma, testtext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

def rot13_menu():
    hide_all_frame()
    Rot13_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Rot13_Frame, text='Hệ mã ROT13',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Rot13_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    # keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    # keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: rot13_encrypt(
        plaintext, ciphertext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    # keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    # keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: rot13_decrypt(
        ciphertext_giai_ma, plaintext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)

def nhan_menu():
    hide_all_frame()
    Nhan_Frame.pack(fill=BOTH, expand=True)
    my_label = Label(Nhan_Frame, text='Hệ mã NHÂN',
                     font=("Arial Bold", 10), pady=10).pack(side="top", fill="both")
    tabControl = ttk.Notebook(Nhan_Frame)
    ma_hoa = Frame(tabControl)
    giai_ma = Frame(tabControl)
    tabControl.add(ma_hoa, text='Mã hóa')
    tabControl.add(giai_ma, text='Giải mã')
    tabControl.pack(expand=True, fill='both', side='top')

    # MA HOA
    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(ma_hoa, textvariable=plain, width=15)
    label_plain.grid(column=0, row=0, padx=50, pady=30)
    plaintext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    plaintext.grid(column=1, row=0)
    btn_open = Button(ma_hoa, text='Openfile',
                      command=lambda: open_file(plaintext))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(ma_hoa, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext = StringVar()
    keytext_entry = Entry(ma_hoa, width=30, textvariable=keytext)
    keytext_entry.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(ma_hoa, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    # testtext.grid(column=1, row=2, pady=10)

    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(ma_hoa, textvariable=cipher)
    label_cipher.grid(column=0, row=4, padx=20, pady=20)
    ciphertext = scrolledtext.ScrolledText(ma_hoa, width=30, height=3)
    ciphertext.grid(column=1, row=4, pady=10)
    btn_save = Button(ma_hoa, text='Save', command=lambda: save_file(
        ciphertext.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(ma_hoa, text="Mã hóa", command=lambda: nhan_encrypt(
        plaintext, keytext_entry, ciphertext))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(ma_hoa, text=' Reset ', command=lambda: reset_with_key(
        plaintext, ciphertext, keytext_entry, testtext))
    btn_reset.grid(column=1, row=5, pady=20)

    # GIAI MA
    cipher = StringVar()
    cipher.set("Ciphertext: ")
    label_cipher = Label(giai_ma, textvariable=cipher, width=15)
    label_cipher.grid(column=0, row=0, padx=50, pady=30)
    ciphertext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    ciphertext_giai_ma.grid(column=1, row=0)
    btn_open = Button(giai_ma, text='Openfile',
                      command=lambda: open_file(ciphertext_giai_ma))
    btn_open.grid(column=2, row=0, padx=20)

    keytext_lable = Label(giai_ma, text="Nhập khóa:")
    keytext_lable.grid(column=0, row=1, padx=50)
    keytext_entry_giai_ma = Entry(giai_ma, width=30, textvariable=keytext)
    keytext_entry_giai_ma.grid(column=1, row=1)

    test = StringVar()
    test.set("Test kết quả: ")
    test_label = Label(giai_ma, textvariable=test)
    # test_label.grid(column=0, row=2, padx=20, pady=20)
    testtext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    # testtext_giai_ma.grid(column=1, row=2, pady=10)

    plain = StringVar()
    plain.set("Plaintext: ")
    label_plain = Label(giai_ma, textvariable=plain)
    label_plain.grid(column=0, row=4, padx=20, pady=20)
    plaintext_giai_ma = scrolledtext.ScrolledText(giai_ma, width=30, height=3)
    plaintext_giai_ma.grid(column=1, row=4, pady=10)
    btn_save = Button(giai_ma, text='Save', command=lambda: save_file(
        plaintext_giai_ma.get("1.0", END))).grid(column=2, row=4, padx=20)

    btn_ma_hoa = Button(giai_ma, text="Giải mã", command=lambda: nhan_decrypt(
        ciphertext_giai_ma, keytext_entry_giai_ma, plaintext_giai_ma))
    btn_ma_hoa.grid(column=1, row=3, pady=10)

    btn_reset = Button(giai_ma, text=' Reset ', command=lambda: reset_with_key(
        plaintext_giai_ma, ciphertext_giai_ma, keytext_entry_giai_ma, testtext_giai_ma))
    btn_reset.grid(column=1, row=5, pady=20)


# he co dien
he_co_dien = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Hệ mã cổ điển", menu=he_co_dien)
he_co_dien.add_command(
    label="Hệ mã đảo ngược - Reverse Cipher", command=reverse_cipher)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Caesar",
                       command=ceasar_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ đổi chỗ",
                       command=doiChoMenu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã thay thế đơn",
                       command=thayTheDonMenu)

he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Affine",
                       command=affine_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Vingenere",
                       command=vingenere_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Hill",
                       command=hill_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Base64",
                       command=base_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã Xor",
                       command=xor_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã ROT13",
                       command=rot13_menu)
he_co_dien.add_separator()
he_co_dien.add_command(label="Hệ mã NHÂN",
                       command=nhan_menu)
# he ma khoi
he_ma_khoi = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Hệ mã khối", menu=he_ma_khoi)
he_ma_khoi.add_command(label="Hệ mã DES", command=des_menu)

he_cong_khai = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Hệ mã khóa công khai", menu=he_cong_khai)
he_cong_khai.add_command(label="Mã RSA", command=rsa_menu)
he_cong_khai.add_separator()
he_cong_khai.add_command(label="Mã Elgamal", command=our_command)


# tao mot vai FRAME
reverse_cipher = Frame(root, width=500, height=500)
# reverse_cipher_giai_ma = Frame(root, width=500, height=500)
des_menu = Frame(root, width=500, height=500)
doicho_Frame = Frame(root, width=500, height=500)
thaythedon_Frame = Frame(root, width=500, height=500)
RSA_Frame = Frame(root, width=500, height=500)
Ceasar_Frame = Frame(root, width=500, height=500)
Affine_Frame = Frame(root, width=500, height=500)
Vingenere_Frame = Frame(root, width=500, height = 500)
Hill_Frame = Frame(root, width=500, height = 500)
Base_Frame = Frame(root, width=500, height = 500)
Xor_Frame = Frame(root, width=500, height = 500)
Rot13_Frame = Frame(root, width=500, height = 500)
Nhan_Frame = Frame(root, width=500, height = 500)

root.mainloop()
