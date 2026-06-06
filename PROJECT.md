# Python_Learn — 项目说明

## 项目目的

本项目是一个 **Python 自学工作区**，专为 Java 后端开发者转型设计，最终目标是掌握 Python 并能熟练使用 **LangChain** 进行 AI 应用开发。

## 项目结构

```
Python_Learn/
├── main.py              # 练习入口文件，在这里运行代码片段
├── docs/
│   └── python-guide.html  # Python 学习文档（主文档，用浏览器打开）
├── .venv/               # Python 虚拟环境（不提交到 git）
├── requirements.txt     # 项目依赖（按需生成）
└── PROJECT.md           # 本文件
```

## 学习文档

打开 `docs/python-guide.html` 查看完整学习文档，包含：

| 章节 | 内容 | 状态 |
|------|------|------|
| 01   | 环境 & 基础语法 | ✅ 完成 |
| 02   | 数据类型 & 集合 | ✅ 完成 |
| 03   | 控制流 | ✅ 完成 |
| 04   | 函数 | ✅ 完成 |
| 05   | 面向对象编程 | 待更新 |
| 06   | 模块 & 包管理 | 待更新 |
| 07   | 文件 & IO | 待更新 |
| 08   | 异常处理 | 待更新 |
| 09   | 高级特性 | 待更新 |
| 10   | 常用标准库 | 待更新 |
| 11   | 异步编程 | 待更新 |
| 12   | LangChain 实战 | 待更新 |

## 快速开始

```powershell
# 激活虚拟环境
.venv\Scripts\activate

# 运行练习文件
python main.py
```

## 技术栈目标

- **Python 3.11+**
- **LangChain** — AI 应用框架
- **OpenAI / Anthropic SDK** — LLM 调用
