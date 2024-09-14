# Hangman

## 1. **Word Selection:**
   - `choose_word()` randomly selects a word from a predefined list.

## 2. **Display Word:**
   - `display_word()` returns the word with guessed letters revealed and unguessed letters as underscores.

## 3. **Game Loop:**
   - The `play_hangman()` function manages the game logic:
     - Displays the current state of the word and the number of attempts left.
     - Prompts the user for a letter guess.
     - Checks the guess against the word and updates the game state.
     - Ends the game if the user guesses the word or runs out of attempts.

## 4. **Game Over:**
   - If the user runs out of attempts, the game ends and reveals the word. If they guess the word correctly, they win!