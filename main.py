def main():
    art = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"'"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
 """
    print(art)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = input("You're at a cross road, which way do you want to go? Type 'left' or 'right'\n")
    if direction.lower() == "left":
        left_turn = input("This direction is flooded. Swim or wait?\n")
        if left_turn.lower() == "wait":
            door = input("You waited for the flooding to subside and find a cellar. Inside the cellar, a doorway stands before you. Would you \nlike to open the 'red' door or 'blue' door or 'yellow' door?\n")
            if door.lower() == "red":
                print("You were burned in a fire. Game over.")
            elif door.lower() == "blue":
                print("Eaten by beasts. Game over.")
            elif door.lower() == 'yellow':
                print("You win!")
            else:
                print("Game over.")
        else:
            print("You got stuck in a flood and drowned. Game over.")
    else:
        print("You fall into a hole. Game over.")

if __name__ == "__main__":
    main()