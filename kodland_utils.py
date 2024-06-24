import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_length = int(input("panjang kata sandi: "))
password = ""

for i in range (pass_length):
    password += random.choice(char)

print (password)