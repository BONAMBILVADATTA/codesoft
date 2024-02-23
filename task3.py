import random
import string
length=int(input("enter the length:"))
char=string.ascii_letters
char+=string.digits
char+=string.punctuation
password=""
for i in range(length):
    next_character=random.choice(char)
    password+=next_character
print("Requested random password:",password)
