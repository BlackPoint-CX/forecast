#!/usr/bin/env python
import multiprocessing

import wget


def read_urls():
    with open('download.txt', mode='r') as f:
        lines = f.readlines()
    return lines


def download(url):
    wget.download(url=url)


lines = read_urls()
print(lines)

pool = multiprocessing.Pool(5)
rel = pool.map(download, read_urls())
print(rel)



import subprocess
cmd = 'wget -O name url'
subprocess.call(cmd,shell=True)
