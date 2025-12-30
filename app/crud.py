from sqlalchemy.orm import Session
from . import models

def get_operator(db: Session, operator_id: int):
    return db.query(models.Operator).filter(models.Operator.id == operator_id).first()

def get_boss(db: Session, boss_id: int):
    return db.query(models.Boss).filter(models.Boss.id == boss_id).first()