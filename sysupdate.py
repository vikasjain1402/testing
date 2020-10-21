#!/usr/bin/python3
import os
from log import logDecorator

@logDecorator
def systemupdateupgrade(*args,**kwargs):
    password=os.environ['SUDO_PASSWORD']
    command="sudo -S apt update"
    print("taking password= ",password)
    print("Executing Update...")
    os.system(f"echo {password} |{command}")
    print("Done\n\n")
    command = "sudo -S apt upgrade -y"
    print("Executing Upgrade....")
    os.system(f"echo {password} |{command}")
    print("Done")



if __name__=="__main__":
    systemupdateupgrade(log_message="update upgrade script ran")