import random
secret_number = random.randint(1, 10)
max_attempts = 3
def welcome_message():
    print("\nwelcome to the Number Guessing Game!")
    print(f"you have {max_attempts} attempts to guess the correct number.")
def guess_recursive(attempts_left):
    guess = int(input("\nGuess the number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulation")
    else:
        print(f"wrong guess. attempts left: {attempts_left-1}")
        if attempts_left > 1:
            guess_recursive(attempts_left - 1)
        else:
            print(f"\nsorry, you couldn't guess the number. The correct number was {secret_number}.")

    welcome_message()
    guess_recursive(max_attempts)
    print(f"Memory address of secret number {secret_number} is {id(secret_number)}")            