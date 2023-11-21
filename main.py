from fastapi import FastAPI
from operations.router import router as router_operation
from auth.auth import auth_backend
from fastapi_users import FastAPIUsers
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

app = FastAPI()

app.include_router(router_operation, )

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

'''
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
'''


@app.get('/')
def hello():
    return {'data': 'welcome to api. take a login and use this api',
            }
