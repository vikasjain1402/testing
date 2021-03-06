#!/usr/bin/python3
import os
import shutil
import sys
result=shutil.disk_usage('/')

def size_human_readable(size):
    for i in ['B','KB','MB','GB','TB','EB','ZB']:
        if abs(size)<1024:
            return "%3.2f %s"%(size,i)
        size=size/1024
    return size+ i


def size_of_folder(path):
    size=0
    for i,_,k in os.walk(path):
        for l in k:
            file_path=os.path.join(i,l)
            try:
                a=os.path.getsize(file_path)
                if a>1024*1024*1024:
                    print("File Size > 1GB :",i ,file_path, size_human_readable(a))
                if a > result.total:
                    print("Ignoring Virtual memory :",i ,file_path, size_human_readable(a))
                else:
                    size=size+a
            except:
                pass
            print(size_human_readable(size), end="\r")
    return(size)





if __name__=='__main__':

    path = sys.argv[1]
    while True:

        if os.path.exists(path)==True:
            print("valid path")
            print('Size of ',path,'=',size_human_readable(size_of_folder(path)))
            break
        else:
            print("invalid path")
            path = input("Please enter Path of the folder e.g /home/vikas/Desktop/   =")

    print("Bye")

