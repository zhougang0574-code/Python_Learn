"""
异步编程 · 练习 5/5：对比 Java 并发模型 / IO 并发收益实验
对应知识点 05_对比Java并发模型.py
"""
import asyncio
import time


async def exercise_10():
    """
    第10题：IO 并发收益实验

    写一个协程 call_api(name, seconds)：模拟一次网络请求
    - 打印 f"{name} 请求中"
    - await asyncio.sleep(seconds)
    - 打印 f"{name} 响应完成"

    分别用两种方式跑 call_api("接口A", 1) / call_api("接口B", 1) / call_api("接口C", 1)：
    1. 顺序 await 三个协程，统计耗时（期望约 3.0 秒）
    2. 用 asyncio.gather 并发跑三个协程，统计耗时（期望约 1.0 秒）

    最后打印两种方式的耗时对比，直观感受"IO 等待型任务用 asyncio 并发能带来多大收益"
    """
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    asyncio.run(exercise_10())
