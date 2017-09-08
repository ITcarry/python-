#coding:gbk
import time
import sys
import threading

def calc_time(func):
    def _deco(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        cost_time = time.time() - begin_time
        print 'do %s cost time: %s' % (func, cost_time)
        return ret
    return _deco

class FuncThread(threading.Thread):
    
    def __init__(self, func, *args, **kwargs):
        super(FuncThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.finished = False
        self.result = None

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)
        self.finished = True

    def is_finished(self):
        return self.finished

    def get_result(self):
        return self.result


def do_in_thread(func, *args, **kwargs):
    ft = FuncThread(func, *args, **kwargs)
    ft.start()
    return ft

def movie():
    print "我在看速8! \n"
    time.sleep(3)

def eating():
    print "我在吃饭. \n"
    time.sleep(1)

def call():
    print "我在打电话! \n"
    time.sleep(0.5)

@calc_time  
def test():   
    thread_objs = []
    
    for func1 in [movie,eating,call]:
        thread_obj = do_in_thread(func1)
        thread_objs.append(thread_obj)
    
    for thread_obj in thread_objs:
        thread_obj.join()
        
test()