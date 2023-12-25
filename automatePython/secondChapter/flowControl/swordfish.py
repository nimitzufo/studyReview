#!/usr/bin/python3

while True:
    print('who are you')
    name = input()
    if name != 'Joe':
        continue
    print('hello, Joe, what is the password? (It\'s a fish)')
    passwd = input()
    if passwd == 'swordfish':
        break
print('Access granted')
