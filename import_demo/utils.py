"""这个文件演示：当你被当作"独立脚本"运行 vs "包成员"导入时的区别。

每个函数打印出自己的 __name__，直观看到身份变化。
"""

print(f"--- 我被加载了！我的名字是 {__name__!r} ---")

VERSION = "1.0"


def hello():
    print(f"hello() 被调用了，我来自 {__name__}")
    return "world"