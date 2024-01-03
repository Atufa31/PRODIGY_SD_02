import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 10

print("Welcome to the Guess the Number game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    try:
       
        guess = int(input("Enter your guess: "))
        
        attempts += 1

       
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:   
        print("Invalid input. Please enter a valid number.")


if attempts >= max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
