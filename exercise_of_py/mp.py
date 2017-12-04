#!/usr/bin/env python
# codint = utf-8


import multiprocessing
import os


def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()


print('Main', os.getpid())

# record = []
# lock = threading.Lock()
# for i in range(5):
#     thread = threading.Thread(target=worker, args=('thread', lock))
#     thread.start()
#     record.append(thread)
#
# for thread in record:
#     thread.join()

# record = []
# lock = multiprocessing.Lock()
#
# for i in range(5):
#     process = multiprocessing.Process(target=worker, args=('process', lock))
#     process.start()
#     record.append(process)
#
# for process in record:
#     process.join()

record = []
lock = multiprocessing.Lock()
for i in range(5):
    process = multiprocessing.Process(target=worker,args=('process',lock))
    process.start()
    record.append(process)

for process in record:
    process.join()
