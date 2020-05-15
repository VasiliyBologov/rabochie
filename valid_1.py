
import socket
import smtplib
import dns.resolver
import re


def validmailvaso(emailinput):
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

	# Assume 250 as Success
	if code == 250:
		print('Success')
	else:
		print('Bad')


validmailvaso('dthompson@tableau.com')


