from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users =[]

@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def post_user(inner_user: User, username, age):
    if len(users) == 0:
        inner_user.id = 1
    else:
        inner_user.id = users[-1].id + 1
    inner_user.username = username
    inner_user.age = age
    users.append(inner_user)
    print(type(inner_user))
    return inner_user


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: int, username: str, age: int):
    user_ok = False
    for _ in range(len(users)):
        if users[_].id == user_id:
            user_ok = True
            users[_].username = username
            users[_].age = age
    if not user_ok:
        raise HTTPException(status_code=404, detail='User was not found"')


@app.delete('/user/{user_id}')
async def del_user(user_id: int):
    user_ok = False
    for _ in range(len(users)):
        if users[_].id == user_id:
            user_ok = True
            users.pop(_)
            return
    if not user_ok:
        raise HTTPException(status_code=404, detail='User was not found"')
