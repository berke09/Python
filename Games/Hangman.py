name = input("Enter name: ")
print("Hello " + name + ", time to play hangman!")

secret_word = "Metallica"
guess_string = ""  # This will store guessed letters
lives = 10  # Number of lives the player has

while lives > 0:
    try:
        character_left = 0

        # Display the word with guessed letters and dashes for unguessed ones
        for character in secret_word:
            if character.lower() in guess_string.lower():
                print(character, end=" ")
            else:
                print("-", end=" ")
                character_left += 1

        print()  # For new line after displaying the word

        # If there are no characters left to guess, player wins
        if character_left == 0:
            print("You won!!!")
            break

        # Ask for the player's guess
        guess = input("Guess a letter: ").lower()

        # Check if input is valid (only one letter at a time)
        if len(guess) != 1 or not guess.isalpha():
            raise ValueError("Please enter only one letter at a time.")

        # Check if the letter has already been guessed
        if guess in guess_string:
            raise ValueError(f"You already guessed '{guess}'. Try a different letter.")

        # Add the guessed letter to the guessed string
        guess_string += guess

        # If the guessed letter is not in the secret word, subtract lives
        if guess not in secret_word.lower():
            lives -= 1
            print("Wrong!")
            print(f"You have {lives} lives left.")

            # If the player runs out of lives
            if lives == 0:
                print(f"You died! The word was: {secret_word}")
                break

    except ValueError as e:
        print(e)  # Print the error message and continue the game
        continue

    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting gracefully...")
        break
