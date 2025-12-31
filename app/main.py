from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import SessionLocal
from . import crud, schemas

app = FastAPI(title="Arknights Damage Calculator")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    operators = db.query(crud.models.Operator).all()
    bosses = db.query(crud.models.Boss).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "operators": operators, "bosses": bosses},
    )


@app.get("/operators")
def get_operators(db: Session = Depends(get_db)):
    return db.query(crud.models.Operator).all()


@app.post("/operators")
def create_operator(op: schemas.OperatorCreate, db: Session = Depends(get_db)):
    return crud.create_operator(db, op)


@app.get("/bosses")
def get_bosses(db: Session = Depends(get_db)):
    return db.query(crud.models.Boss).all()


@app.post("/bosses")
def create_boss(boss: schemas.BossCreate, db: Session = Depends(get_db)):
    return crud.create_boss(db, boss)


@app.post("/calculate", response_model=schemas.DamageResponse)
def calculate(data: schemas.DamageRequest, db: Session = Depends(get_db)):
    op = crud.get_operator(db, data.operator_id)
    boss = crud.get_boss(db, data.boss_id)

    if op.damage_type == "physical":
        damage = max(op.attack - boss.defense, op.attack * 0.05)
    elif op.damage_type == "arts":
        damage = op.attack * (1 - boss.resistance / 100)
    elif op.damage_type == "true":
        damage = op.attack

    return {"damage": round(damage, 2), "damage_type": op.damage_type}
