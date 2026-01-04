def calculate_damage(
    attack: int, damage_type: str, defense: int, resistance: int
) -> float:
    """
    Calculates damage based on Arknights rules.

    Physical:
        max(attack - defense, attack * 0.05)

    Arts:
        attack * (1 - resistance / 100)

    True:
        attack
    """

    damage_type = damage_type.lower()

    if damage_type == "physical":
        return max(attack - defense, attack * 0.05)

    elif damage_type == "arts":
        return attack * (1 - resistance / 100)

    elif damage_type == "true":
        return attack

    else:
        raise ValueError(f"Unknown damage type: {damage_type}")
