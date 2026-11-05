"""数据模型定义 —— 约定请求和响应的"形状"。

类比 Java 的 DTO / VO。
"""
from pydantic import BaseModel


class Item(BaseModel):
    """物品模型"""
    name: str
    price: float
    stock: int = 0


class ItemResponse(BaseModel):
    """响应中返回的物品（多一个 id 字段）"""
    id: int
    name: str
    price: float
    stock: int