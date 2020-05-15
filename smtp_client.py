import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'answer@xorai.tech'))
msg['From'] = email.utils.formataddr(('Author', 'answer@xorai.tech'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP()
server.set_debuglevel(True) # show communication with the server
try:
    server.connect('127.0.0.1', 1025)
    server.sendmail('answer@xorai.tech', ['answer@xorai.tech'], msg.as_string())
finally:
    server.quit()
