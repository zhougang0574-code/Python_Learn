"""
异步编程 · 知识点 1/5：协程基础
- async def 与协程对象
- asyncio.run() 作为程序入口
- await / asyncio.sleep（对比阻塞的 time.sleep）

用 .py 脚本而不是 ipynb 写这一章，是因为 Jupyter notebook 本身已经在运行一个事件循环了
（管理 cell 执行用的），这时候再调 asyncio.run() 会报错：
    RuntimeError: asyncio.run() cannot be called from a running event loop
notebook 里要绕过这个问题得用"顶层 await"这种 Jupyter 专属写法，容易造成"为什么脚本里不能这样写"的误解。
普通 .py 脚本没有这个问题，asyncio.run() 才是标准、通用的写法——直接运行这个文件：python 01_协程基础.py
"""
import asyncio
import time


async def say_hello():
    print("Hello")
    return "done"


def demo_coroutine_object():
    print("--- 1. async def 定义的函数调用后返回协程对象，函数体不会立即执行 ---")
    coro = say_hello()
    print(type(coro))  # <class 'coroutine'>，这时 print("Hello") 还没真正执行
    # 协程对象必须交给事件循环才会真正跑起来，asyncio.run() 就是干这件事的
    result = asyncio.run(coro)
    print(result)  # done


async def main_demo():
    print("协程开始执行")
    return 42


def demo_asyncio_run():
    print("--- 2. asyncio.run()：创建事件循环、运行协程直到结束、关闭事件循环 ---")
    # 是"同步代码"进入"异步世界"的入口；一个程序里通常只在最外层调用一次，不要在协程内部再嵌套调用
    result = asyncio.run(main_demo())
    print(result)


async def task(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)  # await：等这个协程执行完，等待期间让出控制权，不是单纯的阻塞
    print(f"{name} 结束")


async def sequential_tasks():
    await task("A", 1)
    await task("B", 1)


def demo_await_and_sleep():
    print("--- 3. await 与 asyncio.sleep（对比 time.sleep）---")
    # time.sleep() 会让整个线程（包括事件循环本身）卡住，阻塞期间什么协程都跑不了
    # asyncio.sleep() 是"协程版"睡眠：挂起当前协程的同时把控制权交还给事件循环
    start = time.time()
    asyncio.run(sequential_tasks())
    print(f"耗时：{time.time() - start:.1f} 秒")  # 大约 2 秒，因为是顺序 await，没有并发


if __name__ == "__main__":
    demo_coroutine_object()
    print()
    demo_asyncio_run()
    print()
    demo_await_and_sleep()
