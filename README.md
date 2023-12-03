# Number Guessing Game

## Overview

This repository contains a number guessing game implemented in three different ways. The game scenarios include:

1. User guessing a randomly generated number.
2. Computer guessing a randomly generated number using linear search.
3. Computer guessing a randomly generated number using binary search.

## How to Play

### Task 1: Guess the Number through User Input

1. Create a new file in your `week5/` folder named `workshop5.py`.
2. Import the `random` module into this file.
3. Write a function named `guess_random_number()` following the instructions provided.
4. Test the function by calling it with appropriate arguments.

### Task 2: Guess the Number Programmatically through Linear Search

1. Write a function named `guess_random_num_linear()` following the instructions.
2. Test the function by calling it with appropriate arguments.

### Task 3: Guess the Number Programmatically using Binary Search

1. Write a function named `guess_random_num_binary()` following the instructions.
2. Test the function by calling it with appropriate arguments.

## Running the Tests

- Ensure that you have the required Python environment set up.
- Run the test driver code for each task to check for both success and failure cases.

```python
# Example: Test Task 1
guess_random_number(5, 0, 10)

# Example: Test Task 2
guess_random_num_linear(5, 0, 10)

# Example: Test Task 3
guess_random_num_binary(5, 0, 100)