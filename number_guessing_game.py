import random


def number_guessing_game():
    number = random.randint(0, 30)

    tries_left = 3
    tries_used = 0

    print(f"You have {tries_left} Tries.")

    while tries_left > 0:
        user_input = int(input("Guess the number: "))

        if user_input < number:
            print("Try a Greater Number.")
            tries_left -= 1
            tries_used += 1
            print(f"You have {tries_left} Tries Left.")
            continue

        elif user_input > number:
            print("Try a Smaller Number.")
            tries_left -= 1
            tries_used += 1
            print(f"You have {tries_left} Tries Left.")
            continue

        else:
            print("You Guessed the Correct Number.")
            print(f"You Guessed in {tries_used} Tries.")
            return f"The Number is {number}. "

    # print(f"You have {tries_left} Tries Left. You Lost")
    print("You Lost!")
    print(f"The Correct Number was {number}.")


number_guessing_game()
