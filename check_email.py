

"""
Created on 11.05.2020


:author: Bologov V.A.
:email: vasiliybologov@gmail.com

"""
import os
import urllib.request as rq

spisca = ['vickistanley@americanmed.com', 'sarah-jane.king@medacsglobalgroup.com', 'mark.vesconte@nesgt.com', 'fabriziotravaglini@michaelpage.com', 'michaelbaier@michaelpage.com', 'lucasoggiam@michaelpage.com', 'javiertorre@michaelpage.com', 'gijsdelft@michaelpage.com', 'nilsrichter@michaelpage.com']



print(spisca)
"""# работает
import urllib.request as rq
emailinput="vasilii.b@xor.ai"
emailcheck=rq.urlopen(f'https://api.2ip.me/email.txt?email={emailinput}')
print(emailcheck.read())"""

i = 0
while i < len(spisca):


    emailinput = spisca[i]
    emailcheck = rq.urlopen(f'https://api.2ip.me/email.txt?email={emailinput}')
    print(spisca[i], end="")
    print(emailcheck.read())

    i += 1


