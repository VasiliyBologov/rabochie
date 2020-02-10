import random
from threading import Thread

import os

def funct(inti):
    r1 = 0
    r2 = 0
    r3 = 0
    r0 = 0

    w = 0
    while w < 100:
        rand = random.randint(0, 3)
        #print(str(rand) + ";  ", end='')
        if rand == 0:
            r0 += 1
        elif rand == 1:
            r1 += 1
        elif rand == 2:
            r2 += 1
        elif rand == 3:
            r3 += 1
        else:
            print("ne moget bit'")

        w += 1
    print("\n\n Potoc " + str(inti) +":\n 0 - " + str(r0) + "\n 1 - " + str(r1) + "\n 2 - " + str(r2) + "\n 3 - " + str(r3))
    eg = 0
    while eg < 100:
        eg += 1
        file1 = open(os.getcwd() + "/123/123filetest" + str(inti), "a")
        file1.write(str(eg) + "\n")
        file1.close()
    print("end potoc " + str(inti))

"""
threed1 = Thread(target=funct, args=(1,))
threed2 = Thread(target=funct, args=(2,))
threed3 = Thread(target=funct, args=(3,))
threed4 = Thread(target=funct, args=(4,))


threed1.start()
threed2.start()
threed3.start()
threed4.start()

threed1.join()
threed2.join()
threed3.join()
threed4.join()"""

threads = list()
for index in range(20000):
    x = Thread(target=funct, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
        thread.join()
