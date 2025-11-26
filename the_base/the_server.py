
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Response
from pydantic import BaseModel 
import sqlite3
from datetime import datetime
import uvicorn
import csv
import io
import pandas as pd
from the_base.the_classes import Soldier, Base, Residance, Room


app = FastAPI(title="placement control API", version="1.0.0")



@app.post("/placement/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    print("jhyg")
    
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    
    print("jhyg")
    
   
    contents = await file.read()
    print("jhyg")
    contents_as_list_of_instances = create_instances_from_csv(contents)
    sorted_list = sort_soldiers_by_distance(contents_as_list_of_instances)
    base, current_tenat = place_soldiers_in_base(sorted_list)
 
    

    return base





# helper functions
def create_instances_from_csv(csv_content: bytes)-> dict:
    csv_text = csv_content.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
    list_of_soldiers = []
    for row in csv_reader:
        
        new_soldier = Soldier(personal_number=row['מספר אישי'], name=row['שם פרטי'], last_name=row['שם משפחה'], gender=row['מין'], sity=row['עיר מגורים'], distance_in_km=row['מרחק מהבסיס'])
        list_of_soldiers.append(new_soldier)

    return list_of_soldiers

def sort_soldiers_by_distance(list_of_objects: list[dict]):
 
    new_list = sorted(list_of_objects, key=lambda x: x.distance_in_km, reverse=False)

    return new_list



def place_soldiers_in_base(list_of_soldiers):
    base = Base()
    residance = Residance()
    room = Room()
    new_list_of_soldiers = list_of_soldiers

    for i in range(base.residences):
        base.list_of_residences.append(residance)
        residance.residance_num = i+1
        
        for j in range(residance.num_of_rooms):
            residance.list_of_rooms.append(room)
            room.room_num = i+1   
            for z in range(room.max_of_tenats):
                if new_list_of_soldiers:
                    next_soldier = new_list_of_soldiers.pop()
                   
                    room.list_of_soldiers.append(next_soldier)
                    
                    base.current_tenats += 1
                    
                else:
                    print('everyone has placed')
                    return base
    print(new_list_of_soldiers)               
    return base, new_list_of_soldiers
    

                


            
    
    





if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8001)

    #uvicorn the_base.the_server:app --reload --port 8001
    a = 5
    print(place_soldiers_in_base())