import random

correct = random.choice(range(1,20))
print("The number is %s." % correct)

def guessNum():
    # global correct

    guess = int(input('Guess Number: '))
    if guess != correct:
        if guess > correct:
            print("Too high!")
            guessNum()

        elif guess < correct:
            print("Too low!")
            guessNum()
            
    elif guess == correct:
        print("You've guessed it!")

guessNum()
