# Rock, Paper, Scissors

This code is a simple Python implementation of the classic game "Rock, Paper, Scissors." Let's break down each part:

## 1. **Imports**
```python
import random
```
- The `random` module is imported to enable the program to randomly select a choice (rock, paper, or scissors) for the computer.

## 2. **Function Definition**
```python
def rock_paper_scissors():
```
- This line defines a function called `rock_paper_scissors()`. This function contains all the logic for playing the game.

## 3. **Options List**
```python
options = ["rock", "paper", "scissors"]
```
- This list defines the possible choices in the game: `"rock"`, `"paper"`, and `"scissors"`.

## 4. **Welcome Message**
```python
print("Welcome to Rock, Paper, Scissors!")
```
- This line prints a welcome message to the player when the game starts.

## 5. **Main Game Loop**
```python
while True:
```
- This starts an infinite loop that will keep running the game until the player decides to quit.

## 6. **Player Input**
```python
player_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
```
- The program prompts the player to enter their choice. The `input()` function captures this input, and `lower()` ensures that the input is converted to lowercase, making the comparison case-insensitive.

## 7. **Exit Condition**
```python
if player_choice == 'exit':
    print("Thanks for playing! See you next time.")
    break
```
- If the player types `'exit'`, the game will thank the player and end the loop using `break`, effectively ending the game.

## 8. **Invalid Input Check**
```python
if player_choice not in options:
    print("Invalid choice. Please try again.")
    continue
```
- If the player's input is not one of the valid options (`rock`, `paper`, or `scissors`), the program will inform the player that their choice is invalid and prompt them to try again. The `continue` statement restarts the loop without executing the rest of the code in the current iteration.

## 9. **Computer's Choice**
```python
computer_choice = random.choice(options)
print(f"Computer chooses: {computer_choice}")
```
- The computer randomly selects one of the options (`rock`, `paper`, or `scissors`) using `random.choice()`. The choice is then printed.

## 10. **Determine the Winner**
```python
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "paper" and computer_choice == "rock") or \
     (player_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
```
- The game logic to determine the outcome is implemented here:
  - If the player's choice is the same as the computer's, it's a tie.
  - If the player beats the computer according to the rules of Rock, Paper, Scissors (e.g., rock beats scissors), the player wins.
  - Otherwise, the player loses.

## 11. **Main Guard**
```python
if __name__ == "__main__":
    rock_paper_scissors()
```
- This line checks if the script is being run directly (not imported as a module elsewhere). If it is, the `rock_paper_scissors()` function is called, starting the game.