"""
异步编程 · 知识点 4/5：异步上下文管理器与异步迭代器
- async with：__aenter__ / __aexit__（对比第08章学的同步版 __enter__/__exit__）
- async for：配合异步生成器，每次取值都会自动 await
"""
import asyncio


class AsyncResource:
    # 异步上下文管理器要实现 __aenter__ / __aexit__（注意都要用 async def，内部也可以 await）
    # 用法和语义跟同步版完全一样，只是多了"异步"这一层
    async def __aenter__(self):
        print("异步获取资源")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(0.1)
        print("异步释放资源")
        return False


async def async_with_demo():
    async with AsyncResource() as res:
        print("使用资源中")


def demo_async_with():
    print("--- 1. async with：异步上下文管理器 ---")
    asyncio.run(async_with_demo())


async def async_range(n):
    # 异步生成器：函数里同时有 async def 和 yield，每产出一个值之前可以先 await 别的协程
    for i in range(n):
        await asyncio.sleep(0.1)  # 模拟"取下一个值之前要等一下"，比如真实场景里要发一次网络请求
        yield i


async def async_for_demo():
    # async for：专门用来迭代"异步迭代器/异步生成器"，每次取下一个值都会自动 await
    async for i in async_range(3):
        print(i)


def demo_async_for():
    print("--- 2. async for：异步迭代器 / 异步生成器 ---")
    asyncio.run(async_for_demo())


if __name__ == "__main__":
    demo_async_with()
    print()
    demo_async_for()
