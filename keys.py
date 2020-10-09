#!/usr/bin/python3
import os
os.system('xmodmap -e "keycode 108 =less"')
os.system('xmodmap -e "keycode 135 =comma"')


password="1@Million"

command="sudo -S apt update"
print("Executing Update...")
os.system(f"echo {password} |{command}")
print("Done\n\n")

command="sudo -S apt upgrade -y"
print("Executing Upgrade....")
os.system(f"echo {password} |{command}")
print("Done")