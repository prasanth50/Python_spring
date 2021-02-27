def encrypt(msg):
    translated = ''
    i = len(msg) - 1
    while i >= 0:
        translated += msg[i]
        i -= 1
    print("The cipher msg is : ", translated)
    return translated

def decrypt(msg):
    translated = ''
    i = len(msg) - 1
    while i >= 0:
        translated += msg[i]
        i -= 1
    print("The decrypted msg is : ", translated)
message = "CEASER CIPHER DEMO"
x = encrypt(message)
print(x)
decrypt(x)