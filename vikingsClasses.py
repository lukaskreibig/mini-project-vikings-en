import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.healf > 0:
            return f"{self.name} has received {damage} points of damage."
        else:
            return f"{self.name} has died in act of combat."

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.healf > 0:
            return f"A Saxon has received {damage} points of damage."
        else:
            return f"A Saxon has died in combat."

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        attack_result = random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return (attack_result, random_viking.strength)
    
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        attack_result = random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return (attack_result, random_saxon.strength)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    
