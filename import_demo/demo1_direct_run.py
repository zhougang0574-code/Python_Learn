"""演示一：直接运行 main.py 的情况。

用法：python main.py
"""

# 情况 A —— 同级文件，当成独立脚本运行时，只能用绝对名字
#
# 以下两种写法在 "python main.py" 时都能用：
import utils                    # ✅ utils 是顶层模块名

# from .utils import VERSION    # ❌ 会报错！相对导入在独立脚本里不允许

print(f"utils.VERSION = {utils.VERSION}")
print(f"utils.hello() = {utils.hello()}")