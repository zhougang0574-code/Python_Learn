"""物品相关路由 —— 负责处理 /items 开头的请求。

拆到单独文件是 FastAPI 的最佳实践，主文件只负责"组装"。
"""
from fastapi import APIRouter, HTTPException

from ..models import Item, ItemResponse

router = APIRouter(prefix="/items", tags=["物品管理"])

# 用内存字典模拟数据库
fake_db: dict[int, dict] = {}
_next_id = 1


@router.get("/", response_model=list[ItemResponse])
async def list_items():
    """GET /items/  —— 列出所有物品"""
    return [
        ItemResponse(id=item_id, **data)
        for item_id, data in fake_db.items()
    ]


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """GET /items/1 —— 获取指定物品

    {item_id} 是路径参数，FastAPI 自动解析为 int。
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="物品不存在")
    return ItemResponse(id=item_id, **fake_db[item_id])


@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    """POST /items/ —— 创建新物品

    FastAPI 自动把请求 JSON 转成 Item 对象（Pydantic 校验）。
    """
    global _next_id
    item_id = _next_id
    _next_id += 1
    fake_db[item_id] = item.model_dump()
    return ItemResponse(id=item_id, **fake_db[item_id])


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: Item):
    """PUT /items/1 —— 更新物品

    路径参数 + 请求体 一起用，FastAPI 自动区分。
    """
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="物品不存在")
    fake_db[item_id] = item.model_dump()
    return ItemResponse(id=item_id, **fake_db[item_id])


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    """DELETE /items/1 —— 删除物品"""
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="物品不存在")
    del fake_db[item_id]
    return {"message": f"物品 {item_id} 已删除"}