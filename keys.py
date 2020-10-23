#!/usr/bin/python3
from log import logDecorator

import sys
@logDecorator
def keysmodify(*args,**kwargs):
    import os
    os.system('xmodmap -e "keycode 108 =less"')
    os.system('xmodmap -e "keycode 135 =comma"')


if __name__=="__main__":
    keysmodify(log_message="key modify script ran")