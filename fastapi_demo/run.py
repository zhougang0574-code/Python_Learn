import uvicorn
from fastapi_demo import main

def start():
    uvicorn.run(main.app, host="0.0.0.0", port=8000)

start()