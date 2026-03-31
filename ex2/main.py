from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
card_methods = [m for m in dir(Card) if not m.startswith('_')]
combat_methods = [m for m in dir(Combatable) if not m.startswith('_')]
magic_methods = [m for m in dir(Magical) if not m.startswith('_')]

print(f"- Card: {card_methods}")
print(f"- Combatable: {combat_methods}")
print(f"- Magical: {magic_methods}")

warrior = EliteCard('Arcane Warrior', 6, 'Legendary', 5, 10, 8)
print("\nPlaying Arcane Warrior (Elite Card):\n")
print("Combat phase:")
attack_result = warrior.attack("Enemy")
print(f"Attack result: {attack_result}")

defend_result = warrior.defend(5)
print(f"Defense result: {defend_result}")

print("\nMagic phase:")
spell_result = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
print(f"Spell cast: {spell_result}")
mana_result = warrior.channel_mana(3)
print(f"Mana channel: {mana_result}")
print("\nMultiple interface implementation successful!")
