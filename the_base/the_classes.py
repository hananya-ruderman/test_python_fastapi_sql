from pydantic import BaseModel 

class Soldier(BaseModel):
    personal_number: int 
    name: str
    last_name: str
    gender: str
    sity: str
    distance_in_km: int
    has_placed: bool = False



class Room(BaseModel):
    list_of_soldiers: list[Soldier] = []
    room_num: int = 0
    tenat: int = 0
    max_of_tenats: int = 8
    is_full: bool = False

class Residance(BaseModel):
    list_of_rooms: list[Room] = []
    residance_num: int = 0
    num_of_rooms: int = 10
    max_of_tenats: int = 80
    is_full: bool = False

class Base(BaseModel):
    list_of_residences: list[Residance] = []
    residences: int = 2
    max_of_tenats: int = 160
    current_tenats: int = 0
    is_full: bool = False






