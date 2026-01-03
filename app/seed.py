from app.database import engine, SessionLocal
from app.models import Base, Operator, Boss


def seed():
    # Create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Prevent duplicate seeding
    if db.query(Operator).first():
        print("Database already seeded.")
        db.close()
        return

    operators = [
        Operator(name="Exusiai", attack=650, damage_type="physical"),
        Operator(name="SilverAsh", attack=900, damage_type="physical"),
        Operator(name="Eyjafjalla", attack=800, damage_type="arts"),
        Operator(name="Surtr", attack=2000, damage_type="arts"),
        Operator(name="Mlynar", attack=1800, damage_type="physical"),
        Operator(name="Mons3r", attack=1200, damage_type="true"),
        Operator(name="Saga", attack=1000, damage_type="physical"),
        Operator(name="Bubble", attack=300, damage_type="physical"),
    ]

    bosses = [
        Boss(name="Patriot", defense=1200, resistance=50),
        Boss(name="FrostNova", defense=600, resistance=70),
        Boss(name="Crownslayer", defense=400, resistance=20),
        Boss(name="Last Steam Knight", defense=2000, resistance=10),
        Boss(name="Minimalist", defense=200, resistance=40),
        Boss(name="Pompeii", defense=200, resistance=80),
        Boss(name="Mechanist", defense=1400, resistance=50),
    ]

    db.add_all(operators + bosses)
    db.commit()
    db.close()

    print("Database seeded successfully")


if __name__ == "__main__":
    seed()
