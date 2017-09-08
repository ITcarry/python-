#coding:utf-8

import time

def handle_timeout(func,timeout,*args,**kwargs):
    
    interval = 1
    if type(timeout) == tuple:
        timeout,interval = timeout
    ret = None
    while timeout > 0:
        t = time.time()
        rst = func(*args,**kwargs)
        if rst:
            break
        time.sleep(interval)
        timeout -= time.time() - t
        return rst
    
    def foo(m):
        time.sleep(s)
        return 1
    
rt = handle_timeout(fii,60,'haha')
#rt = handle_timeout(fii,(60,2),'haha')
print rt