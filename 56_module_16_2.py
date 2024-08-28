from fastapi import FastAPI, Path
from typing import Annotated

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main() -> str:
    return ("Главная страница")


# @app.get("/user/admin")
# async def admin_pg() -> str:
#     return ("Вы вошли как администратор")
#
#
# @app.get("/user/{user_id}")
# async def user_id(user_id) -> str:
#     return (f"Вы вошли как пользователь № {user_id}")


@app.get("/user/{username}/{id}")
# async def user_all(username: str = Path(min_length=2, max_length=20, description="Введите свое имя"),
#                    age: int = Path(ge=0, le=100, description="введите свой Id")) -> dict:
async def user_all(username: str, age: int ) -> dict:
    return {"User": username, "Age": age}
