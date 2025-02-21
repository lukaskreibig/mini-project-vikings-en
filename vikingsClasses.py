from random import choice

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
        lst_battlecry = ["Odin owns you all!", "In the name of Thor!", "SKOLL", "Fear no death!"]
        battlecry = self.name + " shouts: " + choice(lst_battlecry)
        return battlecry

    def receiveDamage(self, damage: int):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage. HP left: {self.health}"
        else: return f"{self.name} has died in act of combat and is taken to Valhalla."

# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage: int) -> str:
            self.health = self.health - damage
            if self.health > 0:
                return f"A Saxon has received {damage} points of damage. HP left: {self.health}"
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
        random_viking: Viking = choice(self.vikingArmy)
        random_saxon: Saxon = choice(self.saxonArmy)
        battle_cry = random_viking.battleCry()
        damage = random_viking.attack()
        attack_result = random_saxon.receiveDamage(damage)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return battle_cry, attack_result

    def saxonAttack(self):
        if not self.saxonArmy:
            return None
        random_saxon: Saxon = choice(self.saxonArmy)
        random_viking: Viking = choice(self.vikingArmy)
        damage = random_saxon.attack()
        attack_result = random_viking.receiveDamage(damage)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return attack_result


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


