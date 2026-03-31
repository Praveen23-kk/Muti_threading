## MUltiprocessiing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor

import time

def sqr_num(num):
    time.sleep(2)
    return f"Square:{num*num}"

numbers=[1,4,5,6,7,8,4,7,12,23]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(sqr_num,numbers)
        
    for result in results:
        print(result)    