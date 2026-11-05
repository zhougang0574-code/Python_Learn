"""演示二：从外部导入包里的模块。

用法（在项目的根目录下运行）：
    python -c "from import_demo import demo2_imported"

或者交互式：
    >>> from import_demo import demo2_imported
"""

# 情况 B —— 被外部当作包成员导入时，可以用相对导入：
from .utils import VERSION        # ✅ .  = 当前包 import_demo
from .utils import hello          # ✅ 相对导入正常工作

# 也可以用绝对路径：
from import_demo.utils import VERSION as version2  # ✅ 也行，但比较长

print(f"VERSION = {VERSION}")
print(f"hello() = {hello()}")