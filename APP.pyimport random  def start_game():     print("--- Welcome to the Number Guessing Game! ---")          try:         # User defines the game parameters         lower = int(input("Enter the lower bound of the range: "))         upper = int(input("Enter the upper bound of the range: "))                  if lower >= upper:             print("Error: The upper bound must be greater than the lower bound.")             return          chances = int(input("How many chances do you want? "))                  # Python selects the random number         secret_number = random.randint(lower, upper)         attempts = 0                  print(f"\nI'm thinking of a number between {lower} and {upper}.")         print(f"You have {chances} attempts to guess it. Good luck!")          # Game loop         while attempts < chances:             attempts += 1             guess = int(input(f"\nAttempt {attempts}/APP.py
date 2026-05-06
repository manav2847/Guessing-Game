import random

def start_game():
    print("--- Welcome to the Number Guessing Game! ---")
    
    try:
        # User defines the game parameters
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
        
        if lower >= upper:
            print("Error: The upper bound must be greater than the lower bound.")
            return

        chances = int(input("How many chances do you want? "))
        
        # Python selects the random number
        secret_number = random.randint(lower, upper)
        attempts = 0
        
        print(f"\nI'm thinking of a number between {lower} and {upper}.")
        print(f"You have {chances} attempts to guess it. Good luck!")

        # Game loop
        while attempts < chances:
            attempts += 1
            guess = int(input(f"\nAttempt {attempts}/{chances} - Enter your guess: "))

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} tries!")
                break
            elif guess < secret_number:
                print("Hint: The secret number is HIGHER than your guess.")
            else:
                print("Hint: The secret number is LOWER than your guess.")

            # Check if user has run out of lives
            if attempts == chances:
                print(f"\nGame Over! You've used all your chances. The number was {secret_number}.")

    except ValueError:
        print("Invalid input! Please enter whole numbers only.")

if __name__ == "__main__":
    start_game()
