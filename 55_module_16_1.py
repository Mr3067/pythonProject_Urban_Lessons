from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main() -> str:
    return ("Главная страница")


@app.get("/user/admin")
async def admin_pg() -> str:
    return ("Вы вошли как администратор")


@app.get("/user/{user_id}")
async def user_id(user_id) -> str:
    return (f"Вы вошли как пользователь № {user_id}")


@app.get("/user")
async def user_all(username: str = "Иван", age: int = "25") -> dict:
    return ({"User": username, "Age": age})
