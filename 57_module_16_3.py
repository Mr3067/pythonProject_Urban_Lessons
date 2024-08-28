from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"
         }


@app.get('/users')
async def get_dict():
    return users


@app.post('/user/{username}/{age}')
async def post_dict(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def put_dict(user_id: int, username: str, age: int):
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'

@app.delete('/user/{user_id}')
async def del_dict(user_id: int)->str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'

