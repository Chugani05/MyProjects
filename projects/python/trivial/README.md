# Trivial

Here's a brief explanation of the code:

## 1. **Question Dictionary:** 
   - `questions` is a dictionary with trivia questions as keys and their answers as values.

## 2. **`play_trivia` Function:**
   - **Shuffle Questions:** Randomizes the order of questions.
   - **Ask Questions:** Loops through each question, asking the user for an answer.
   - **Check Answers:** Compares the user’s answer to the correct answer (case-insensitive). Updates the score if the answer is correct.
   - **Print Results:** Displays whether the user was correct or not and shows the final score at the end of the game.

## 3. **Game Start:**
   - The `if __name__ == "__main__":` block ensures that the `play_trivia()` function runs when the script is executed.