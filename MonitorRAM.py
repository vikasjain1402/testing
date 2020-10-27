import os
from time import sleep
from copy import copy
from colorama import Back ,Fore


def printchart(array1,noofrows=10,screenwidth=os.get_terminal_size().columns):
    array=copy(array1)
    digits=len(str(max(array)))

    for i in range(len(array)):
        array[i]=int(array[i]/10**(digits-1))

    array.extend([0 for _ in range(noofrows-len(array))])

    print("RAM Uilization")
    print("-"*screenwidth)
    count = 0
    for value in array:
        screen=int(screenwidth/10*max(array))
        mulfactor=int(screen/max(array))
        if count==0:
            format=Fore.BLUE+f"{chr(9608)*value*mulfactor} {value}0%"
        else:
            format = Fore.GREEN+ f"{chr(9608) * value * mulfactor} {value}0%"

        print(format)
        count+=1
    print("-" * screenwidth)


from collections import deque
li = deque()

import subprocess
try:
    while True:
        from os import system
        system('clear')
        a = subprocess.run(['cat', '/proc/meminfo'], capture_output=True, text=True)
        desireddata = {}
        list = a.stdout.split("\n")
        for l in list[0:3]:
            desireddata[l.split(":")[0]] = int(l.split(" ")[-2].split(" ")[0])
        width = int(os.get_terminal_size().columns) - 40
        used = desireddata['MemTotal'] - desireddata['MemAvailable']
        usedpercentage = int(used * 100 / desireddata['MemTotal'])
        if len(li)<10:
            li.appendleft(usedpercentage)
        else:
            li.pop()
            li.appendleft(usedpercentage)
        printchart(li)
        sleep(2)

except KeyboardInterrupt:
    print(chr(9608))

