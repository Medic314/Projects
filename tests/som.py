import random
common_index = ["stupid", "dumb", "idiot", "moron", "dummy"]
rare_index = ["alright", "ok", "sure"]
epic_index = ["awesome", "tubular"]
common = random.choice(common_index)
rare = random.choice(rare_index)
epic = random.choice(epic_index)
full_index = [common, common, common, common, common, common, rare, rare, rare, epic]
rolling = False
while rolling == False:
    common = random.choice(common_index)
    rare = random.choice(rare_index)
    epic = random.choice(epic_index)
    result = random.choice(full_index)
    print(result)
    rolling = bool(input("go again?: "))