#coding:gbk

import time
from concurrent.futures import ThreadPoolExecutor

t = ThreadPoolExecutor(50)  #50个线程并发


def test():
    time.sleep(1)
    print '我做了这件事情\n'
    
    
def func():
    for i in range(100):
        t.submit(test)
        
func()