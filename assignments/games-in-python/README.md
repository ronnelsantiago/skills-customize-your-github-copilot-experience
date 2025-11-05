
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and handling user input. Students will implement the game loop, guess validation, and win/lose logic.

## 📝 Tasks

### 🛠️	Hangman Game

#### Description
Create a console-based Hangman game in Python. The program should pick a random word from a list, let the player guess letters, show progress in a "_ _ _" format, and end with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list in the program (or loaded from a simple file).
- Prompt the player for single-letter guesses and reject invalid input (non-letters, multiple characters, or previously guessed letters).
- Display the current word progress using underscores and revealed letters (e.g., _ a _ _ m a n).
- Track and display the number of incorrect guesses remaining (typical default: 6).
- End the game when the full word is guessed (win) or attempts run out (lose), and show an appropriate message.

#### Example session
```
Welcome to Hangman!
Word: _ _ _ _ _ _
Guesses left: 6
Guess a letter: a
Good guess! Word: _ a _ _ _ a
Guesses left: 6
Guess a letter: z
Sorry, no 'z'. Guesses left: 5
...
```

---

If you want an extra challenge, add these optional enhancements:

- Allow the word list to be loaded from a file.
- Show a simple ASCII-art hangman that progresses with incorrect guesses.
- Support whole-word guesses with appropriate win/lose handling.

