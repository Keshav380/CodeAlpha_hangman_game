"""
Hangman Game
------------
A simple text-based Hangman game played in the console.

Rules:
  * The computer picks a random word from a list of 5 predefined words.
  * The player guesses one letter at a time.
  * The player is allowed a maximum of 6 incorrect guesses.

Concepts used: random, while loop, if-else, strings, lists.

Run with:  python hangman.py
"""

import random

# ---------------------------------------------------------------------------
# 1. Game data
# ---------------------------------------------------------------------------

WORDS = ["python", "keyboard", "internship", "rainbow", "computer"]

MAX_WRONG_GUESSES = 6

# One drawing for each number of wrong guesses (0 to 6).
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]


# ---------------------------------------------------------------------------
# 2. Helper functions
# ---------------------------------------------------------------------------

def choose_word():
    """Return one random word from the predefined word list."""
    return random.choice(WORDS)


def build_display_word(secret_word, guessed_letters):
    """
    Build the word as the player sees it.
    Correctly guessed letters are shown, everything else is an underscore.
    Example: p _ t h _ n
    """
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    return display.strip()


def show_status(wrong_count, display_word, guessed_letters):
    """Print the hangman drawing and the current state of the game."""
    print(HANGMAN_STAGES[wrong_count])
    print("Word    : " + display_word)
    if guessed_letters:
        print("Guessed : " + ", ".join(sorted(guessed_letters)))
    print("Lives   : " + str(MAX_WRONG_GUESSES - wrong_count))
    print("-" * 40)


def get_guess(guessed_letters):
    """
    Ask the player for a single new letter.
    Keeps asking until the input is valid and has not been used before.
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly ONE letter.\n")
        elif not guess.isalpha():
            print("Letters only please (a-z).\n")
        elif guess in guessed_letters:
            print("You already guessed '" + guess + "'. Try another letter.\n")
        else:
            return guess


# ---------------------------------------------------------------------------
# 3. Main game loop
# ---------------------------------------------------------------------------

def play_game():
    """Play one full round of Hangman."""
    secret_word = choose_word()
    guessed_letters = []      # every letter the player has tried
    wrong_count = 0           # number of incorrect guesses so far

    print("\n=========================================")
    print("          WELCOME TO HANGMAN!")
    print("=========================================")
    print("The word has " + str(len(secret_word)) + " letters.")
    print("You are allowed " + str(MAX_WRONG_GUESSES) + " wrong guesses.\n")

    while True:
        display_word = build_display_word(secret_word, guessed_letters)
        show_status(wrong_count, display_word, guessed_letters)

        # Win check: no underscores left in the displayed word
        if "_" not in display_word:
            print("CONGRATULATIONS! You guessed the word: " + secret_word.upper())
            break

        # Lose check
        if wrong_count == MAX_WRONG_GUESSES:
            print("GAME OVER! You ran out of lives.")
            print("The word was: " + secret_word.upper())
            break

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct! '" + guess + "' is in the word.\n")
        else:
            wrong_count = wrong_count + 1
            print("Wrong! '" + guess + "' is not in the word.\n")


def main():
    """Run the game and let the player replay as many times as they want."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


# This makes sure the game only starts when the file is run directly.
if __name__ == "__main__":
    main()
