#!/usr/bin/python3
from time import sleep
import subprocess
import sys
from colorama import Back,Fore
try:
    while True:
        a=subprocess.run(['cat','/proc/meminfo'],capture_output=True,text=True)
        desireddata={}
        li=a.stdout.split("\n")
        for l in li[0:3]:
            desireddata[l.split(":")[0]]=int(l.split(" ")[-2].split(" ")[0])
        #used=desireddata['MemTotal']-desireddata['MemAvailable']-desireddata['MemFree']
        used=desireddata['MemTotal']-desireddata['MemAvailable']
        usedpercentage=used*100/desireddata['MemTotal']
        print(Fore.GREEN+"live RAM USAGE {2}{3}  {1:.4f} GB   {0:.2f}%".
            format(usedpercentage,
                    used/1024/1024,
                    chr(9608)*int(usedpercentage),    
                    "|"*(100-int(usedpercentage)),   
                    ),end="\r")
        sleep(2)
            
except KeyboardInterrupt:
    print(chr(9608))
    
