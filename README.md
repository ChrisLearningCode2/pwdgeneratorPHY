<h3>Simple Password Generator in Python</h3>

<h2>Practicing what I learned.</h2>

<pre>
import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length =('Input your password length')
length =int(length)

print('Here are your passwords:')

for pwd in range(number):
    passwords = ''
    for C in range(length):
        passwords += random.choice(chars)
        print(passwords)
</pre>

        

![Password Generator](https://private-user-images.githubusercontent.com/207068886/476316355-e8266ab5-2895-4412-a4d5-a2cddf35a375.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTQ3Nzc3MDksIm5iZiI6MTc1NDc3NzQwOSwicGF0aCI6Ii8yMDcwNjg4ODYvNDc2MzE2MzU1LWU4MjY2YWI1LTI4OTUtNDQxMi1hNGQ1LWEyY2RkZjM1YTM3NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgwOVQyMjEwMDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lMTcyNmQ2YWZhNzM1M2M3OTgxOTEyYjVlZmYxMTZjNjMwYjgxMWNmMGMxZGVhNDRiMjQzMDJkMDc5NDZiMDk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.YviKLFZHlm0vDcQHP-ApTaHf2TjHIlcno-PHIY2pp_8)
