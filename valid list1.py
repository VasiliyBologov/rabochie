
#!/usr/bin/python3

"""
Created on 9.12.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""

from validate_email import validate_email


import datetime
import os

import socket
import smtplib
import dns.resolver
import re

print(datetime.datetime.today())
t1 = datetime.datetime.today()
pasth = os.getcwd() + "/For Vasya.csv"

file = open(pasth, 'r')

s = file.readlines()
file.close()
s = [line.rstrip() for line in s]
s = [line.split(',') for line in s]
print(s)

new_s = []
con =0
i = 0
while i < len(s):
    emailinput = s[i][4]
    try:
        addressToVerify = emailinput
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        if match == None:
            print('Bad Syntax')
            raise ValueError('Bad Syntax')

        r = emailinput.split('@')
        dom = r[1]
        print(dom)

        records_ = dns.resolver.query(dom, 'MX')
        mxRecord = records_[0].exchange
        mxRecord = str(mxRecord)

        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail(emailinput)
        code, message = server.rcpt(str(addressToVerify))
        server.quit()
    except:
        code = 0

    # Assume 250 as Success
    if code == 250:
        print(str(i) + '  Success')
        new_s.append(s[i])
    else:
        print(str(i) + '  Bad')
        con += 1

    i+=1

print(new_s)
print(con)


s_new_s = []
i = 0
while i < len(new_s):
    l = new_s[i][0]+new_s[i][1] + new_s[i][2] + new_s[i][3] +new_s[i][4]
    s_new_s.append(l)
    i+=1

pasth = os.getcwd() + "/new_very_new.csv"
file2 = open(pasth, 'w')
file2.writelines(s_new_s)
file2.close()
print(t1)
print(datetime.datetime.today())