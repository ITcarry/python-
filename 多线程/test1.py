import threading
import time
import utils

def test(file_name):
    time.sleep(3)
    print '3 second'
    f = open(file_name, 'w')
    ret = 'I love coding'
    f.write(ret)
    f.close()
    return ret


def wc():
    print 'go to wc'
    
    
ft = utils.do_in_thread(test,'ss.txt')
time.sleep(4)
print ft.is_finished()
print ft.get_result()