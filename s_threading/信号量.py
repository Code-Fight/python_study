# Author zfCode
import threading
import time

# 应用场景 线程池 连接池 不做计数 但是控制可用的总线程数量  来对程序实现计算机资源利用的控制

def run(num):
    semaphore.acquire()
    # print("num ",num)
    time.sleep(1)
    print("run the thread:%s\n"%num)
    semaphore.release()

semaphore = threading.BoundedSemaphore(5)
for i in range(20):
    t1 = threading.Thread(target=run, args=(i,))
    t1.start()

while threading.active_count() != 1:
    pass
else:
    print("all done...")





