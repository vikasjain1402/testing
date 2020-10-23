import logging
import os
from pathlib import Path
logfilepath=os.path.join(Path(__file__).resolve().parent,"log.txt")

def logDecorator(func):
    def inner(*args,**kwargs):
        logging.basicConfig(level=logging.DEBUG,
                            filename=logfilepath,
                            filemode='a',
                            format='%(levelname)s : %(asctime)s : %(message)s')
        loger=logging.getLogger()
        loger.setLevel(logging.DEBUG)

        log_message = kwargs.get('log_message', "NO message received ")
        loger.debug(f"{log_message} from Function :{func.__name__}")
        a=None
        try:
            a=func(*args,**kwargs)
        except Exception as err:
            loger.debug(f"Error :.....{err}")
        return a
    return inner
