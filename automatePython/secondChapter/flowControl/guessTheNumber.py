import random

#select random number(int) between 1 and 100
secretNumber = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

#Ask the player to guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')

    elif guess > secretNumber:
        print('your guess is too high')

    else:
        break 

if guess == secretNumber:
    print('Congrats! You guessed the number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
