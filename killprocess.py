import subprocess
def kill_process_fun(processes=None):
    '''
    :param processes: list desfault=  ['chrome','vscode','firefox','spyder','libr',"pycharm"]
    :return: None
    '''
    if processes is None:
        processes=['chrome','vscode','firefox','spyder','libr',"pycharm"]
    a=subprocess.run(['ps','-aux'],text=True,capture_output=True)
    lines=a.stdout.split("\n")
    pr_id=[]
    for line in lines:
        for item in line.split(" "):
            for process in processes:
                if process in item:
                    pr_id.append(line.split(" ")[7])
                    print(process,line.split(" ")[7])

    for id in pr_id:
        a=subprocess.run(['kill' ,id],capture_output=True,text=True)
        if a.stderr =="":
            print(a.stderr)

if __name__=="__main__"  :
    kill_process_fun()
