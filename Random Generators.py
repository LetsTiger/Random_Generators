# Random Number Generator (with range)
# Dice Roller
# Coin Flipper

import Modules.random_number as rn
import Modules.random_dice as rd
import Modules.random_coin as rc

# Main

list = [
    "\nWelchen Random Generator willst du benutzen?\n",
    "1: Random Number Generator (Zufallszahl zwischen zwei Grenzen)",
    "2: Dice Generator (Würfelgenerator)",
    "3: Coin Flipper (Kopf oder Zahl)\n"
]

for i in list:
    print(i)

generator_chosen = False

while not generator_chosen:
    try:
        chosen_generator = int(input("\nDeine Auswahl (1-3): "))
        
        if 0 < chosen_generator < 4:
            generator_chosen = True
        else:
            raise ValueError

    except ValueError:
        print(f"Bitte gib eine Ganzzahl zwischen 1 und 3 ein.")

if chosen_generator == 1:
    rn.generator()

elif chosen_generator == 2:
    rd.generator()

elif chosen_generator == 3:
    rc.generator()

input("\nZum beenden <Enter> drücken.")