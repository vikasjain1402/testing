from log import logDecorator
import os
from killprocess import  kill_process_fun

@logDecorator
def shutdown(*args,**kwargs):

    time=kwargs.get('shutdownDelay',1)
    kill_process_fun()
    password=os.environ['SUDO_PASSWORD']
    command=f"shutdown -h {time}"
    os.system(f"echo {password} |{command}")

if __name__=="__main__":
    shutdownDelay=2
    shutdown(shutdownDelay=shutdownDelay,
               log_message=f"shutdwon from main file in {shutdownDelay} minutes")
