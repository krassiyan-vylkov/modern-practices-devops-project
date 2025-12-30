from pydantic import BaseModel

class DamageRequest(BaseModel):
    operator_id: int
    boss_id: int

class DamageResponse(BaseModel):
    damage: float
    damage_type: str
