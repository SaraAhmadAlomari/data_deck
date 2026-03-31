from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("=== DataDeck Tournament Platform ===\n")

dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10, 8)
wizard = TournamentCard("Ice Wizard", 4, "Rare", 6, 6)
wizard.BASE_RATING = 1150

platform = TournamentPlatform()

print("Registering Tournament Cards...\n")
id1 = platform.register_card(dragon)
id2 = platform.register_card(wizard)

for c_id, card in [(id1, dragon), (id2, wizard)]:
    info = card.get_rank_info()
    interfaces = ["Card", "Combatable", "Rankable"]
    print(f"{card.name} (ID: {c_id}):")
    print(f"- Interfaces: {interfaces}")
    print(f"- Rating: {info['rating']}")
    print(f"- Record: {info['record']}\n")

print("\nCreating tournament match...")
result = platform.create_match(id1, id2)
print(f"Match result: {result}")

print("\nTournament Leaderboard:")
leaderboard = platform.get_leaderboard()
for i, entry in enumerate(leaderboard, 1):
    print(f"{i}. {entry['name']} - Rating: {entry['rating']} "
          f"({entry['record']})")

print("\nPlatform Report:")
print(platform.generate_tournament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
