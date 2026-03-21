# Letters (lowercase + uppercase)
import random
letters = ['a','b','c','d','e','f','g','h','i','j',
           'k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']

# Numbers
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '+', '=', '{', '}',
           '[', ']', ':', ';', '<', '>', '?', '/',
           '|', '~']
#
# print("Welcome to password GEN")
# nr_letters=int(input("Letters:"))
# nr_symbols=int(input("Symbols:"))
# nr_numbers=int(input("Numbers:"))
#
# password =""
# for char in range(0, nr_letters):
#     password +=random.choice(letters)
# for char in range(0, nr_symbols):
#     password +=random.choice(symbols)
# for char in range(0, nr_numbers):
#     password +=random.choice(numbers)

print("Welcome to password GEN")
nr_letters=int(input("Letters:"))
nr_symbols=int(input("Symbols:"))
nr_numbers=int(input("Numbers:"))

password_list =[]
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print(password_list)

password=("")
for char in password_list:
    password+=char

print(f"Password: {password}")


