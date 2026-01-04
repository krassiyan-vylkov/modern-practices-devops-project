from pydantic import BaseModel


class OperatorCreate(BaseModel):
    name: str
    attack: int
    damage_type: str


class BossCreate(BaseModel):
    name: str
    defense: int
    resistance: int


class DamageRequest(BaseModel):
    operator_id: int
    boss_id: int


class DamageResponse(BaseModel):
    damage: float
    damage_type: str
