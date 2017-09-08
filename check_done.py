#coding:gbk

import time 
import os


FILE_PATH = r'c:\Users\lenovo\Desktop\finish'

def check_file_exist(file_name):
    return os.path.exists(file_name)

def handle_timeout(func,timeout,*args,**kwargs):
    '''
    func:������
    timeout:��ʱʱ��
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
    
    
    
    '''��һ����֮�ڼ���������Ƿ���finish����һ���ļ�������У�����True��
    ���û�У�������飬ֱ����ʱ
    '''
    
    print handle_timeout(check_file_exist,60,FILE_PATH)