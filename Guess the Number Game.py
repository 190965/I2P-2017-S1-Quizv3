import random

number=random.randint(0,100)
guess = int(input("Choose a number between 1-100:"))
tries=1

while guess !=number:
    if guess>number:
        print("Lower")
        guess=int(input("Take a Guess:"))
        tries+=1

    elif guess<number:
        print("Higher")
        guess=int(input("Take a guess"))
        tries+=1

    elif guess==number:
        print("You guessed it the number was",number)
        print("You only had",tries,"tries")

input("\n\n Press Enter Key to Exit")
