from fastapi import FastAPI
from pydantic import BaseModel
from app.damage import calculate_damage

app = FastAPI(title="Arknights Damage Calculator")

class DamageInput(BaseModel):
    attack: int
    defense: int
    multiplier: float

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/damage")
def damage(data: DamageInput):
    result = calculate_damage(data.attack, data.defense, data.multiplier)
    return {"damage": result}