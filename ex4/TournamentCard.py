from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    BASE_RATING = 1200
    WIN_POINTS = 16
    LOSS_POINTS = 16

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("Attack power must be a positive integer.")
        if not isinstance(defense, int) or defense <= 0:
            raise ValueError("Defense must be a positive integer.")
        self.attack_power = attack_power
        self.defense = defense
        self._wins: int = 0
        self._losses: int = 0
        self._rating: int = self.BASE_RATING

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"{self.name} enters the tournament arena!",
        }

    def attack(self, target) -> dict:
        target_name = (
            target.name if hasattr(target, "name") else str(target)
        )
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "tournament",
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError(
                "Incoming damage must be a non-negative integer."
            )
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < self.attack_power,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
        }

    def calculate_rating(self) -> int:
        self._rating = (
            self.BASE_RATING
            + (self._wins * self.WIN_POINTS)
            - (self._losses * self.LOSS_POINTS)
        )
        return self._rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("Wins must be a non-negative integer.")
        self._wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("Losses must be a non-negative integer.")
        self._losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self._wins,
            "losses": self._losses,
            "record": f"{self._wins}-{self._losses}",
        }

    def get_tournament_stats(self) -> dict:
        stats = self.get_rank_info()
        stats.update(self.get_combat_stats())
        stats["interfaces"] = ["Card", "Combatable", "Rankable"]
        return stats
