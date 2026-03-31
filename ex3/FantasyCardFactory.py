from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> CreatureCard:
        creatures = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 3, 2),
        ]
        name, cost, rarity, attack, health = random.choice(creatures)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power=None) -> SpellCard:
        spells = [
            ("Fireball", 3, "Rare", "damage"),
        ]
        name, cost, rarity, effect = random.choice(spells)
        return SpellCard(name, cost, rarity, effect)

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        artifacts = [
            ("Mana Ring", 2, "Rare", 3, "+1 mana per turn"),
            ("Lightning Bolt", 2, "Rare", 3, "+1 mana per turn"),
        ]
        name, cost, rarity, durability, effect = random.choice(artifacts)
        return ArtifactCard(name, cost, rarity, durability, effect)

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            card = random.choice([
                self.create_creature,
                self.create_spell,
                self.create_artifact
            ])()
            deck.append(card)
        return {'deck': deck, 'size': len(deck)}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
