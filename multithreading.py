## Multithreading 
## when to multi threading 
##I/O bond tasks(file operation)
##Concurrent executions

import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"number:{i}")
        
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")   


## create two threads
t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)

t=time.time()     
## start the thread
t1.start()
t2.start()

##wit for the thread to complete  
t1.join()
t2.join()   

ft=time.time() - t 

print(ft)       