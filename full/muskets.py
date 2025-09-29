import random

chips = 1000
tower = 1
room = 1
lives = 3
gem = 0
potion = 0
weights = False
knucks = 0
ending = "Bad"
starting_protection = True


print("(-= MUSKETS =-)")
playing = bool(input(f"Are you ready to ascend? (enter nothing for NO): "))

while playing == True:
    if knucks > 0:
        knucks_use = bool(input(f"Use your knuckledusters on this room? you currently have {knucks} "))
        if knucks_use == True:
            print(f"You shove the goons in the room and beat them with your Knuckledusters, but sadly, your beatdown was so good they broke in the process.")
            knucks -= 1
            room += 1
            level_start = False
        else: level_start = True
    else:
        level_start = True
    while level_start == True:
        if tower == 1:
            goal = int(((tower * 1000) + ((room - 1) * 500)) * ((tower ** 2) / tower))
        else:
            goal = int(((tower * 1000) + ((room - 1) * 500)) * ((tower ** 2) / 2))
        print(f"TOWER . . . {tower}")
        print(f"FLOOR . . . {room}")
        print(f"Your goal is {goal} chips. Gain that many chips to continue.")
        gained_chips = 0
        in_room = True 
        while in_room == True:

            print(f"{goal - gained_chips} chips left to earn. \n")
            if weights == True:
                print(f"You have sneakily put the weights on the dice, 1 will be rolled twice as often.")
            if gem > 0:
                print(f"The power of the gemstone resinates in your pocket. Wins will rake in more money. You have {gem} gems.")
            if potion > 0:
                print(f"The potion makes your head hurt, but it will protect you. You have {potion} potions.")
            if starting_protection == True:
                print(f"A mysterious force feild gathers around your person, it will protect you from losing chips for your first turn")

            bet = int(input(f"How much do you wish to bet? (Current chips: {chips}) "))
            prediction = int(input(f"What number do you NOT want rolled? "))
            
            if prediction < 1:
                prediction = 1
            if prediction > 6:
                prediction = 6

            if weights == False:
                diceComp = [1, 2, 3, 4, 5, 6]
            else:
                diceComp = [1, 1, 2, 3, 4, 5, 6]

            dice1 = random.choice(diceComp)
            dice2 = random.choice(diceComp)
            dice3 = random.choice(diceComp)

            print(f"\nThe results are \n. . . \n{dice1}, {dice2} and {dice3}\n")
            if dice1 == prediction or dice2 == prediction or dice3 == prediction:
                if chips <= 0:
                    if lives == 0:
                        print(f"Out of luck! maybe in another life...")
                        playing = False
                        ending = "xtra bad"
                        break
                    else:
                        lives -= 1
                        print(f"Ouch! you got some chips back... but you lost a life! current lives: {lives}\n")
                        chips = 300
                else:
                    if potion <= 0 and starting_protection == False:
                        print(f"Tough luck, Shepherd! You lost -{bet} chips!\n")
                        chips -= bet
                        gained_chips -= (bet // 4)
                        if chips <= 0:
                            if lives == 0:
                                print(f"Out of luck! maybe in another life...")
                                playing = False
                                ending = "xtra bad"
                                break
                            else:
                                 lives -= 1
                                 print(f"Ouch! you got some chips back... but you lost a life! current lives: {lives}\n")
                                 chips = 300
                    else:
                        print(f"You couldve lost {bet} chips, but the power of your potion prevented it! Its power has faded though...\n")
                        potion -= 1
                        starting_protection = False
            else:
                chips += (bet * (3 + gem))
                gained_chips += (bet * (3 + gem))
                starting_protection = False
                print(f"Good job, Shepherd! your bet has been muliplied by {2 + gem} and added to your chips. \n+{bet * (2 + gem)} CHIPS\n")
                if gained_chips >= goal:
                    print(f"You have escaped the floor! The vagabond has been waiting for you outside...\n")
                    if not room == 4:
                        room += 1
                    else:
                        room = 1
                        tower += 1
                    in_room = False
                    level_start = False

    if tower == 4:
        ending = "Good"
        playing = False
    if tower == 2 and room == 4:
        print("Tower 2 completed! 2500 chip bonus!")
        chips += 2500
    if tower == 1 and room == 4:
        print("Tower 1 completed! 1000 chip bonus!")
        chips += 1000
 
    shop_choice = bool(input(f"Do you wish to visit the Vagabond? "))
    if shop_choice == False:
        print(f"You punch him out of the way, crashing his back against the wall, and carry on.\n")
        level_start = True
        in_shop = False
    else:
        in_shop = True
    while in_shop == True:
        shop_inventory = ["Gemstone", "Potion", "Weights", "Knuckledusters"]
        shop_stock = random.choice(shop_inventory)
        if shop_stock == "Gemstone":
            price = 5000 * tower
            print(f"\nHe holds a shiny blue gemstone out to you, says it adds one to your ending multiplication. (Ex; x2 (starting) to x3)\n\nIt costs {price} chips.")
        elif shop_stock == "Potion":
            price = 1000 * tower
            print(f"\nHe holds out a potion, bubbling and stirring in his hand, says it can keep you from loosing chips for a turn.\n\nIt costs {price} chips.")
        elif shop_stock == "Weights":
            price = 7500
            print(f"\nHe holds out small weights, crafted to fill a dot on the dice. Says you can use it to make the 1 side on each die more likely to be rolled.\n\nIt costs {price} chips.")
        else:
            price = 10000 * tower
            print(f"\nHe holds out some knuckledusters, says you can use them to completely skip a room. By beating everyone up, of course.\n\nIt costs {price} chips.")

        shop_take = input(f"[REROLL] for 500 chips, [TAKE] this item, or [SKIP] this shop? you currently have {chips} chips. ")
        if shop_take == "take" or shop_take == "Take" or shop_take == "TAKE":
            if chips <= price:
                print(f"You dont have the money, dummy! get outta my sight!")
                in_shop = False
            else:
                chips -= price
                print(f"He thanks you for your patronage, and stuffs the chips into an unseen pocket. -{price} chips.\n")
                if shop_stock == "Gemstone":
                    gem += 1
                elif shop_stock == "Potion":
                    potion += 1
                elif shop_stock == "Weights":
                    weights = True
                else:
                    knucks += 1
                if chips > 0:
                    reroll2 = bool(input(f"reroll for more using 200 chips? hes willing to give you a discount for your previous purchase... you currently have {chips} chips. "))
                    if reroll2 == True:
                        print(f"He searches through his coat pocket again...")
                        chips -= 200
                    else:
                        in_shop = False
        elif shop_take == "skip" or shop_take == "Skip" or shop_take == "SKIP":
            print(f"He gives you a stern look, but waves you away to the next room, asking to reconsider later.\n")
            in_shop = False
        elif shop_take == "reroll" or shop_take == "Reroll" or shop_take == "REROLL":
            print(f"He searches through his coat pocket again...")
            chips -= 500
            if chips <= 0:
                print("you tried to reroll, but your pockets went dry! try again...")
                chips = 0
                in_shop = False
        else: 
            in_shop = False

if ending == "Bad":
    print("\n\nAnd with that... The Shepherd walked away from the towers, keeping his cards so close, not even he could see them. Maybe someone else will be more couragous...")
elif ending == "xtra bad":
    print(f"\n\nThe Shepherd's luck ran out, and he couldn't pay his debts. Beaten and bruised, he crawlled out of tower {tower} and bled out in the snow. Maybe someone else will be luckier...")
else:
    print(f"\n\nFinally, The Shepherd liberated the towers, and ranked in a big payout! he cashed out his {chips} dollars, I wonder what hes going to use it for... maybe in another life, we'll know.")