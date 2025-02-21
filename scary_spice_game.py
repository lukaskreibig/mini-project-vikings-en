from vikingsClasses import *

in_any_bad_situation = "Something is badly wrong, game over."
ongoing_war_status_text = "Vikings and Saxons are still in the thick of battle."


def recruit_soldiers(soldier_type: str):
    count_soldiers = int(input(f"How many {soldier_type} soldiers will fight: "))
    
    for i in range(count_soldiers):
        if soldier_type == "Viking":
            name = input(f"What is the name of {soldier_type} {i+1}: ")

        health = int(input(f"Health points of {soldier_type} {i+1}: "))
        strength = int(input(f"Strength points of {soldier_type} {i+1}: "))

        if soldier_type == "Viking":
            war.vikingArmy.append(Viking(name, health, strength))
            # print(f"Viking {name} with HP {health} and SP {strength} has joined the force.")
        elif soldier_type == "Saxon":
            war.saxonArmy.append(Saxon(health, strength))
            # print(f"Some Saxon with HP {health} and SP {strength} has joined the force.")
        else:
            raise ValueError(in_any_bad_situation)
    

    print()
    print(f"The king of {soldier_type}s has recruited:")
    if soldier_type == "Viking":
        for viking in war.vikingArmy:
            print(f"- {viking.name} with {viking.health} HP and {viking.strength} SP.")
    elif soldier_type == "Saxon":
        for saxon in war.saxonArmy:
            print(f"- a soldier with {saxon.health} HP and {saxon.strength} SP.")
    print(f"All armed and dangerous. {soldier_type}s army is ready to fight!")
    print()

def create_armies():
    print()
    recruit_soldiers(soldier_type="Viking")
    print()
    recruit_soldiers(soldier_type="Saxon")
    print()
    user_interaction()

def game_viking_attack():
    print()
    print("Vikings attack!")
    battle_cry, attack_result = war.vikingAttack()
    print(battle_cry)
    print(attack_result)
    print("\n")

def game_saxon_attack():
    print()
    print("Saxons attack!")
    attack_result = war.saxonAttack()
    print(attack_result)
    print()


def user_interaction():
    if not (war.vikingArmy and war.saxonArmy):
        print("Armies need warriors.")
        create_armies()
        print()
    
    war_status = war.showStatus()
    while war_status == ongoing_war_status_text:
        user_action = int(input(" Press 1 for Vikings attack\n Press 2 for Saxons attack\n: "))
        if user_action == 1:
            game_viking_attack()
        if user_action == 2:
            game_saxon_attack()
        war_status = war.showStatus()
        print(war_status)
        print()
        
        
if __name__ == '__main__':
    print("Vikings and Saxons are in the state of war!")
    war = War()
    user_interaction()
