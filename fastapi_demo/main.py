"""FastAPI Demo —— 最精简的 Web API 服务。

对比你之前看的那段生产代码，这个是"骨架版"。

启动方式：
    uvicorn fastapi_demo.main:app --reload

然后访问：
    http://localhost:8000           → 欢迎页
    http://localhost:8000/docs      → Swagger 交互式文档（自动生成）
    http://localhost:8000/items/    → 物品列表 API
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .models import Item, ItemResponse     # 上一级的 models 模块
from .routers import items_router          # 上级的 routers 包

# ============================================================
# 一、生命周期管理
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用启动和关闭时的钩子。

    yield 之前 = 启动时执行（初始化数据库连接等）
    yield 之后 = 关闭时执行（清理资源）
    """
    print(">>> 服务启动了！")
    yield
    print(">>> 服务关闭了！")


# ============================================================
# 二、创建应用实例（组装各个组件）
# ============================================================

app = FastAPI(
    title="FastAPI 入门 Demo",
    description="一个极简的 CRUD API，用来说明 FastAPI 的核心概念",
    version="1.0.0",
    lifespan=lifespan,
)

# 注册子路由（模块化的路由，就像 import 子模块一样）
app.include_router(items_router)

# ============================================================
# 三、根路径 —— 最简单的一个路由
# ============================================================


@app.get("/")
async def root():
    """GET / —— 浏览器打开 http://localhost:8000 就能看到"""
    return {
        "message": "欢迎来到 FastAPI Demo！",
        "docs": "http://localhost:8000/docs",
        "tips": [
            "GET  /            → 本页面",
            "GET  /items/      → 列出所有物品",
            "POST /items/      → 创建物品 (需要 JSON 请求体)",
            "GET  /items/1     → 查看 id=1 的物品",
            "PUT  /items/1     → 更新 id=1 的物品",
            "DELETE /items/1   → 删除 id=1 的物品",
        ],
    }