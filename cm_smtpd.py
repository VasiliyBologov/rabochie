import smtplib

import smtpd
remoteaddr = ('alt4.aspmx.l.google.com', 25)
s = smtpd.SMTPServer('localhost', remoteaddr)

print(s.connect())
