# pip install uvicorn[standard]

from typing import Optional
import uvicorn
from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates

import json
from pydantic import BaseModel
import numpy as np
import os
from pathlib import Path
# from imageScore import ImageScore, getScore

app = FastAPI()

#app.mount("/site", StaticFiles(directory="site", html = True), name="site")

@app.get("/test")
def test():
    return 'success'

class ImageScore(BaseModel):
    imageNum: str
    scoreNum: int

def getScore(image_score: ImageScore):
    Path("./scores").mkdir(parents=True, exist_ok=True)
    if os.path.isfile('./scores/data.json'):
        with open('./scores/data.json', 'r') as fread:
            dic = json.load(fread)
            if image_score.imageNum in dic.keys():
                dic[str(image_score.imageNum)].append(image_score.scoreNum)
            else:
                dic[str(image_score.imageNum)] = [image_score.scoreNum]
    else:
        dic = {}
        dic[str(image_score.imageNum)] = [image_score.scoreNum]
    with open('./scores/data.json', 'w') as fwrite:
        json.dump(dic, fwrite)
    return "ok"

@app.post("/saveScore")
def saveScore(imageScore: ImageScore):
    getScore(imageScore) # the key is image_n number, 1 is positive
    return "ok"

@app.get("/getResult")
def getResult():
    with open('./scores/data.json', 'r') as fread:
        dic = json.load(fread)
    return dic

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# uvicorn main:app --reload --port 8000