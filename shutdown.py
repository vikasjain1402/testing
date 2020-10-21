from log import logDecorator
import os

@logDecorator
def shutdown(*args,**kwargs):
    time=kwargs.get('shutdownDelay',1)
    password=os.environ['SUDO_PASSWORD']
    command=f"sudo shutdown -h {time}"
    #os.system(f"echo {password} |{command}")

if __name__=="__main__":
    shutdownDelay=2
    shutdown(shutdownDelay=shutdownDelay,
               log_message=f"shutdwon from main file in {shutdownDelay} minutes")
