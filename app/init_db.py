from app.database import engine, SessionLocal
from .models import Base, Operator, Boss

Base.metadata.create_all(bind=engine)

db = SessionLocal()

operators = [
    Operator(name="Exusiai", attack=650, damage_type="physical"),
    Operator(name="SilverAsh", attack=900, damage_type="physical"),
    Operator(name="Eyjafjalla", attack=800, damage_type="arts"),
]

bosses = [
    Boss(name="Patriot", defense=1200, resistance=50),
    Boss(name="FrostNova", defense=600, resistance=70),
    Boss(name="Crownslayer", defense=400, resistance=20),
]

db.add_all(operators + bosses)
db.commit()
db.close()

print("Database seeded.")
