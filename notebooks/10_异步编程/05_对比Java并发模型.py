"""
异步编程 · 知识点 5/5：对比 Java 的并发模型

Python 的 asyncio 是单线程"协作式并发"：只有一个线程在跑，协程之间靠主动 await 让出控制权，
不会像多线程那样在任意一行代码中间被系统随时打断，所以不用加锁就能避免很多并发 bug。
适合"等待型"任务（网络请求、数据库查询、文件 IO）：等待的时候让出控制权给别的协程，CPU 没有被浪费。
不适合"计算型"任务（大量数值计算）：因为只有一个线程，算得慢的协程会一直占着，其他协程根本没机会跑。

对比 Java：
- Java 的 Thread / ExecutorService 是真正的多线程，能利用多核 CPU，但要自己处理线程安全（锁、并发集合）
- Java 的 CompletableFuture 在"组合多个异步结果"这点上跟 asyncio.gather 思路类似，但底层还是线程池
- 更贴近的类比其实是 JavaScript 的 async/await + Promise：都是单线程事件循环，写法也几乎一样

Python 还有个著名的 GIL（全局解释器锁）：同一时刻只有一个线程能执行 Python 字节码，
这也是为什么 Python 处理"计算密集型"任务更常用多进程（multiprocessing）而不是多线程。
"""

import asyncio
import time


async def io_bound_task(name, delay):
    # 模拟"等待型"任务，比如等一个网络请求返回
    print(f"{name} 发起请求，等待响应")
    await asyncio.sleep(delay)
    print(f"{name} 收到响应")


async def io_bound_demo():
    # 三个"等待型"任务并发执行：总耗时约等于最慢的那一个，而不是三个相加
    start = time.time()
    await asyncio.gather(
        io_bound_task("请求A", 1),
        io_bound_task("请求B", 1),
        io_bound_task("请求C", 1),
    )
    print(f"三个等待型任务并发耗时：{time.time() - start:.1f} 秒（约等于最慢的一个，而不是三个相加）")


def demo_why_asyncio_fits_io():
    print("--- asyncio 为什么适合 IO 等待型任务，而不是计算密集型任务 ---")
    asyncio.run(io_bound_demo())
    print("如果这里换成纯计算（比如循环算 10 亿次），asyncio 不会有任何加速效果——")
    print("因为计算过程中没有 await 这种主动让出控制权的点，事件循环根本没机会切到别的协程")


if __name__ == "__main__":
    demo_why_asyncio_fits_io()
