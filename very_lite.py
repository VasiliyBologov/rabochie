#!/usr/bin/python3

"""
Created on 9.12.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""

from validate_email import validate_email


import datetime
import os

print(datetime.datetime.today())
t1 = datetime.datetime.today()
pasth = os.getcwd() + "/For Vasya.csv"

file = open(pasth, 'r')

s = file.readlines()

s = [line.rstrip() for line in s]
s = [line.split(',') for line in s]
print(s)

new_s = []

i = 0
while i < len(s):
    emailinput = s[i][4]
    if validate_email(emailinput):
        if validate_email(emailinput, check_mx=True):
            print(str(i) + '  ' + s[i][4] + '  very  true')
            new_s.append(s[i])
    i+=1

print(new_s)
pasth = os.getcwd() + "/new_very.csv"

file2 = open(pasth, 'w')

file2.readlines(new_s)


print(t1)
print(datetime.datetime.today())