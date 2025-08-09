<h3>Simple Password Generator in Python</h3>

<h2>Practicing what I learned.</h2>

import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length =('Input your password length')
lenrth =int(length)

print('Here are your passwords:')

for pwd in range(number):
    passwords = ''
    for C in range(length):
        passwords += random.choice(chars)
        print(passwords)

        
