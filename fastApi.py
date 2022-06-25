from unittest.mock import Base
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from processImage import processImage
from createEmbeding import addLocalUser

from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

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

templates = Jinja2Templates(directory="templates")

@app.get("/embedings")
async def get_embedings():
    with open('face_enc.json', 'r') as jsonFile:
        data = json.load(jsonFile)
        return data


class UserToDelete(BaseModel):
    id: int
    

@app.post("/deleteUser/{id}")
async def delete_user(UserToDelete: UserToDelete):
    with open('face_enc.json', 'r') as jsonFile:
        id = str(UserToDelete.id)
        jsonOut = json.load(jsonFile)
        # print(jsonOut)
        ids = list(jsonOut.keys())
        print(ids)
        for localId in ids:
            if(localId == id):
                jsonOut.pop(id)
        with open('test.json', 'w') as data_file:
            data = json.dump(jsonOut, data_file)
        with open('test.json', 'r') as dataOut:
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


@app.get("/getProcessing")
async def getProcessing(photoToProcess: photoToProcess):
    photo = photoToProcess.base64
    photo = str(photo.split(",")[1]).replace(" ", "+")
    # print(str(photo.split(",")[0]))
    # print(photo)
    processImage(photo)
    return(photo)

@app.post("/addUser")
async def addUser(UserToAdd: UserToAdd):
    dict = {UserToAdd.id:UserToAdd.base64}
    addLocalUser(dict)
