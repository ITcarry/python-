#coding:gbk

import time 
import os


FILE_PATH = r'c:\Users\lenovo\Desktop\finish'

def check_file_exist(file_name):
    return os.path.exists(file_name)

def handle_timeout(func,timeout,*args,**kwargs):
    '''
    func:函数名
    timeout:超时时间
    '''    
    
    interval = 1
    
    ret = None
    while timeout > 0:
        begin_time = time.time()
        ret = func(*args,**kwargs)
        if ret:
            break
        time.sleep(interval)
        timeout -= time.time() - begin_time
        
        
        
        return ret
    
    
    
    '''在一分钟之内检查桌面上是否有finish这样一个文件，如果有，返回True，
    如果没有，继续检查，直到超时
    '''
    
    print handle_timeout(check_file_exist,60,FILE_PATH)