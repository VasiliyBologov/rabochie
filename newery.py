
import socket
import smtplib
#import resolver
import re
import random
from threading import Thread

import os
from validate_email import validate_email
import datetime

coin = 0
cont = []



def validmailvaso(linee):
	#print(linee)
	try:
		lineee = linee.split(',')

		emailinput = lineee[6]
		#print(emailinput)
		if validate_email(emailinput, check_regex=True, check_mx=True):  # emailinput, verify=True
			#print(emailinput + '  very  true')
			cont.append(linee + "\n")
			"""nefl1 = open(os.getcwd() + '/04_02_to_spam 2.csv', 'a')
			nefl1.writeline(linee + "\n")
			nefl1.close()"""
	# coin += 1
	except:
		print("error++" + linee)


	"""else:
		print(emailinput + '  not very')"""



print(datetime.datetime.today())
t1 = datetime.datetime.today()

fil = open(os.getcwd() + '/23_01_to_check.csv', 'r')
contact = fil.readlines()
fil.close()

contact = [line.rstrip() for line in contact]
contact2 = [line.split(',') for line in contact]

validmailvaso(contact2[51][6])


threads = list()
for index in contact:
    x = Thread(target=validmailvaso, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
        thread.join()

#print(coin)

print(t1)
nefl = open(os.getcwd() + '/05_02_to_spam.csv', 'w')
nefl.writelines(cont)
nefl.close()

print(datetime.datetime.today())