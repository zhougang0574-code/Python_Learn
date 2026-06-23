"""
异步编程 · 练习 3/5：超时控制与异常处理
对应知识点 03_超时与异常.py
"""
import asyncio


async def exercise_6():
    """
    第6题：asyncio.wait_for 超时控制

    写一个协程 slow_query()：await asyncio.sleep(5)，返回 "查询结果"
    用 asyncio.wait_for(slow_query(), timeout=2) 设置 2 秒超时
    捕获 asyncio.TimeoutError，打印 "查询超时"
    """
    # 在这里写你的代码
    pass


async def exercise_7():
    """
    第7题：gather 的异常处理与 return_exceptions

    写一个协程 validate(n)：
    - 如果 n == 2，raise ValueError(f"第 {n} 项校验失败")
    - 否则 await asyncio.sleep(0.1)，返回 n

    测试两种情况：
    1. 用 asyncio.gather(validate(1), validate(2), validate(3)) 默认方式调用，
       用 try/except 捕获 ValueError，打印捕获到的异常信息
    2. 用 asyncio.gather(validate(1), validate(2), validate(3), return_exceptions=True)，
       打印结果列表，期望：[1, ValueError('第 2 项校验失败'), 3]
    """
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    asyncio.run(exercise_6())
    print()
    asyncio.run(exercise_7())
