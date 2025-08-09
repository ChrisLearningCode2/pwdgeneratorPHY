<h3>Simple Password Generator in Python</h3>

<h2>Practicing what I learned.</h2>

<pre>
import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Input your password length:')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for C in range(length):
        passwords += random.choice(chars)
        print(passwords)
</pre>

        

![Password Generator](https://private-user-images.githubusercontent.com/207068886/476320645-420c2ddc-6adb-4cb4-99c9-af430cf862b6.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTQ3ODM2ODgsIm5iZiI6MTc1NDc4MzM4OCwicGF0aCI6Ii8yMDcwNjg4ODYvNDc2MzIwNjQ1LTQyMGMyZGRjLTZhZGItNGNiNC05OWM5LWFmNDMwY2Y4NjJiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgwOVQyMzQ5NDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04N2E1NWMyOWMyZDY2MzA1YzM1ZWI0ZDlhMTY5OTBiM2QzNTBjZTdkMzdiNTU3MGJjYzQ0NGUzYjYzNWMzYWJjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bo6ygPU7MyP8wvzYZIrDFSWUiBB_Ye7wR626V3nm_fc)
