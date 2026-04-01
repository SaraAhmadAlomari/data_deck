from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===")
print("Testing Abstract Base Class Design:\n")

dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

print(f"CreatureCard Info: {dragon.get_card_info()}")

available_mana = 6
print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
print(f"Playable: {dragon.is_playable(available_mana)}")

game_state = {"board": []}
play_result = dragon.play(game_state)
print(f"Play result: {play_result}")

print("\nFire Dragon attacks Goblin Warrior:")
attack_result = dragon.attack_target(goblin)
print(f"Attack result: {attack_result}")

print("\nTesting insufficient mana (3 available):")
print(f"Playable: {dragon.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
