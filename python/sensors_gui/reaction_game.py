#!/usr/bin/python
from time import perf_counter, sleep
from random import random

while(True):
    print('Get Ready', flush=True)
    sleep(random()*5+1)
    print('Go', flush=True)
    start = perf_counter();
    input()
    end = perf_counter()
    print(f' you reacted in {(end-start)*100:.0f} milliseconds.\n', flush=True)
    break
