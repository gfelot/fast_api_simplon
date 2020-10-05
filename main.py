import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
import logging
from bson.objectid import ObjectId

from correction.aluni import Alumni

CLIENT = MongoClient("mongodb+srv://gil:qwerty123@cluster0.0gdwd.gcp.mongodb.net/alumni?retryWrites=true&w=majority")
DB = CLIENT["test_heroku"]
STUDENTS = DB["students"]

app = FastAPI()


@app.get("/alumni")
async def get_all_students():
    data_list = []
    try:
        for d in STUDENTS.find():
            d["_id"] = str(d["_id"])
            data_list.append(d)
    except Exception as e:
        logging.error("Error in find_one")
        logging.error(e)
        return e

    return data_list


@app.get("/alumni/{id}")
async def get_one_student(id):
    try:
        data = STUDENTS.find_one({"_id": ObjectId(id)})
        data["_id"] = str(data["_id"])
    except Exception as e:
        logging.error("Error in find_one")
        logging.error(e)
        return e

    return data


@app.post("/alumni")
async def create_item(item: Alumni):
    try:
        id = str(STUDENTS.insert_one(item.dict()).inserted_id)
    except Exception as e:
        logging.error(e)
        return e
    return {"_id": id}


@app.delete("/alumni/{id}")
async def delete_one(id):
    try:
        STUDENTS.delete_one({"_id": ObjectId(id)})
    except Exception as e:
        logging.error("Error in find_one")
        logging.error(e)
        return e

    return {"text": f"Alumni with id {id} deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
