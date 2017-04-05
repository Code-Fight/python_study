# Author zfCode

import threading
import time

def run(name, sleep):

    print("running ", name)
    time.sleep(sleep)
    print(name, "done...")

# t1 = threading.Thread(target=run, args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
#
# t1.start()
# t2.start()

# for i in range(50):
#     t=threading.Thread(target=run, args=("t-%s"%i,))
#     t.start()

# 实验 join 相当于别的语言wait
# t1 = threading.Thread(target=run, args=("t1",2,))
# t2 = threading.Thread(target=run, args=("t2",2,))
# t1.start()
# t1.join()
# t2.start()
# print("all dong...")

# 实验守护线程 主线程不会等待守护线程执行完毕才结束 守护线程的重要性比较低
for i in range(50):
    t=threading.Thread(target=run, args=("t-%s"%i, 2,))
    # t.setDaemon(True)
    t.setDaemon(True)
    t.start()

print("all dong...")




