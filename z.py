#!/usr/bin/python3

from sysupdate import systemupdateupgrade
from keys import keysmodify
from shutdown import shutdown
import sys,os
from pathlib import Path

helpfilepath=os.path.join(Path(__file__).resolve().parent,"help.txt")


if __name__=="__main__":
    args=sys.argv
    if ("--help" in args) or ("-h" in args) or (len(args)==1) or (len(args)>3): 
        with open (helpfilepath,'r') as f:
            print(f.read())
        
    elif not set(args[1:]).issubset(set(['--update','--keys','--shutdown'])):
        print("Invalid Inputs")
    else:
        if "--keys" in args:
            keysmodify(log_message="key Modify ran from z command")
        if "--update" in args:
            systemupdateupgrade(log_message="System update ran from z command")
        if "--shutdown" in args:
            shutdown(log_message="shutdown ran from z command")        
