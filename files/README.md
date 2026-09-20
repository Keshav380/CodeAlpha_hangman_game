# Hangman Game (Python)

A simple text-based Hangman game built as **Task 1** of my internship.
The player guesses a hidden word one letter at a time, with a limit of 6 incorrect guesses.

## Features

- Random word chosen from a list of 5 predefined words
- Maximum of 6 incorrect guesses
- ASCII hangman drawing that updates after every wrong guess
- Shows the word progress, already-guessed letters and remaining lives
- Input validation (single letter only, no repeated guesses)
- Option to play again after each round

## Key Concepts Used

`random` · `while` loop · `if-else` · `strings` · `lists`

## Requirements

- Python 3.6 or newer
- No external libraries needed (only the built-in `random` module)

## How to Run in VS Code

1. Install [Python](https://www.python.org/downloads/) and tick **"Add Python to PATH"** during installation.
2. Install [Visual Studio Code](https://code.visualstudio.com/).
3. In VS Code, open the **Extensions** panel (`Ctrl+Shift+X`) and install the official **Python** extension by Microsoft.
4. Open this project folder: **File → Open Folder…** and select the `hangman-game` folder.
5. Open `hangman.py`.
6. Run it in either way:
   - Click the **▶ Run Python File** button in the top-right corner, **or**
   - Open the terminal (`Ctrl+~`) and run:

     ```bash
     python hangman.py
     ```

     On macOS/Linux use `python3 hangman.py`.
7. The game starts in the terminal. Type a letter and press **Enter** to guess.

## Sample Output

```
=========================================
          WELCOME TO HANGMAN!
=========================================
The word has 6 letters.
You are allowed 6 wrong guesses.

     +---+
     |   |
         |
         |
         |
         |
    =========

Word    : _ _ _ _ _ _
Lives   : 6
----------------------------------------
Guess a letter: p
Correct! 'p' is in the word.
```

## How to Upload This Project to GitHub

### Option A — Using the GitHub website (easiest)

1. Log in at [github.com](https://github.com) and click **+ → New repository**.
2. Name it `hangman-game`, keep it **Public**, and click **Create repository**.
3. On the new repo page, click **uploading an existing file**.
4. Drag `hangman.py`, `README.md` and `.gitignore` into the box.
5. Write a commit message like `Add Hangman game` and click **Commit changes**.

### Option B — Using Git in the VS Code terminal

Make sure [Git](https://git-scm.com/downloads) is installed, then run these commands inside the project folder:

```bash
git init
git add .
git commit -m "Task 1: Hangman game"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/hangman-game.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. The first push will ask you to sign in to GitHub.

## Project Structure

```
hangman-game/
├── hangman.py     # main game file
├── README.md      # project documentation
└── .gitignore     # files Git should ignore
```
