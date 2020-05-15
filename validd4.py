

#!/usr/bin/python3

"""
Created on 9.12.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""




from validate_email import validate_email


import datetime

import urllib.request as rq

"""#emailinput=input('Введите почту: ')"""
emailinput = 'vasilii.b@xor.ai'



#print(datetime.datetime.today())
#print(validate_email(emailinput))
#print(datetime.datetime.today())
#print('mx ' + str(validate_email(emailinput, check_mx=True)))
print(datetime.datetime.today())
print('very ' + str(validate_email(emailinput, verify=True)))

print(datetime.datetime.today())