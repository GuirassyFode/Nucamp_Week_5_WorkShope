import random

# Task 1: Guess the Number through User Input
def guess_random_number(tries, start, stop):
    target_number = random.randint(start, stop)

    while tries != 0:
        print(f"Tries remaining: {tries}")
        user_guess = int(input("Enter your guess: "))

        if user_guess == target_number:
            print("Congratulations, you've guessed the correct number!")
            return
        elif user_guess < target_number:
            print("Guess higher!")
        else:
            print("Guess lower!")

        tries -= 1

    print("Game Over. You could not guess the number.")

# Test Task 1
guess_random_number(5, 0, 10)

# Task 2: Guess the Number Programmatically through Linear Search
def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)

    for guess in range(start, stop + 1):
        print(f"Guess {guess}: {guess} ", end="")
        if guess == target_number:
            print("(Congratulations, you've guessed the correct number!)")
            return

    print("Game Over. The computer could not guess the number.")

# Test Task 2
guess_random_num_linear(5, 0, 10)

# Task 3: Guess the Number Programmatically using Binary Search
def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)

    low, high = start, stop

    while tries != 0:
        mid = (low + high) // 2
        print(f"Guess {mid}: {mid} ", end="")

        if mid == target_number:
            print("(Congratulations, you've guessed the correct number!)")
            return
        elif mid < target_number:
            low = mid + 1
        else:
            high = mid - 1

        tries -= 1

    print("Game Over. The computer could not guess the number.")

# Test Task 3
guess_random_num_binary(5, 0, 100)
