import random
#generate a random number between 1 and 10
number = random.randint(1, 10)

#Function GuessNum uses if statements to compare the guess variable to the number variables 
# and if it is too low or too high it print it on screen and runs the function again. If the guess matches the
# number it prints you're correct with the number
def GuessNum():
    global number
    guess = input("Guess a number between 1 and 10: ")
    if(int(guess) == (int(number))):
        print("You guessed correctly the number was " + str(number))
    elif(int(guess) > (int(number))): 
        print("That number is too high")
        GuessNum()
    elif(int(guess) < (int(number))):
        print("That number is too low")
        GuessNum()
GuessNum()