#!/usr/bin/pythoon3
#prints chars in a string using for loop

name = input("Name: ")

for c in name:
    if (c == 'e'):
        continue
    print(c*8)
else:
    print("You dont have a good name")