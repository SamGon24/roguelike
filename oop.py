class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power 
    
    def is_alive(self):
        return self.hp > 0
  
    def take_damage(self, amount):
        self.hp -= amount

    def attack(self, other):
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
        other.take_damage(self.attack_power)  # updated here too

# Create characters
knight = Character("Knight", 55, 100)
goblin = Character("Goblin", 20, 80)

round = 1
while knight.is_alive() and goblin.is_alive():
    print(f"\n--- Round {round} ---")
    knight.attack(goblin)
    print(f"{goblin.name} HP: {goblin.hp}")

    if goblin.is_alive():
        goblin.attack(knight)
        print(f"{knight.name} HP: {knight.hp}")
    
    round += 1

print("\n--- Battle Over ----")
if knight.is_alive():
    print(f"{knight.name} wins!")
else:
    print(f"{goblin.name} wins!")





