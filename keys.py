#!/usr/bin/python3
import os
os.system('xmodmap -e "keycode 108 =less"')
os.system('xmodmap -e "keycode 135 =comma"')

<<<<<<< HEAD
password=os.environ['SUDO_PASSWORD']


command="sudo -S apt update"
=======
password = os.environ.get("root_password", "Password")
command = "sudo -S apt update"

print("taking password= ",password)
>>>>>>> 82dafa081812726e541d943510e9e8e8c1eb34ce
print("Executing Update...")
os.system(f"echo {password} |{command}")
print("Done\n\n")

command = "sudo -S apt upgrade -y"
print("Executing Upgrade....")
os.system(f"echo {password} |{command}")
print("Done")
