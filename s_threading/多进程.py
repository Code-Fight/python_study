# Author zfCode
import multiprocessing
import time

def run(name):
    print("running ",name)


if __name__ == '__main__':
    p = multiprocessing.Process(target=run,args=("p1",))
    p.start()