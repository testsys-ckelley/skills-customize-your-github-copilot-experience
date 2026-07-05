# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Set Up the Word Bank and Game State

#### Description
Create a predefined list of words and write the logic to randomly select one at the start of each game. Track the player's guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a list of at least 10 words to choose from
- Randomly select a word using the `random` module
- Initialize a counter for incorrect guesses remaining

### 🛠️ Build the Game Loop

#### Description
Implement the main game loop that accepts letter guesses from the player, updates the display, and checks for win or loss conditions.

#### Requirements
Completed program should:

- Prompt the player to enter a letter guess
- Display current progress in `_ _ _` format, revealing correct guesses
- Track and display incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display a win or lose message at the end