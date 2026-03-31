from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int):
        super().__init__(name, cost, rarity)

        if attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if health <= 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        info: dict = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        game_state["board"].append(self)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> dict:
        target.health -= self.attack
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
