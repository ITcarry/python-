

import Queue
import time

q = Queue.Queue()

for i in range(10):
    q.put(i)
    
while not q.empty():
    print q.get()
    print q.empty()
    time.sleep(0.5)