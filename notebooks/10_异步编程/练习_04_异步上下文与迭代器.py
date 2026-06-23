"""
异步编程 · 练习 4/5：异步上下文管理器与异步迭代器
对应知识点 04_异步上下文与迭代器.py
"""
import asyncio


async def exercise_8():
    """
    第8题：自定义异步上下文管理器

    写一个类 AsyncDBConnection：
    - __aenter__：打印 "连接数据库"，await asyncio.sleep(0.1)，返回 self
    - __aexit__：await asyncio.sleep(0.1)，打印 "关闭数据库连接"，return False

    用 async with AsyncDBConnection() as conn: 包一段代码，块内打印 "执行查询中"
    """
    # 在这里写你的代码
    pass


async def exercise_9():
    """
    第9题：异步生成器与 async for

    写一个异步生成器 fetch_pages(total)：
    - 循环 range(total)
    - 每次先 await asyncio.sleep(0.1)（模拟翻页请求要等一下）
    - yield f"第 {i+1} 页数据"

    用 async for page in fetch_pages(3): 逐页打印
    期望输出：
    第 1 页数据
    第 2 页数据
    第 3 页数据
    """
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    asyncio.run(exercise_8())
    print()
    asyncio.run(exercise_9())
