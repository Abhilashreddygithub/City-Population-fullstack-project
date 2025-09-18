from fastapi import FastAPI
from pydantic import BaseModel
from db import get_es

app = FastAPI()

class City(BaseModel):
    name: str
    population: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upsert")
def upsert_city(city: City):
    es = get_es()
    es.index(index="cities", id=city.name, document={"name": city.name, "population": city.population})
    return {"message": f"{city.name} added/updated"}

@app.get("/city/{name}")
def get_city(name: str):
    es = get_es()
    res = es.get(index="cities", id=name, ignore=[404])
    if res.get("found"):
        return res["_source"]
    return {"error": "City not found"}