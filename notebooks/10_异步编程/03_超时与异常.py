"""
异步编程 · 知识点 3/5：超时控制与异常处理
- asyncio.wait_for()：超时自动取消
- gather 默认遇到异常会立刻往外抛
- gather(return_exceptions=True)：异常不抛出，放进结果列表里
"""
import asyncio


async def slow_task():
    await asyncio.sleep(3)
    return "完成"


async def wait_for_demo():
    try:
        # wait_for(协程, timeout)：超过 timeout 秒还没完成就抛出 asyncio.TimeoutError，并取消这个任务
        result = await asyncio.wait_for(slow_task(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("超时了")


def demo_wait_for():
    print("--- 1. asyncio.wait_for()：超时控制 ---")
    asyncio.run(wait_for_demo())


async def risky(n):
    if n == 2:
        raise ValueError(f"任务 {n} 出错了")
    await asyncio.sleep(0.1)
    return n


async def gather_exception_demo():
    # 默认情况下，gather 里只要有一个协程抛异常，gather 本身就会立刻把这个异常往外抛
    try:
        await asyncio.gather(risky(1), risky(2), risky(3))
    except ValueError as e:
        print(f"捕获到：{e}")

    # return_exceptions=True：异常不会往外抛，而是把异常对象本身放进结果列表里，其他任务正常返回结果
    results = await asyncio.gather(risky(1), risky(2), risky(3), return_exceptions=True)
    print(results)  # [1, ValueError('任务 2 出错了'), 3]


def demo_gather_exceptions():
    print("--- 2. gather 的异常处理与 return_exceptions ---")
    asyncio.run(gather_exception_demo())


if __name__ == "__main__":
    demo_wait_for()
    print()
    demo_gather_exceptions()
