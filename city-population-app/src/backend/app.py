from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import get_es

app = FastAPI()

# Allow the frontend (served on localhost:3000) to call these APIs during development.
# For production, restrict origins appropriately.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class City(BaseModel):
    name: str
    population: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upsert")
async def upsert_city(req: Request):
    """Accepts either {"name":..., "population":...} or {"city":..., "population":...}
    to be compatible with the frontend payload shape.
    """
    payload = await req.json()
    # Accept both 'name' and 'city' as the identifier
    name = payload.get("name") or payload.get("city")
    population = payload.get("population")
    if not name or population is None:
        return {"detail": [{"type": "missing", "loc": ["body", "name or city"], "msg": "Field required", "input": payload}]}

    es = get_es()
    es.index(index="cities", id=name, document={"name": name, "population": population})
    return {"message": f"{name} added/updated"}


@app.get("/query")
def query_city(city: str):
    """Compatibility endpoint for the frontend: /query?city=Name"""
    es = get_es()
    res = es.get(index="cities", id=city, ignore=[404])
    if res.get("found"):
        return res["_source"]
    return {"error": "City not found"}


@app.get("/city/{name}")
def get_city(name: str):
    # keep existing path-based endpoint as well
    es = get_es()
    res = es.get(index="cities", id=name, ignore=[404])
    if res.get("found"):
        return res["_source"]
    return {"error": "City not found"}