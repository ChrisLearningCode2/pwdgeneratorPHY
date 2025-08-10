import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input('Amount of passwords: '))
length = int(input('Input your password length: '))

print('\nHere are your passwords:')

for _ in range(number):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)   # moved outside inner loop