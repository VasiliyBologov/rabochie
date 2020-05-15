
host = 'smtp.gmail.com'
passw = 587


from telnetlib import Telnet
tn = Telnet('smtp.gmail.com', 587)   # connect to finger port
tn.write('OPEN\r\n')
print(tn.read_all())