#coding:gbk

import time
from concurrent.futures import ThreadPoolExecutor

t = ThreadPoolExecutor(50)  #50���̲߳���


def test():
    time.sleep(1)
    print '�������������\n'
    
    
def func():
    for i in range(100):
        t.submit(test)
        
func()