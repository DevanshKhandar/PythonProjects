print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
c1 = input('You`re at a crossroad, where do you want to go? type "Left" or "Right".\n').lower()

if c1 == "left":
    c2 = input('you\'ve come to a lake. There is a island in the middle of the lake. '
               'Type "Wait" to wait for a boat. '
               'Type "Swim" to swim across.\n').lower()
    if c2 == "wait":
        c3 = input("You arrive at the island unharmed. "
              "There is house with Three doors. "
              "One Red, One Yellow and One Blue. "
              "Which Colour do you choose?\n").lower()
        if c3 == "red":
            print("It's a room full of fire. Game over.")
        elif c3 == "yellow":
            print("You found the treasure. you win!")
        elif c3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("Sorry you fell into the hole. Game Over.")
