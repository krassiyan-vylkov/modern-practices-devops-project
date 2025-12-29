from app.damage import calculate_damage

def test_basic_damage():
    assert calculate_damage(100, 50, 1.0) == 50

def test_zero_damage():
    assert calculate_damage(50, 100, 1.0) == 0