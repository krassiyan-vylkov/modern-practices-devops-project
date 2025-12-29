def calculate_damage(attack: int, defense: int, multiplier: float) -> int:
    base_damage = max(attack - defense, 0)
    return int(base_damage * multiplier)