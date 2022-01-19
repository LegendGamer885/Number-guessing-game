import random

print ("Number Guessing game!")

number = random.randint(1,9)
chance = 5

print ("Guess a number between 1 to 9")

while (chance > 0):
    guess = int(input("Enter you number!"))
    if(guess == number):
        print ("Congrats you have won the game!!")
        break
    elif(guess < number):
        print("you have guessed a lower number")        
    else:
        print("You guessed a higher number") 
    chance -= 1
    print("you have",chance," chances remaining")

if(not chance > 0 ):
    print("Game Over you ran out of chances, Your number was", number)