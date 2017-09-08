#coding:gbk

import time
from concurrent.futures import ThreadPoolExecutor

"""
POOL_SIZE:线程池的大小
TEST_COUNT：要做压测的次数
"""

POOL_SIZE = 100
TEST_COUNT = 1000

thread_pool = ThreadPoolExecutor(POOL_SIZE)


def need_to_do():
    time.sleep(3)
    print 'i am doing run func'


def run(count=100):
    for i in range(count):
        thread_pool.submit(need_to_do)


if __name__=="__main__":
    run(TEST_COUNT)
    
    
    
"""
工作场景：任何压测
万金玉压测脚本
要做的是：
1：重新定义要做的事情
2： 写一下初识线程池大小和压测并发
"""