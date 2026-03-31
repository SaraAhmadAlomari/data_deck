from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===\n")

engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
print("Configuring Fantasy Card Game...")
engine.configure_engine(factory, strategy)
print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")

available_type = factory.get_supported_types()
print(f"Available types: {available_type}")

print("\nSimulating aggressive turn...")
turn_data = engine.simulate_turn()
print(f"Hand: [{', '.join(turn_data['hand'])}]")

print("\nTurn execution:")
print(f"Strategy: {turn_data['strategy']}")
print(f"Actions: {turn_data['actions']}")

print("\nGame Report:")
print(engine.get_engine_status())
print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
