import random
random_number = random.randint(0, 50)

max_trys = 7

# Loop for user input
for trys in range(1, max_trys + 1):
    user_guess = int(input("Guess the number (between 0 and 50): "))

    if user_guess == random_number:
        print("You guessed correctly!")
        break
    elif user_guess < random_number:
        print("The value is too low.")
    else:
        print("The value is too high.")

    if trys == max_trys:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")
        break