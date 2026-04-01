import random


def numbers_game():
    to_guess = random.randint(1, 100)
    guess_limit = 5
    guesses_taken = 0
    while guesses_taken < guess_limit:
        try:
            guess_input = int(input("Your guess: "))
            guesses_taken += 1
            print(f"Guesses left: {guess_limit - guesses_taken}")
            if guess_input > to_guess:
                print("Lower!")
            if guess_input < to_guess:
                print("Higher!")
            if guess_input == to_guess:
                print("Correct!")
                break

        except ValueError as e:
            print(f"Error: {e}")
        if guesses_taken == guess_limit and guess_input != to_guess:
            print(f"Guess limit reached! The number was {to_guess}.")


numbers_game()
