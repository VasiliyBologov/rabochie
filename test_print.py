#hi im VASO

import time
import sys

def esc(code):
    return f'\033[{code}m'



spisok = {0, 1, 3, 4, 7, 9, 21, 30, 31, 32, 33, 34, 34, 36, 40, 41, 42, 43, 44, 45, 46, 47, 51, 52, 90, 91, 92, 93, 94, 95, 96, 97}





for sp in spisok:
    print(sp, end =" ")
    print('\x1b['+ str(sp) +'m' + "Привет " + '\033[0m' + str(sp) + " " + '\033[' + str(sp) +'m' + "Привет" + '\033[0m')



print(f'\033[41;93;1m' + "Привет" + '\033[0m')
print('\x1b[31m' + "Привет" + '\033[0m')
print("Привет")


print('\nBefore the loop\n')

for i in range(1, 101):
    time.sleep(0.05)
    sys.stdout.write("\r[ {}{} ] {}%".format('#' * i, '*' * (100-i), i))
    # sys.stdout.flush()
print()

print('\nAfter the loop')
