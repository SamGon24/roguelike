class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def is_alive(self):
        return self.hp > 0
  
    def take_damage(self, amount):
        self.hp -= amount
    def attack(self, other):
       print(f"{self.name} attacks {other.name} for {self.attack} damage!")
       other.take_damage(self.attack)    
       
knight = Character("knight", 55, 100)
goblin = Character("Goblin", 20, 3)

round = 1 # round-based game
while knight.is_alive() and goblin.is_alive():
    print(f"\n--- Round {round} ---")
    knight.attack(goblin)
    print(f"{goblin.name} HP: {goblin.hp}")

    if goblin.is_alive():
        goblin.attack(knight)
        print(f"{knight.name} HP: {hero.hp}")
    
    round += 1

print ("\n--- Battle Over ----")
if knight.is_alive():
    print("{hero.name} wins!")
else:
    print("{goblin.name} wins!")




