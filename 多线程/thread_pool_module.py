#coding:gbk

import time
from concurrent.futures import ThreadPoolExecutor

"""
POOL_SIZE:�̳߳صĴ�С
TEST_COUNT��Ҫ��ѹ��Ĵ���
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
�����������κ�ѹ��
�����ѹ��ű�
Ҫ�����ǣ�
1�����¶���Ҫ��������
2�� дһ�³�ʶ�̳߳ش�С��ѹ�Ⲣ��
"""