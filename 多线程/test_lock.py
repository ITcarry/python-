#coding:gbk

import threading
from threading import Lock


some_var = 0
lock = Lock()

class FuncThread(threading.Thread):
    
    def __init__(self, func, *params, **kwparams):
        threading.Thread.__init__(self)
        self.func = func
        self.params = params
        self.kwparams = kwparams
        self.result = None
        self.finished = False
    
    def run(self):
        self.result = self.func(*self.params, **self.kwparams)
        self.finished = True
    
    def get_result(self):
        return self.result
    
    def is_finished(self):
        return  self.finished

def do_in_thread(func, *params, **paramMap):
    ft = FuncThread(func, *params, **paramMap)
    ft.start()
    return ft


def add_some_var():
    lock.acquire()
    global some_var
    read_value = some_var
    print "当前全局变量的值： %d \n" %  read_value
    some_var = read_value + 1
    lock.release()
    print "加过后全局变量的值： %d\n" %  some_var


def do_add_in_thread():
    threads = []
    for i in range(50):
        t = do_in_thread(add_some_var)
        threads.append(t)
    for t in threads:
        t.join()
    print "预期some_var为50"
    print "实际结果是 %d" % (some_var,)


do_add_in_thread()