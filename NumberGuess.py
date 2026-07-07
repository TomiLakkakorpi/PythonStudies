# Number guess game
# arvotaan numero
# kysytään käyttäjältä arvaus
# näytetään onko arvo yli vai alle
# jos arvo on lähellä (yli 5 tai alle 5) niin näytetään "lähellä"

from random import random

GuessValue = int(random() * 100)
varGuess = 0
varGuessCount = 0

print("Guess a number between 1 and 100")

while (varGuessCount < 20):
    varGuessCount += 1

    varGuess = int(input("Your guess: "))

    if(varGuess == GuessValue):
        print("You guessed it right!")
        exit()
    elif(abs(varGuess - GuessValue) <= 5):
        if(varGuess > GuessValue):
            print("Close, too high!")
        else:
            print("Close, too low!")
    elif(varGuess > GuessValue):
        print("Too high!")
    else:
        print("Too low!")