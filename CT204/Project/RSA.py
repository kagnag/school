import sys
from base64 import b64encode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

from tkinter import *
from Cryptodome import Random
# keyPair = RSA.generate(2048)
random_generator = Random.new().read
rsa_key = RSA.generate(2048, random_generator)
# pubKey = keyPair.random.publickey()
pubKey = rsa_key.publickey()
keyPair = rsa_key

# TAO KHOA
# print('TAO KHOA')
# keyPair = RSA.generate(2048)
# pubKey = keyPair.publickey()
# # print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# # print(pubKeyPEM.decode('ascii'))
# # print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))


# Plaintext
# print("Plaintext")
# msg = bytes(str(input("Enter plain text: ")), 'utf-8')
msg = bytes(str(''), 'utf-8')

# MA HOA
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted))
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
# print('Decrypted:', decrypted.decode('utf-8'))


def taoKhoa(text_cong_khai, text_bi_mat, text_cong_khai_giai_ma, text_bi_mat_giai_ma):
    random_generator = Random.new().read
    rsa_key = RSA.generate(2048, random_generator)
    # pubKey = keyPair.random.publickey()
    pubKey = rsa_key.publickey()
    keyPair = rsa_key
    
    text_cong_khai.delete("1.0", END)
    text_bi_mat.delete("1.0", END)
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()
    text = pubKeyPEM.decode('ascii').strip('-----BEGIN PUBLIC KEY-----\n')
    text_cong_khai.insert('end-1c', text.strip('-----END PUBLIC KEY-----'))
    text_cong_khai_giai_ma.insert(
        'end-1c', text.strip('-----END PUBLIC KEY-----'))
    text_bm = privKeyPEM.decode('ascii').strip(
        ' -----BEGIN RSA PRIVATE KEY-----\n')
    text_bi_mat.insert(
        'end-1c', text_bm.strip('-----END RSA PRIVATE KEY-----'))
    text_bi_mat_giai_ma.insert(
        'end-1c', text_bm.strip('-----END RSA PRIVATE KEY-----'))


def ma_hoa_RSA(cipher_text, plaintext):
    msg = plaintext.get('1.0', "end-1c").strip()
    msg = bytes(str(msg), 'utf-8')
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    cipher_text.delete("1.0", END)
    cipher_text.insert('end-1c',  binascii.hexlify(encrypted))


def giai_ma_RSA(ciphertext_giai_ma, plaintext_giai_ma):
    msg = ciphertext_giai_ma.get('1.0', "end-1c").strip()
    msg = (binascii.a2b_hex(msg))
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(msg)
    plaintext_giai_ma.delete("1.0", END)
    plaintext_giai_ma.insert('end-1c',  decrypted.decode('utf-8'))

# -----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArEKi0yZ0XFepZ1eIoRQD
# YWjt06Ng4dyDpCyhmcF4nLwdpSM47zs7YgTt1y+DzqPcawhnQSdcSLvz3b0EGJyw
# l3Wkk4GlqKi4L2zFAcucFSG5ZZ7Pa8M8pPhR0mY75zo8WdzD1o4Ya3nAwno0R9f7
# tmoV7vzUPNBj0nUmZdWNGcpg627Zx4SUf6KqPM9FagYHXZbF2ALRiiXSaLs7PhsU
# cM5JglrG+4fSy3e5m/earkzLX7MBymyPg/zoLkNw2Iq/wN1C2ekxy+xuSnL4r/xA
# qtJw0s6Bbn1iLdMlM1VCxbiGR4X5za/ll98QrmDW3eqHPvyk0ZLvN0OQdsP3AKh2
# NQIDAQAB
# -----END PUBLIC KEY-----

# -----BEGIN RSA PRIVATE KEY-----
# MIIEowIBAAKCAQEAw9U+W4GtxeRmJf2AWkhYg2C4hMM2u1VtKW8+sj+u5xoh47C4
# R9kBG2I5TlkHYHUokpw4eEIXWlbG+NiCeCn3QWAG+ipAZdukjj0ebEShxYRSL2p3
# cruw0JPlJGF1DK/e9ghisc4vNxBNFf+vnhsG9b3Szqx3M/+R352w1dtl7PCG4i9h
# 4ShGj4jiKN5QKwBtqhoaMVwtIWRi/qqpyupzYa1DNBNzNASLF82L98Ys/SOQQmha
# VWPv5aqWZN1nUpTNJguWomnppzBA/F/17KxiKZy1YE8gdotcK8/Q9q2u+LvFfow3
# iVyIBgIDhDpYQ9qXksi42UdpVFMfx1MDQvk4NQIDAQABAoIBAB1xzCDvxBmGPbzw
# 5eIX5kXGqVJo6atMF7rhpkXLISNQALrJQO6omFaDiRtDHpf9tZ5+96yj6fqkI+GZ
# ktsPcET3nm+cd7dOSZU2EljJZEtxmaErJbpDXJKtPLL2JlEZ28ZsEgQq/LAPoY+G
# X2OV1mY6PDPlUZJTbHL4tPR1Za4KDr33iXZUF02WIX6c1Egyg7DXEcsTSh31RCxZ
# ktZht+YFF6k88rZKV4N/22LLKLlz/iIItD7i8XF8bfHVsh7DnqrdAfbSvMR1InQF
# 34Mi84YYkX6izVtM9g0S7My8hwInfimKlN/WRD8f5/sjWY29fEJOP4vdz9cT1co4
# oBQXZ7cCgYEA0hXLhyqHVZXWVJ3hWM7Q/2aM8xAgbj2IbHC/Tw2ZLSDIEcEAGNsA
# 72InJIMfdx0zDx8wowfd3o0wEnr4IfVgiuViSXryUhU7glWNORRdulJGzAJ94Szq
# uJ0HqGrSnME/49spdmmzU7MDPwNXD1D8qsYLHURUR77anJTpJc2eWU8CgYEA7qIL
# ZA8LhQ9CDvwm3H8RgCnSAjjKX65PMngjOSzDyBBQO8+pA8talbd57gbcE6H5+wDk
# 3ABNfQHq2n0UhCqzsyk0q3peGoUwhagb/+cZbXn4fqh2Yh6TPLmGA08PGiqIcWr5
# HCeKyeI7Ae1U5wC0VNqios44rqcC3MPTBxBMbTsCgYASp0LCBqGrlLlKHBaVJw/h
# jX54Wnc2spn5Xu1tnHx8SEvbX7KdglyL5MAq+sWBcwNElXVhFGK7zvd0vJxpj3r5
# +jIG6ja32RDGmsgGSGumDoYguRvqMW3J5I94gbuflX0RwzTkQbBdfyiLoMVLI9q7
# Ywg7mgSNtkF846/r3lzv+wKBgQCkvCTU7DXtozzdD2DccrPoH/akJgQ+zRxLIPhf
# 7fEx2WEqCQ8KWYWtOT3o/b9LplPl3RYgce0MURiJwDM7kib/lYCQqCbyc+OtQQIj
# RKwfEUZkWXNwBN9r2j8TZa5tR9NtSIWz0/BRseU+TVKBLdFPiqcfcPFcUFr/gAfc
# Jno8JQKBgBFO1XWsFgxTZEmLP+bjhrV1NT7gP00mzMeduZOWbOaPiOji3D2ADVv7
# uQl+zi4RCoXiveA8WJP/IhfCTho6rpMA1zorSiFFgVvJ+z+zooXS6f0yg7MWBVtk
# QGlHQzwPGIo6dYUNRtzFl8dmoDDqg8AHV9w7KrLjSOv4APaVdY/4
# -----END RSA PRIVATE KEY-----
