from fastapi import FastAPI
from config import *
from operations.router import router as router_operation

app = FastAPI()

app.include_router(router_operation, )


@app.get('/')
def hello():
    return {'data': 'hello, world',
            'DB_NAME': DB_NAME
            }
