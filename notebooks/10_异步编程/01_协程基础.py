"""
异步编程 · 知识点 1/5：协程基础

直接运行这个文件：python 01_协程基础.py

为什么用 .py 而不是 .ipynb：
  Jupyter 自身就跑着一个事件循环，在里面再调 asyncio.run() 会报错：
  RuntimeError: asyncio.run() cannot be called from a running event loop
  .py 脚本没有这个问题，asyncio.run() 在这里才是标准写法。
"""
import asyncio
import time


# ─── 1. 为什么需要异步 ──────────────────────────────────────────────────────
#
# 场景：同时调三个接口，每个接口响应需要 1 秒。
#
# 同步写法（串行）：
#   等接口A → 等接口B → 等接口C，总耗时 3 秒
#
# 异步写法（并发）：
#   同时发出三个请求，等待期间不阻塞，总耗时约 1 秒
#
# asyncio 的核心思路：
#   只用一个线程，靠协程在 IO 等待时主动"让出控制权"来实现并发。
#   适合 IO 等待型任务（网络请求、数据库查询、文件读写）。
#   不适合 CPU 密集型计算——计算期间没有让出点，事件循环无法切换。


# ─── 2. 事件循环：单线程调度器 ─────────────────────────────────────────────
#
# 事件循环是一个不断轮询的调度器，决定"现在该跑哪个协程"。
# 它做的事类似于：
#
#   while 还有未完成的协程:
#       task = 找一个"现在可以继续跑"的协程
#       运行它，直到它遇到 await
#       把控制权交回给事件循环
#       等它 await 的东西完成了，再唤醒它继续跑
#
# 关键点：协程遇到 await 时，主动把控制权交出去。
#         事件循环趁这个空档去跑其他协程。
#         这叫"协作式并发"——协程自己让，不像线程那样被系统强制打断。


# ─── 3. async def 与协程对象：调用 ≠ 执行 ────────────────────────────────

async def fetch(name, seconds):
    print(f"{name} 开始")
    await asyncio.sleep(seconds)   # 挂起自己，把控制权交给事件循环
    return f"{name} 完成"


def demo_coroutine_object():
    print("=== 3. async def 与协程对象 ===")

    # 调用 async def 函数，只会返回一个"协程对象"，函数体一行都没跑
    coro = fetch("订单", 1)
    print(type(coro))   # <class 'coroutine'>

    # 此时 "订单 开始" 还没有被打印——协程对象必须交给事件循环才会真正执行
    print("此时函数体还没跑，'订单 开始' 还没打印")

    # asyncio.run(协程)：创建事件循环 → 跑这个协程直到结束 → 关闭事件循环
    # 这是在同步代码里启动异步世界的唯一入口
    result = asyncio.run(coro)
    print(result)   # 订单 完成


# ─── 4. asyncio.run()：同步代码进入异步世界的入口 ─────────────────────────
#
# asyncio.run(协程) 做了三件事：
#   1. 创建一个新的事件循环
#   2. 把协程丢进去跑，直到它结束
#   3. 关闭事件循环
#
# 重要规则：
#   asyncio.run() 只在最外层的"同步代码"里调用，通常只调一次。
#   不能在协程（async def）内部调 asyncio.run()——
#   因为协程已经跑在某个事件循环里了，再开一个新循环会报错：
#   RuntimeError: asyncio.run() cannot be called from a running event loop


def demo_asyncio_run():
    print("=== 4. asyncio.run() ===")
    result = asyncio.run(fetch("支付", 1))
    print(result)


# ─── 5. await：在协程内部驱动另一个协程 ──────────────────────────────────
#
# 在协程（async def）内部，驱动另一个协程用 await，不用 asyncio.run()。
# await 的意思：把这个协程交给"当前已有的事件循环"跑，跑完再继续我。
#
# 对比：
#   同步代码   →  协程：asyncio.run(协程)     ← 创建事件循环
#   协程       →  协程：await 协程             ← 借用已有的事件循环


async def checkout():
    print("开始结账流程")
    result = await fetch("结账-验库存", 1)   # await：协程内部驱动协程
    print(result)
    result2 = await fetch("结账-扣款", 1)
    print(result2)


def demo_await():
    print("=== 5. await ===")
    asyncio.run(checkout())   # 同步代码里用 asyncio.run()


# ─── 6. 完整执行流程（以 demo_await 为例） ───────────────────────────────
#
# asyncio.run(checkout())
#   → 创建事件循环
#   → 跑 checkout
#       → await fetch("结账-验库存", 1)
#           → 打印 "结账-验库存 开始"
#           → await asyncio.sleep(1)：挂起 fetch，控制权交回事件循环
#           → 1 秒后，事件循环唤醒 fetch
#           → fetch 返回 "结账-验库存 完成"
#       → 打印 "结账-验库存 完成"
#       → await fetch("结账-扣款", 1)  ← 同理
#       → ...
#   → checkout 结束，关闭事件循环


if __name__ == "__main__":
    demo_coroutine_object()
    print()
    demo_asyncio_run()
    print()
    demo_await()
