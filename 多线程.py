#进程，线程
# 进程是一个资源单位，每一个进程至少要有一个线程
# 线程是一个执行单位
from threading import Thread


# 启动每一个程序默认都会有一个主线程
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ == '__main__':
#     func()
#     for i in range(1000):
#         print("main",i)

from threading import Thread
def func(name):
    for i in range(1000):
        print(name,i)

# if __name__ == '__main__':
#     T = Thread(target=func)#创建线程并安排工作
#     T.start() #多线程状态为开始工作状态，具体执行时间由cpu决定
#     for i in range(1000):
#         print("main",i)

# class MyThread(Thread):
#     def run(self):   #固定的  --> 当线程被执行的时候，被执行的就是run()
#         for i in range(100):
#             print("子线程",i)

if __name__ == '__main__':
    t1 = Thread(target=func,args=("周杰伦",))
    # t.run() #方法的调用了，--> 单线程？？？
    t1.start() #开启线程

    t2= Thread(target=func,args=("王力宏",))
    t2.start()
    for i in range(100):
        print("主线程",i)
