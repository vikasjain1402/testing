import logging
import os
from pathlib import Path
logfilepath=os.path.join(Path(__file__).resolve().parent,"log.txt")
def logDecorator(func):
    def inner(*args,**kwargs):

        log_message=kwargs.get('log_message',f"NO message received from {__name__}")

        logging.basicConfig(level=logging.DEBUG,
                            filename=logfilepath,
                            filemode='a',
                            format='%(levelname)s : %(asctime)s : %(message)s')
        loger=logging.getLogger()
        loger.setLevel(logging.DEBUG)
        loger.debug(log_message)
        a=func(*args,**kwargs)
   
        return a
    return inner
