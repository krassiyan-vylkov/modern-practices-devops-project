from app.damage import calculate_damage


def test_physical_damage_normal():
    dmg = calculate_damage(
        attack=1000, damage_type="physical", defense=600, resistance=0
    )
    assert dmg == 400


def test_physical_damage_minimum():
    dmg = calculate_damage(
        attack=100, damage_type="physical", defense=200, resistance=0
    )
    # 5% minimum rule
    assert dmg == 5


def test_arts_damage_normal():
    dmg = calculate_damage(attack=1000, damage_type="arts", defense=0, resistance=50)
    assert dmg == 500


def test_arts_damage_zero_resistance():
    dmg = calculate_damage(attack=800, damage_type="arts", defense=0, resistance=0)
    assert dmg == 800


def test_true_damage():
    dmg = calculate_damage(attack=1000, damage_type="true", defense=100, resistance=20)
    assert dmg == 1000
