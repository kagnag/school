import base64
from tkinter import *


def base_encrypt(message, ciphertext):
    message = message.get("1.0", "end-1c")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    print(base64_bytes)
    base64_message = base64_bytes.decode('ascii')
    cipher_text = base64_message
    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)

def base_decrypt(message, ciphertext):
    message = message.get("1.0", "end-1c")
    base64_bytes = message
    plain_bytes = base64.b64decode(base64_bytes)
    plain_text = plain_bytes.decode('ascii')

    cipher_text = plain_text
    ciphertext.delete("1.0", END)
    cipher_text = cipher_text.strip()
    ciphertext.insert("end", cipher_text)