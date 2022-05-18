#ma hoa
def ma_dao_nguoc_encrypt (message):
    i = len(message) - 1
    translated = ''
    while (i >= 0):
        translated = translated + message[i]
        i = i-1
    return translated

#giai ma
def ma_dao_nguoc_decrypt (translated):
    i = len(translated) - 1
    decrypted = ''
    while (i >= 0):
        decrypted = decrypted + translated[i]
        i = i - 1
    return decrypted