from datetime import datetime
from passlib import hash
from bson import ObjectId


class ObjectID:
    def __init__(self) -> None:
        # self.__obj_id = 
        pass 
    
    def generate_id(self):
        obj_id = ObjectId()
        time_obj = hash.bcrypt.hash(str(datetime.now()))[50:]
        result = f"ORDER+{time_obj}{obj_id}"
        return result

    def __str__(self) -> str:
        return self.generate_id()

