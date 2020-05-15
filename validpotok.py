



import socket
import smtplib
import dns.resolver
import re
from threading import Thread
import requests
import time
import datetime
import os






def valider(file_nam, file_num2):



    path = os.getcwd() + "/"+ file_nam
    file = open(path, "r")
    senders = file.readlines()
    file.close()
    senders = [line.rstrip() for line in senders]

    #print(len(senders))

    for nm in senders:
        addressToVerify = nm

        try:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

            if match == None:
                print('Bad Syntax')
                raise ValueError('Bad Syntax')

            r = nm.split('@')
            dom = r[1]
            # print(dom)

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
            server.mail(nm)
            code, message = server.rcpt(str(addressToVerify))
            server.quit()
        except:
            code = 100500

        # Assume 250 as Success
        """if code == 250:
            #print('Success')

        else:
            #print('Bad')
            path2 = os.getcwd() + "/govnopochti" + file_num2
            f = open(path2, 'a')
            f.write(nm + '\n')
            f.close()"""
        if code != 250:
            # print('Bad')
            path2 = os.getcwd() + "/govnopochti" + file_num2
            f = open(path2, 'a')
            f.write(nm + '\n')
            f.close()









t_ = str(datetime.datetime.today())
print(t_)

thread1 = Thread(target=valider, args=('emails1', '1'))
thread2 = Thread(target=valider, args=('emails2', '2'))
thread3 = Thread(target=valider, args=('emails3', '3'))
thread4 = Thread(target=valider, args=('emails4', '4'))
thread5 = Thread(target=valider, args=('emails5', '5'))
thread6 = Thread(target=valider, args=('emails6', '6'))
thread7 = Thread(target=valider, args=('emails7', '7'))
thread8 = Thread(target=valider, args=('emails8', '8'))
thread9 = Thread(target=valider, args=('emails9', '9'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()


t = str(datetime.datetime.today())
print(t_, t)