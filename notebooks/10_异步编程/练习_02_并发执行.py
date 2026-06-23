"""
异步编程 · 练习 2/5：并发执行多个协程
对应知识点 02_并发执行.py
"""
import asyncio


async def exercise_3():
    """
    第3题：asyncio.gather 并发执行

    写一个协程 download(filename, seconds)：打印 f"{filename} 下载中"，
    await asyncio.sleep(seconds)，打印 f"{filename} 下载完成"

    用 asyncio.gather() 并发执行三个下载任务：
    download("file1.txt", 1) / download("file2.txt", 1) / download("file3.txt", 1)
    用 time 统计总耗时，期望大约 1.0 秒（而不是顺序执行的 3.0 秒）
    """
    # 在这里写你的代码
    pass


async def exercise_4():
    """
    第4题：asyncio.create_task 提前调度

    写一个协程 process(name, seconds)，逻辑跟前面类似
    用 asyncio.create_task() 分别创建两个任务：process("任务A", 3) 和 process("任务B", 1)
    创建完之后先打印一行 "两个任务已提交"，再分别 await 这两个 task 拿到结果

    要验证的点：从打印顺序能看出任务是"创建即开始跑"的，不是等到 await 才开始
    （"任务B" 耗时短，会先打印完成，即使代码里先 await 的是 task_a）
    """
    # 在这里写你的代码
    pass


async def exercise_5():
    """
    第5题：Task 对象状态

    用 asyncio.create_task() 创建一个耗时 1 秒的任务
    - 创建后立刻调用 task.done()，应该是 False
    - await 这个 task 之后，再调用 task.done()，应该是 True
    - 用 task.result() 取出结果并打印
    """
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    asyncio.run(exercise_3())
    print()
    asyncio.run(exercise_4())
    print()
    asyncio.run(exercise_5())
