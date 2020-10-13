#!/usr/bin/python3
import os
import sys
def find_text_in_file_in_path(path,text,ext):

    os.chdir(path)
    for i,_,k in os.walk(path):
        for l in k:
                filepath=os.path.join(i,l)
                try:
                    if ext==filepath.split(".")[-1]:
                        f=open(filepath,"r",)
                        print(l,end="                                                     \r")
                    else:
                        continue
                    r=f.readlines()
                except Exception:
                    print("...Excluding :",l)
                else:
                    for m in r:
                        if text.lower() in m.lower():
                            print(i," $$ ",l)
                            inp=input("press 'n' to exit")
                            if inp=='N' or inp=='n'  :
                                print ("Thanks!!")
                                return
                            else:
                                break

if __name__=="__main__":
    text=input("Enter file text or phrase you want to Search : ")
    while True:
        path=sys.argv[1]
        ext=sys.argv[2]
        if os.path.exists(path)==True:
            find_text_in_file_in_path(path,text,ext)
            print("bye")
            break

