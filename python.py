import os
import time
import shutil

file_check=input("enter folder: ")
delete_time=int(input("Type how old the file should be to be deleted: "))
def file_delete(): 
    t=time.time()
    t2=int(t/86400)
    print(t2) 

    ctime = os.stat(file_check).st_ctime
    ctime2=int(ctime)
    ctime3=ctime2/86400
    print(ctime3)
    days=t2-ctime3
    print("days:", days)
    ti_c = os.path.getctime(file_check)
    c_ti = time.ctime(ti_c)
    print(c_ti)
    

    if days>delete_time:
        shutil.rmtree(file_check)
        print("File was deleted because it was older than thirty days.")
    else: 
        print("File was youger than thirty days so saved.")

file_delete()


    


   







