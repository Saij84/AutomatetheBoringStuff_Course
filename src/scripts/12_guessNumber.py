import random
#toDo
'''
-ask players name
-player need to guess a random number between 1 - 20

-player only have 6 guesses
-player need to be able to input a number
    -check need to be performed to ensure number us between 1 - 20
    -check that player is imputing int
-after input give player hint
    -"Your guess is too high"
    -"Your guess is too low"
    -"You guessed right, the number i thinking of is {number}
'''

randInt = random.randint(1, 20)

print("what is your name?")
playerName = input()

print("Hi {}".format(playerName))

for count in range(1, 7):
    print("Please guess a number from 1 - 20")
    guess = input()

    try:
        int(guess)
    except ValueError:
        print("Please enter a number")

    if int(guess) < randInt:
        print("Your guess is too low")
    elif int(guess) > randInt:
        print("Your guess is too high")
    else:
        print("Correct {}! The number is {}".format(playerName, randInt))
        break
