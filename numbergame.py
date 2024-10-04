import random
import time
low=1
high=100
guesses = 0
answer = random.randint(low, high)
is_running = True

print("Python Number Guessing Game")


while is_running:
    guess = input(f"Enter a number between {low} and {high} (q to quit): ").lower()
    if guess == 'q':
        break
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > high or guess < low:
            print("Number is out of range")
        elif guess > answer:
            print("Too high, try again!")
        elif guess < answer:
            print("Too low, try again!")
        else:
            print("CORRECT!")
            print(f'Your number of guesses was {guesses}')
            time.sleep(3)
            is_running = False

    else:
        print("Invalid input")
