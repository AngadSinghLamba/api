from fastapi import FastAPI
from pydantic import BaseModel ## For data validation

app = FastAPI()


user_db = {
    1: {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30
    },
    2: {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "age": 25
    },
    3: {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "age": 28
    },
    4: {
        "name": "Bob Brown",
        "email": "bob@example.com",
        "age": 32
    },
    5: {
        "name": "Charlie Davis",
        "email": "charlie@example.com",
        "age": 27
    },
    6: {
        "name": "David Miller",
        "email": "david@example.com",
        "age": 31
    },
    7: {
        "name": "Emily Wilson",
        "email": "emily@example.com",
        "age": 31
    }
}

# Creating a function and that function will upadate the data. That function we are eventually going to use as an API. 
class User(BaseModel):
    
    name: str
    email: str
    age: int




@app.put("/user_db/data/v1/update/{user_id}")
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    
    else:
        return {"message": "User not found"}
    
    
@app.delete("/user_db/data/v1/delete/{user_id}")    
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}