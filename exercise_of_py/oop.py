#!/usr/bin/env python
# coding = utf-8
import os
import threading
import time


def doChore():
    time.sleep(5)


class BoothThread(threading.Thread):
    def __init__(self, tid, monitor):
        self.tid = tid
        self.monitor = monitor
        threading.Thread.__init__(self)

    def run(self):
        while True:
            monitor['lock'].acquire()
            if monitor['tick'] != 0:
                monitor['tick'] -= 1
                print(self.tid,':now left:',monitor['tick'])
                doChore()
            else:
                print('Thread_id',self.tid,' no more tickets')
                os._exit(0)
            monitor['lock'].release()
            doChore()

monitor = {'tick': 100, 'lock': threading.Lock()}


for k in range(10):
    new_thread = BoothThread(k,monitor=monitor)
    new_thread.start()
