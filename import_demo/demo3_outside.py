"""演示三：包外的脚本如何导入包里的东西。

用法：python demo3_outside.py

这个文件在 import_demo 包的外面，和 import_demo 文件夹平级。
"""

# 方式一：完整路径（永远可用）
from import_demo.utils import hello
print(f"方式一: hello() = {hello()}")

# 方式二：间接导入（如果 __init__.py 里预导了，就可以简写）
import import_demo
# import_demo.hello()  # ❌ 因为 __init__.py 没预导出 hello

# 方式三：from 包 import 模块
from import_demo import utils
print(f"方式三: utils.hello() = {utils.hello()}")