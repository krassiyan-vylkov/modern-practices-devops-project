from sqlalchemy import Column, Integer, String
from .database import Base


class Operator(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    attack = Column(Integer)
    damage_type = Column(String)


class Boss(Base):
    __tablename__ = "bosses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    defense = Column(Integer)
    resistance = Column(Integer)
