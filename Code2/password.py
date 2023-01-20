import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = int(input('number of passwords?'+ "\n"))
length = int(input('password length?'+ "\n"))
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print(password)
while True:
    a = input("Press Enter To Exit")
    break