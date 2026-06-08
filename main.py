# main.py

from fastapi import FastAPI  # 导入框架，相当于Spring Boot的@SpringBootApplication
from pydantic import BaseModel

app = FastAPI()  # 创建应用实例，相当于Spring容器

# 题目：实现一个商品详情接口
# 请求方式：GET
# 路径：/item/{item_id}
# 路径参数：item_id: int
# 接口内部构造一条商品数据（不需要真实数据库），包含以下字段：
#   - id: int
#   - name: str
#   - price: float
#   - cost: float         # 成本价，内部字段，不能返回给前端
#   - stock: int          # 库存，内部字段，不能返回给前端
# 返回字段（只含对外字段）：
#   - id: int
#   - name: str
#   - price: float
# 要求：用 response_model 控制返回字段

# 在这里写你的代码
class InProduct(BaseModel):
    id:int
    name:str
    price:str
    cost:float
    stock:int

class OutProduct(BaseModel):
    id:int
    name:str
    price:str
@app.get("/item/{item_id}",response_model=OutProduct)
def item(item_id: int):
    return {"id":item_id,"name":"product_name","price":1000}

# 题目：实现一个用户注册接口，注册时需要密码，但返回信息不能包含密码
# 请求方式：POST
# 路径：/register
# 请求体字段：
#   - username: str，必填
#   - email: str，必填
#   - password: str，必填
# 返回字段（不含password）：
#   - username: str
#   - email: str
#   - message: str，固定值 "注册成功"
# 要求：用 response_model 控制返回字段

# 在这里写你的代码

class InRegister(BaseModel):
    username:str
    email:str
    password:str

class OutRegister(BaseModel):
    username: str
    email: str
    message:str = "注册成功"

@app.post("/register",response_model=OutRegister)
def register(in_register:InRegister):
    return in_register









# 题目：实现一个"更新商品价格"接口
# 请求方式：PUT
# 路径：/product/{product_id}
# 路径参数：product_id: int
# 请求体字段：
#   - price: float，必填，新价格
#   - reason: str，选填，默认"常规调价"，调价原因
# 返回格式：{"product_id": 1, "new_price": 99.9, "reason": "促销活动"}

# 在这里写你的代码

class Query(BaseModel):
    price: float
    reason: str

@app.put("/product/{product_id}")
def product_id(query:Query,product_id: int):
    return {"product_id":product_id,"new_price":query.price,"reason":query.reason}




# 请求体
# 题目：实现一个"创建商品"接口
# 请求方式：POST
# 路径：/product
# 请求体字段：
#   - name: str，必填，商品名称
#   - price: float，必填，价格
#   - stock: int，选填，默认100，库存数量
# 返回格式：{"message": "创建成功", "product": {"name": "...", "price": ..., "stock": ...}}
# 提示：返回 product 字段时，可以用 product.model_dump() 把 BaseModel 转成字典

# 在这里写你的代码

class Product(BaseModel):
    name:str
    price:float
    stock:int = 100

@app.post("/product")
def product(product:Product):
    return {"message":"创建成功","product":product.model_dump()}



# 路由装饰器：@app.get 对应 @GetMapping
# "/hello" 是路径，相当于 @GetMapping("/hello")
@app.get("/hello")
def say_hello():
    # 直接return字典，FastAPI自动序列化为JSON（不需要@ResponseBody，默认就是）
    return {"message": "Hello World"}


# 题目：创建一个FastAPI应用，实现一个"计算器"接口
# 路径：GET /add/{a}/{b}
# 功能：返回两个整数 a 和 b 的和
# 返回格式：{"a": 1, "b": 2, "result": 3}
# 要求：a 和 b 都是路径参数，类型为 int

# 在这里写你的代码

@app.get("/add/{a}/{b}")
def add(a:int,b:int):
    return {"a":a,"b":b,"result":a+b}

# 题目：实现一个商品搜索接口
# 路径：GET /products
# 查询参数：
#   - keyword: str，必填，搜索关键词
#   - min_price: float，选填，默认0.0，最低价格
#   - max_price: float，选填，默认9999.0，最高价格
# 功能：直接返回这些参数（不需要真实搜索逻辑）
# 返回格式：{"keyword": "手机", "min_price": 100.0, "max_price": 500.0}

# 在这里写你的代码

@app.get("/products")
def products(keyword:str,min_price:float =0.0,max_price :float =9999.0):
    return {"keyword":keyword,"min_price":min_price,"max_price":max_price}