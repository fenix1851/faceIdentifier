from sqlite3 import Date
from fastapi_utils.tasks import repeat_every
from http import server
from unittest.mock import Base
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from processImage import processImage
from createEmbeding import addLocalUser
from createEmbeding import updateLocalUsers

from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import requests

app = FastAPI()
import json

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB_USER = "hakatonKrasnodar"
# DB_PASSWORD = "n01082002"
# DB_HOST = "http://hakatonKrasnodar.mysql.pythonanywhere-services.com"
# DB_PORT = 3306
# DATABASE = "hakatonKrasnodar$hacaton_3"


# connect_string = 'mysql+mysqlconnector://{}:{}@{}/{}?port={}?charset=utf8'.format(
#     DB_USER, DB_PASSWORD, DB_HOST, DATABASE, DB_PORT)

# DATABASE_URL = "mysql+mysqlconnector://hakatonKrasnodar@http://hakatonKrasnodar.mysql.pythonanywhere-services.com:3306/hakatonKrasnodar$hacaton_3"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

templates = Jinja2Templates(directory="../src/templates")

@app.get("/embedings")
async def get_embedings():
    with open('.../data/face_enc.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        return data


class UserToDelete(BaseModel):
    id: int
    

@app.post("/deleteUser/{id}")
async def delete_user(UserToDelete: UserToDelete):
    with open('.../data/face_enc.json', 'r') as jsonFile:
        id = str(UserToDelete.id)
        jsonOut = json.load(jsonFile)
        # print(jsonOut)
        ids = list(jsonOut.keys())
        print(ids)
        for localId in ids:
            if(localId == id):
                jsonOut.pop(id)
        with open('.../data/test.json', 'w') as data_file:
            data = json.dump(jsonOut, data_file)
        with open('.../data/test.json', 'r') as dataOut:
            # print(id)
            dataOut = json.load(dataOut)
            return dataOut
        # with open("face_enc.json", "w") as outfile:
        #     outfile.write(json.dumps(jsonOut))


@app.get('/video', response_class=HTMLResponse)
async def getVideo(request: Request):
    return templates.TemplateResponse("video.html", {"request": request})

class UserToAdd(BaseModel):
    base64: str
    id: int

class photoToProcess(BaseModel):
    base64: str

@app.post("/getProcessing")
async def getProcessing(photoToProcess: photoToProcess):
    photo = photoToProcess.base64
    # print(str(photo))
    photo = str(photo.split(",")[1]).replace(" ", "+")
    return(processImage(photo))

@app.post("/addUser")
async def addUser(UserToAdd: UserToAdd):
    dict = {UserToAdd.id:UserToAdd.base64}
    addLocalUser(dict)


@app.on_event("startup")
@repeat_every(seconds=5)
async def getUser():
    print(1)
    x = requests.get('https://hakatonkrasnodar.pythonanywhere.com/get_list_users')
    text = x.text
    with open(".../data/local.json", 'r')as local:
        localDict = json.load(local)
        serverDict = json.loads(text)
        localDictKeys = localDict.keys()
        serverDictKeys = serverDict.keys()
        # print(localDictKeys == serverDictKeys)
        if(localDict == serverDict):
            return({"message":"up to date"})
        else:
            with open(".../data/local.json", "w") as outfile:
                outfile.write(x.text)
                updateLocalUsers()

            return({"message": "data update"})
    return(x.text)
