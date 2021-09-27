from pydantic import BaseModel
# from helper import Database
import random
class User(BaseModel):
    id: int
    f_name : str
    l_name : str
    email : str
    pwd : str

# usr = User(_id = 1332, f_name="steve",l_name="mac",email="tim@mail.com",pwd="test")
# # db.add(usr.dict())
# y = db.retrieve("f_name=steve")
# print(y)