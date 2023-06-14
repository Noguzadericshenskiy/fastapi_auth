import os
from fastapi import FastAPI
import uvicorn

from auth.config_auth import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from file.routes import router as routes_file
from config import CURRENT_PATH


app = FastAPI(title="task_api_csv_file")


app.include_router(routes_file)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


@app.on_event("startup")
async def startup_event():
    path = os.path.join(CURRENT_PATH, "uploaded_files")
    if not os.path.exists(path):
        os.makedirs(path)


# if __name__ == '__main__':
#     uvicorn.run("main:app", port=8000, host='127.0.0.1')
