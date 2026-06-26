"""
异步编程 · 练习 1/5：协程基础
对应知识点 01_协程基础.py
"""
import asyncio
import time


async def fetch(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)
    return f"{name} 完成"

async def exercise_1():
    """
    第1题：协程对象与执行时机

    写一个协程函数 fetch(name, seconds)：
    - 打印 f"{name} 开始"
    - await asyncio.sleep(seconds)
    - 返回 f"{name} 完成"

    测试步骤：
    1. 调用 fetch("订单", 1)，不要 await，先打印它的类型，验证此时函数体还没真正执行
       （应该打印不出 "订单 开始"，因为协程对象还没交给事件循环）
    2. 再用 await 把这个协程对象真正执行起来，打印返回值
       期望输出：
       <class 'coroutine'>
       订单 开始
       订单 完成
    """
    # 在这里写你的代码
    f = fetch("订单", 1)
    print(type(f))
    result = await f    # await 会返回协程的返回值，要用变量接住
    print(result)

async def exercise_2():
    """
    第2题：await 的顺序执行

    写两个协程：login(name, seconds) 和 send_email(name, seconds)，逻辑跟 fetch 类似
    （打印开始 -> await asyncio.sleep -> 打印完成）

    在 exercise_2 里用 time 统计总耗时：按顺序 await login("Tom", 1) 再 await send_email("Tom", 1)
    期望输出大约耗时 2.0 秒（因为是顺序执行，没有并发）
    """
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    asyncio.run(exercise_1())