import random, sys

# doesn't need sys import

max = int(input("Max Number: "))
print('The number is between 1 and %s.'% max)

correct = random.choice(range(1,max))
# print("The number is %s." % correct)

def guessNum():
    # global correct

    guess = int(input('Guess Number: '))
    if guess > max:
        print('Error: exceeding max!\n')
        guessNum()

    if guess != correct:
        if guess > correct:
            print("Too high!\n")
            guessNum()

        elif guess < correct:
            print("Too low!\n")
            guessNum()
            
    elif guess == correct:
        print("You've guessed it!\n")
        sys.exit()

guessNum()
