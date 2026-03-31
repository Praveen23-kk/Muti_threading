## Process that run in parallel
## CPU-Bound tasks
##parallel executions use multiply core of the cpu

import multiprocessing

import time

def sqr_num():
    for i in range (5):
        time.sleep(5)
        print(f"Square:{i*i}")
        
def cube_num():
    for i in range (5):
        time.sleep(1.5)
        print(f"Cube:{i*i*i}")        

if __name__=="__main__":
    
    p1=multiprocessing.Process(target=sqr_num)      
    p2=multiprocessing.Process(target=cube_num)  
    t=time.time()

            
            
    ## start the process
    p1.start()
    p2.start()       

    ##wait for the process to complete
    p1.join()
    p2.join()

    ft=time.time()-t
    print(ft)
    
    

    
           
        
