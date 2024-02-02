import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    lista = input("numero caratteri: ")
    if not lista.isdigit():
        print("metti un numero e non una stringa")
        input("premi invio per riprovare")
    else:
        lista = int(lista)
        break
password = ""
for i in range(lista):
    password += random.choice(caratteri)
print(password)