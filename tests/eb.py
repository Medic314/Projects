import random
print("==-== COOL TITLE HERE ==-==")

playing = bool(input("Play? "))
enemy_pool = ["skeleton", "slime", "dark knight", "reaper", "goblin"]

while playing == True:
    enemy = random.choice(enemy_pool)
    if enemy == "skeleton":
        health = 125
        attacks = ["swing", "block"]
    if enemy == "slime":
        health = 50
        attacks = ["approach", "absorb"]
    if enemy == "dark knight":
        health = 350
        attacks = ["swing", "sheild", "mace", "parry"]
    if enemy == "reaper":
        health = 250
        attacks = ["swing", "summon", "cloak", "aura farm"]
    if enemy == "goblin":
        health = 100
        attacks = ["swing", "block", "steal"]

player_turn = input("CHOOSE: [ATTACK] [BLOCK] [PARRY]")
