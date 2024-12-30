import time

# def func():
#     print("我爱黎明")
#     time.sleep(2) #让当前的线程处于阻塞状态，cpu是不为我工作的
#     print("我真哎黎明")
#
# if __name__ == '__main__':
#     func()

#input()程序也是处于阻塞状态
# requests.get(url)在网络请求前返回数据之前，程序也是处于阻塞状态的
#  一般情况下，当程序处于IO操作的时候，可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 在宏观上，我们能看到的其实是多个任务一起在执行
# 多任务异步操作

# 上方所讲的一切，都是在单线程的条件下
import asyncio
import time

# async def func():
#     print("你好啊，我叫赛利亚")

# if __name__ == '__main__':
#     g = func()
#     asyncio.run(g)

# async def func1():
#     print("你好啊，我叫潘金莲")
#     # time.sleep(3) #当程序出现了同步操作的时候，异步就中断了 requests.get
#     await asyncio.sleep(3)
#     print("你好啊，我叫潘金莲")
#
# async def func2():
#     print("你好啊，我叫王坚果")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊，我叫王建国")
#
# async def func3():
#     print("你好啊，我叫李雪琴")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好啊，我叫李雪琴")
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#
#     t2 = time.time()
#     print(t2-t1)

# async def func1():
#     print("你好啊，我叫潘金莲")
#     # time.sleep(3) #当程序出现了同步操作的时候，异步就中断了 requests.get
#     await asyncio.sleep(3)
#     print("你好啊，我叫潘金莲")
#
# async def func2():
#     print("你好啊，我叫王坚果")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好啊，我叫王建国")
#
# async def func3():
#     print("你好啊，我叫李雪琴")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好啊，我叫李雪琴")
#
# async def main():
#     # await asyncio.gather(func1(), func2(), func3())
#       tasks = [func1(), func2(), func3()]
#       python3.8以后使用下面方法
#       tasks = [ asyncio.create_task(func1()),
#                 asyncio.create_task(func2()),
#                 asyncio.create_task(func3())
#       ]
#     # await asyncio.gather(*tasks)
#       await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2-t1)

# 在爬虫领域的作用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2) #网络请求
    print("下载完成")

async def main():
    urls = [
        "https://www.baidu.com",
        "https://www.bilibili.com",
        "https://www.163.com",
    ]
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    # tasks = [asyncio.create_task(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())