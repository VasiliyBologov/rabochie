#!/usr/bin/python3
"""
Created on 11.05.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""

from pyisemail import is_email
import datetime
import os



def verymail(email):
    print(email + '   ---   ' + str(is_email(email, check_dns=True, diagnose=True)))



if __name__ == '__main__':
    try:
        verymail('vasiliyqqq.b@xor.ai')
    except:
        print("error of valid")