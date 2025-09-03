from fastapi import FastAPI
from fastapi import FastAPI, Request
from starlette.responses import Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/ping")
def read_root():
    return {"message": "pong"}

class Characteristic(BaseModel):
    max_speed: int
    max_fuel_capacity: int

class CarModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic



car_stores: List[CarModel] = []

def serialized_stored_students():
    car_converted = []
    for car in car_stores:
        car_converted.append(car.model_dump())
    return car_converted

@app.post("/cars")
def add_car(cars: List[CarModel]):
    for car in cars:
        car_stores.append(car)
    return JSONResponse({"message":"car added"}, status_code=201)

@app.get("/cars")
def cars_list():
    return JSONResponse({"cars": serialized_stored_students()}, status_code=200)

@app.get("/cars/{id}")
def get_car_with_id(id : str):
    for i, car in enumerate(car_stores):
        if id == car[i].identifier:
            return JSONResponse({"car" : car[i]},status_code=200)
    return JSONResponse({"message" : "the id in paramaters doesn't exist"},status_code=404)

