import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self._cards: dict = {}
        self._matches: list = []

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError(
                "Only TournamentCard instances can be registered."
            )
        card_id = f"{card.name.lower().replace(' ', '_')}_001"
        self._cards[card_id] = card
        return card_id

    def create_match(
        self, card1_id: str, card2_id: str
    ) -> dict:
        if card1_id not in self._cards:
            raise ValueError(f"Card '{card1_id}' not registered.")
        if card2_id not in self._cards:
            raise ValueError(f"Card '{card2_id}' not registered.")

        card1 = self._cards[card1_id]
        card2 = self._cards[card2_id]

        if card1.attack_power > card2.attack_power:
            winner_id, loser_id = card1_id, card2_id
        elif card2.attack_power > card1.attack_power:
            winner_id, loser_id = card2_id, card1_id
        else:
            winner_id, loser_id = random.choice(
                [(card1_id, card2_id), (card2_id, card1_id)]
            )

        winner = self._cards[winner_id]
        loser = self._cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)

        match_record = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(match_record)
        return match_record

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self._cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            info = card.get_rank_info()
            leaderboard.append({
                "rank": rank,
                "card_id": card_id,
                "name": info["name"],
                "rating": info["rating"],
                "record": info["record"],
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        ratings = [
            c.calculate_rating() for c in self._cards.values()
        ]
        avg_rating = (
            round(sum(ratings) / total) if total > 0 else 0
        )
        return {
            "total_cards": total,
            "matches_played": len(self._matches),
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
