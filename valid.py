#!/usr/bin/python3

"""
Created on 9.12.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""


from pyisemail import is_email
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
coint = 0
i = 0
while i < len(s):
    #emailinput = s[i][4]
    if is_email(s[i][4], check_dns=True, diagnose=True):
        print(i)
        new_s.append(s[i])
    else:
        print(str(i) + '  error  ' + s[i][4])

        coint += 1

    i += 1
print(coint)
print(new_s)
pasth = os.getcwd() + "/new_very_"+str(datetime.datetime.today())+".csv"

file2 = open(pasth, 'w')
s_new_s = []
f = 0
while f < len(new_s):
    j = new_s[f][0] +','+ new_s[f][1] +','+ new_s[f][2] +','+ new_s[f][3] +','+ new_s[f][4]+'\n'
    s_new_s.append(j)
    f+=1


file2.writelines(s_new_s)


print(t1)
print(datetime.datetime.today())