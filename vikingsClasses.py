import random

# Soldier


class Soldier:
    def __init__(self, health: int, strength: int):
        self.strength = strength
        self.health = health
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage: int):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return ("Odin Owns You All!")

    def receiveDamage(self, damage: int):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage: int) -> str:
            self.health = self.health - damage
            if self.health > 0:
                return f"A Saxon has received {damage} points of damage"
            else: return "A Saxon has died in combat"

# Davicente
class War():

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking:Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon:Saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_viking: Viking = random.choice(self.vikingArmy)
        random_saxon: Saxon = random.choice(self.saxonArmy)
        damage = random_viking.attack()
        result = random_saxon.receiveDamage(damage)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return result

    def saxonAttack(self):
        random_saxon: Saxon = random.choice(self.saxonArmy)
        random_viking: Viking = random.choice(self.vikingArmy)
        damage = random_saxon.attack()
        result = random_viking.receiveDamage(damage)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



