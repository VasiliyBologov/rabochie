#!/usr/bin/python3

"""
Created on 9.12.19


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""


from pyisemail import is_email
import datetime
import os

#print(datetime.datetime.today())
"""t1 = datetime.datetime.today()"""

address = "kthompson@chevyfordmotorplex.com"
print(datetime.datetime.today())
bool_result_with_dns = is_email(address, check_dns=True)
print(bool_result_with_dns)
print(datetime.datetime.today())
detailed_result_with_dns = is_email(address, check_dns=True, diagnose=True)
print(detailed_result_with_dns)

print(datetime.datetime.today())
detailed_result_with_dns = is_email(address, diagnose=True)
print(detailed_result_with_dns)

print(datetime.datetime.today())
detailed_result_with_dns = is_email(address)
print(detailed_result_with_dns)
print(datetime.datetime.today())