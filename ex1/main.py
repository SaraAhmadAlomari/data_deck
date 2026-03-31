from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana")
cards = [spell, crystal, dragon]
deck = Deck()
for c in cards:
    deck.add_card(c)
print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")
print(f"Deck stats:{deck.get_deck_stats()}\n")
print("Drawing and playing cards:\n")

while deck.cards:
    card = deck.draw_card()
    print(f"Drew: {card}")
    print(f"Play result: {card.play({'board': []})}\n")
print("\nPolymorphism in action: Same interface, different card behaviors!")
