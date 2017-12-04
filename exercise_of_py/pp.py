

import multiprocessing as mul


def proc1(pipe):
    pipe.send('hello')
    print('proc1 send',pipe.recv())


def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello,too')


pipe = mul.Pipe()

p1 = mul.Process(target=proc1,args=(pipe[0],))
p2 = mul.Process(target=proc2,args=(pipe[1],))

p1.start()
p2.start()
p1.join()
p2.join()

