"""
异步编程 · 知识点 2/5：并发执行多个协程
- asyncio.gather()：并发跑多个协程，等全部完成
- asyncio.create_task()：立刻提交给事件循环调度，不用等 await 才开始跑
- Task 对象常用方法：done() / result()
"""
import asyncio


async def task(name, delay):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 结束")
    return name


async def gather_demo():
    # gather(*协程)：把多个协程一起丢给事件循环并发执行，等全部完成后按"传入顺序"返回结果列表
    results = await asyncio.gather(task("A", 1), task("B", 1), task("C", 1))
    print(results)  # ['A', 'B', 'C']，是按参数顺序排的，不是谁先完成谁排前面


def demo_gather():
    import time
    print("--- 1. asyncio.gather()：并发执行 ---")
    start = time.time()
    asyncio.run(gather_demo())
    print(f"耗时：{time.time() - start:.1f} 秒")  # 大约 1 秒，因为三个任务是并发执行的


async def worker(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} 完成")
    return name


async def create_task_demo():
    # create_task()：把协程包装成一个 Task，立刻提交给事件循环开始调度执行，不用等 await 才开始跑
    t1 = asyncio.create_task(worker("A", 2))
    t2 = asyncio.create_task(worker("B", 1))
    print("两个任务已经创建，继续往下执行（这时 A、B 已经在后台跑了）")

    result1 = await t1  # 这里才是"等结果"，但任务从 create_task 那一刻就已经开始执行了
    result2 = await t2
    print(result1, result2)


def demo_create_task():
    print("--- 2. asyncio.create_task()：创建任务，立刻开始调度 ---")
    asyncio.run(create_task_demo())


async def task_object_demo():
    async def slow_worker():
        await asyncio.sleep(1)
        return "result"

    task_obj = asyncio.create_task(slow_worker())
    print(task_obj.done())  # False，刚创建还没完成
    result = await task_obj
    print(task_obj.done())  # True，完成了
    print(task_obj.result())  # result，拿到协程的返回值（跟 await task_obj 拿到的是同一个值）


def demo_task_object():
    print("--- 3. Task 对象常用方法：done() / result() ---")
    asyncio.run(task_object_demo())


if __name__ == "__main__":
    demo_gather()
    print()
    demo_create_task()
    print()
    demo_task_object()
