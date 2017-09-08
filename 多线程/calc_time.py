
import sys
import time


def calc_time(func):
    def _deco(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        cost_time = time.time() - begin_time
        print 'do %s cost time: %s' % (func, cost_time)
        return ret
    return _deco


@calc_time
def add(m, n):
    time.sleep(2)
    return m+n