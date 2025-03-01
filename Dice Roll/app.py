import random

def dice_Roll():
    while True:
        print("1. D4")
        print("2. D6")
        print("3, D20")
        print("4, Exit Program")
        choice = input("Select a Die to roll: \n")
        if(choice == str(1)):
            print("D4 was rolled, you rolled a: " + str(random.randint(1, 4)))
        elif(choice == str(2)):
            print("D6 was rolled, you rolled a: " + str(random.randint(1, 6)))
        elif(choice == str(3)):
            print("D20 was rolled, you rolled a: " + str(random.randint(1, 20)))
        elif(choice == str(4)):
            break
dice_Roll()