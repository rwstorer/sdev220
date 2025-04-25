from os import getpid
import multiprocessing as mp
import random
from datetime import datetime
from time import sleep

def mp_demo(proc_num):
    print("process id:", getpid(), ". Proc num", proc_num)

if __name__ == "__main__":
    for i in range(0,3):
        num_seconds = random.random()
        print(num_seconds)
        p = mp.Process(target=mp_demo, args=(i,))
        p.start()
        p.join()
        sleep(num_seconds)
        print(datetime.now())
