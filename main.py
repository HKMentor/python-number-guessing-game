import random

print("Welcome to the Number Guessing Game! \n You got 5 attempts to game the number between 50 and 100 , Let's start the game")

number_to_guess = random.randrange(50, 100)

chances:int = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Enter your guess:"))
    
    if my_guess == number_to_guess:
        print(f"Congratulations! The number is {number_to_guess} and  You found it the right!! in the {guess_counter} attempts") 
        break
    
    elif guess_counter >= chances and my_guess !=  number_to_guess:
        print(f"Oops sorry , the number is {number_to_guess}better luck next time!")
    
    elif my_guess > number_to_guess:
        print("your guess is to high, try again!" )
        
    elif my_guess <number_to_guess:
        print("your guess is to low, try again!")
    
    
    
    
    