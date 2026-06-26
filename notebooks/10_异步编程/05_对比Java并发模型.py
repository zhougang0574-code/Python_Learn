"""
异步编程 · 知识点 5/5：asyncio 与 LangChain 的连接

学完前四章之后，这一章做两件事：
  1. 把 Python asyncio 和 Java 并发模型做个横向对比，帮你建立正确的心智模型
  2. 把 asyncio 的每个核心模式映射到 LangChain / LangGraph 里的实际用法

直接运行：python 05_对比Java并发模型.py
"""
import asyncio
import time


# ─── 1. 对比 Java 并发模型 ───────────────────────────────────────────────────
#
# Java                            Python asyncio
# ──────────────────────────────────────────────────────
# Thread / ExecutorService         单线程事件循环
# 多线程，真正并行                   协程，协作式并发
# 系统随时打断线程切换                遇到 await 才切换
# 需要锁 / 并发集合保证线程安全       单线程天然不需要锁
# CompletableFuture 组合结果         asyncio.gather 组合结果
# 底层是线程池                        底层是事件循环
#
# 更贴近的类比其实是 JavaScript 的 async/await + Promise：
#   都是单线程事件循环，写法和思路几乎一模一样。
#
# GIL 补充：
#   Python 有全局解释器锁（GIL），同一时刻只有一个线程能跑 Python 字节码。
#   所以 Python 多线程对 CPU 密集型任务没有加速效果。
#   asyncio 是单线程，天然绕开了 GIL 的问题——它本来就不靠多线程。
#   真正需要 CPU 并行的话，用 multiprocessing（多进程）。


# ─── 2. IO 密集 vs CPU 密集：asyncio 的适用边界 ──────────────────────────

async def io_task(name, delay):
    print(f"{name} 开始等待")
    await asyncio.sleep(delay)   # 模拟网络请求/数据库查询
    print(f"{name} 响应完成")
    return name


async def demo_io_bound():
    print("=== IO 密集型：asyncio 有显著收益 ===")
    start = time.time()
    results = await asyncio.gather(
        io_task("接口A", 1),
        io_task("接口B", 1),
        io_task("接口C", 1),
    )
    print(f"结果：{results}，耗时：{time.time() - start:.1f} 秒（约等于最慢的一个，不是三个相加）")


def cpu_heavy():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


async def demo_cpu_bound():
    print("=== CPU 密集型：asyncio 没有加速效果 ===")
    # cpu_heavy() 内部没有任何 await，事件循环无法在中途切到别的协程
    # 这段时间整个事件循环都被这个计算占着
    start = time.time()
    result = cpu_heavy()
    print(f"计算结果：{result}，耗时：{time.time() - start:.1f} 秒（asyncio 没有任何加速）")
    print("CPU 密集型任务应该用 multiprocessing，不是 asyncio")


# ─── 3. asyncio 模式 → LangChain / LangGraph 实际用法 ─────────────────────
#
# 你学的每个 asyncio 模式，在 LangChain / LangGraph 里都有对应的真实场景：
#
# ┌─────────────────────────────┬─────────────────────────────────────────────┐
# │ asyncio 模式                │ LangChain / LangGraph 场景                  │
# ├─────────────────────────────┼─────────────────────────────────────────────┤
# │ async def / await           │ chain.ainvoke() / llm.ainvoke()             │
# │                             │ 所有 LangChain 组件都有 async 版本（a 前缀）  │
# ├─────────────────────────────┼─────────────────────────────────────────────┤
# │ asyncio.gather()            │ 并发调用多个 LLM / 多个 chain                │
# │                             │ 比如同时让模型生成三个答案候选，取最好的一个   │
# ├─────────────────────────────┼─────────────────────────────────────────────┤
# │ async for                   │ chain.astream() / llm.astream()             │
# │                             │ 流式输出：逐 token 打印，不用等全部生成完     │
# ├─────────────────────────────┼─────────────────────────────────────────────┤
# │ async with                  │ AsyncCallbackManager、异步 HTTP session      │
# │                             │ 在异步上下文里安全管理资源                    │
# ├─────────────────────────────┼─────────────────────────────────────────────┤
# │ asyncio.wait_for()          │ 给 LLM 调用设置超时，防止模型响应过慢卡死    │
# └─────────────────────────────┴─────────────────────────────────────────────┘
#
# LangChain 的命名规律：
#   同步方法：invoke / stream / batch
#   异步方法：ainvoke / astream / abatch（加 'a' 前缀）
#
# 看到这样的代码你就能看懂了：
#
#   async def run_parallel_chains(question: str):
#       results = await asyncio.gather(
#           chain_a.ainvoke({"question": question}),
#           chain_b.ainvoke({"question": question}),
#       )
#       return results
#
#   async def stream_response(question: str):
#       async for chunk in llm.astream(question):
#           print(chunk.content, end="", flush=True)


# ─── 4. 模拟 LangChain 的 ainvoke / astream 模式 ────────────────────────

async def fake_llm_ainvoke(prompt: str, delay: float = 1.0) -> str:
    """模拟 LangChain 的 llm.ainvoke()——实际上是一个异步网络请求"""
    await asyncio.sleep(delay)
    return f"[模型回答] {prompt} 的答案是 42"


async def fake_llm_astream(prompt: str):
    """模拟 LangChain 的 llm.astream()——逐 token 流式输出"""
    words = f"这是对 '{prompt}' 的流式回答".split()
    for word in words:
        await asyncio.sleep(0.2)
        yield word


async def demo_parallel_invoke():
    print("=== 并发调用多个 LLM（模拟 gather + ainvoke）===")
    start = time.time()
    results = await asyncio.gather(
        fake_llm_ainvoke("问题A", 1.0),
        fake_llm_ainvoke("问题B", 1.0),
        fake_llm_ainvoke("问题C", 1.0),
    )
    for r in results:
        print(r)
    print(f"耗时：{time.time() - start:.1f} 秒（三个并发，不是串行的 3 秒）")


async def demo_stream():
    print("=== 流式输出（模拟 astream + async for）===")
    async for token in fake_llm_astream("Python 异步编程"):
        print(token, end=" ", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(demo_io_bound())
    print()
    asyncio.run(demo_cpu_bound())
    print()
    asyncio.run(demo_parallel_invoke())
    print()
    asyncio.run(demo_stream())
