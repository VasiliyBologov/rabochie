
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
pasth = os.getcwd() + "/1.csv"

file = open(pasth, 'r')

s = file.readlines()
file.close()
s = [line.rstrip() for line in s]
s = [line.split(',') for line in s]
print(s)

new_s = []
con =0
new_s.append(s[0])
i = 1
while i < len(s):
    emailinput = s[i][6]
    if validate_email(emailinput, verify=True):   #emailinput, verify=True
        print(str(i) + '  ' + s[i][6] + '  very  true')
        new_s.append(s[i])
    else:
        print(str(i) + '  ' + s[i][6] + '  not very')
        con += 1
        #print(con)
    i+=1

print(new_s)
print(con)


s_new_s = []
i = 0
while i < len(new_s):
    l = new_s[i][0]+";"+new_s[i][1] +";"+ new_s[i][2] +";"+ new_s[i][3] +";"+new_s[i][4]+";"+new_s[i][5]+";"+new_s[i][6]+";"+new_s[i][7]+";"+new_s[i][8]+'\n'  #";"+new_s[i][9]+";"+new_s[i][10]+";"+new_s[i][11]+";"+new_s[i][12]+'\n'
    s_new_s.append(l)
    i+=1

pasth = os.getcwd() + "/new_very"+str(datetime.datetime.today())+".csv"
file2 = open(pasth, 'w')
file2.writelines(s_new_s)
file2.close()
print(t1)
print(datetime.datetime.today())