# W6_Task:6- 
# Mini project:- Command-Line RPG Game (Text-Based Project Design)

import random
import json

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=10, defense=5)
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)

class Enemy(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

class Game:
    def __init__(self, player):
        self.player = player
        self.locations = ["Forest", "Cave", "Village"]
    
    def explore(self):
        place = random.choice(self.locations)
        print(f"You arrive at the {place}.")
        
        if random.random() < 0.5:  # enemy encounter
            enemy = Enemy("Goblin", 30, 8, 2)
            print(f"A wild {enemy.name} appears!")
            self.combat(enemy)
        else:
            item = "Potion"
            print(f"You found a {item}!")
            self.player.add_item(item)

    def combat(self, enemy):
        while enemy.is_alive() and self.player.is_alive():
            print(f"{self.player.name} HP: {self.player.hp} | {enemy.name} HP: {enemy.hp}")
            action = input("Do you want to (a)ttack or (r)un? ").lower()
            
            if action == "a":
                enemy.take_damage(self.player.attack)
                if enemy.is_alive():
                    self.player.take_damage(enemy.attack)
            elif action == "r":
                print("You fled the battle!")
                return
        
        if self.player.is_alive():
            print(f"You defeated {enemy.name}!")
        else:
            print("You have been defeated... Game Over!")

    def save(self):
        data = {
            "name": self.player.name,
            "hp": self.player.hp,
            "attack": self.player.attack,
            "defense": self.player.defense,
            "inventory": self.player.inventory
        }
        with open("save.json", "w") as f:
            json.dump(data, f)
        print("Game Saved!")

    def load(self):
        try:
            with open("save.json", "r") as f:
                data = json.load(f)
                self.player = Player(data["name"])
                self.player.hp = data["hp"]
                self.player.attack = data["attack"]
                self.player.defense = data["defense"]
                self.player.inventory = data["inventory"]
            print("Game Loaded!")
        except FileNotFoundError:
            print("No saved game found.")

player = Player("Hero")
game = Game(player)

while player.is_alive():
    game.explore()
    if input("Do you want to save and quit? (y/n): ").lower() == "y":
        game.save()
        break
