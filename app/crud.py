from sqlalchemy.orm import Session
from . import models


def get_operator(db: Session, operator_id: int):
    return db.query(models.Operator).filter(models.Operator.id == operator_id).first()


def get_boss(db: Session, boss_id: int):
    return db.query(models.Boss).filter(models.Boss.id == boss_id).first()


def create_operator(db: Session, operator):
    db_operator = models.Operator(
        name=operator.name,
        attack=operator.attack,
        damage_type=operator.damage_type,
    )
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


def create_boss(db: Session, boss):
    db_boss = models.Boss(
        name=boss.name,
        defense=boss.defense,
        resistance=boss.resistance,
    )
    db.add(db_boss)
    db.commit()
    db.refresh(db_boss)
    return db_boss
