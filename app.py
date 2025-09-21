import model
import shutil
import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel 
from general_utility import number_to_indian_mix




app = FastAPI()

@app.post("/api/v1/train")
async def train_model(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    model.train(temp_path)
    os.remove(temp_path)
    return model.weights()

@app.get("/api/v1/weights")
def show_weights():
    return model.weights()

@app.get("/api/v1/weights/reset")
def rest_model():
    model.reset_weights()
    return model.weights()

@app.get("/api/v1/predict_price")
def predict_price(rooms: float, sqft: float):
    return number_to_indian_mix(model.predict_price(rooms, sqft))
