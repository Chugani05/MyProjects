# Guess the Number

This Python code implements a simple number-guessing game where the user has to guess a randomly generated number between 1 and 20 within 5 attempts. Here’s a step-by-step explanation of how the code works:

## 1. **Importing the Random Module**
```python
import random
```
- The `random` module is imported to generate random numbers.

## 2. **Generating a Random Number**
```python
numero_aleatorio = random.randint(1, 20)
```
- `random.randint(1, 20)` generates a random integer between 1 and 20, inclusive. This number is stored in the variable `numero_aleatorio`.

## 3. **Welcome Message**
```python
print("Bienvenido al juego de adivinar el número.")
print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")
```
- These lines print a welcome message and explain the rules of the game to the user: they have 5 attempts to guess the secret number.

## 4. **Loop for User Attempts**
```python
for intento in range(1, 6):
```
- This `for` loop iterates from 1 to 5, giving the user 5 attempts to guess the number.

## 5. **User Input**
```python
numero_usuario = int(input(f"Intento {intento}: Adivina el número: "))
```
- `input()` prompts the user to enter their guess. `int()` converts the input from a string to an integer. The variable `numero_usuario` stores the user’s guess.

## 6. **Checking the Guess**
```python
if numero_usuario == numero_aleatorio:
    print(f"¡Felicidades! Has adivinado el número en el intento {intento}!")
    break
elif numero_usuario < numero_aleatorio:
    print("El número que buscas es más grande.")
else:
    print("El número que buscas es más pequeño.")
```
- If the user's guess matches the secret number (`numero_aleatorio`), a congratulatory message is printed, and the loop is exited using `break`.
- If the user's guess is less than the secret number, a hint is given that the number is larger.
- If the user's guess is greater than the secret number, a hint is given that the number is smaller.

## 7. **Post-Loop Message**
```python
if numero_usuario != numero_aleatorio:
    print(f"Lo siento, no has adivinado el número en 5 intentos. El número correcto era {numero_aleatorio}. ¡Inténtalo de nuevo!")
```
- After the loop ends (either because the user guessed the number correctly or used all 5 attempts), this `if` statement checks if the user did not guess the number. If the number was not guessed, it prints the correct number and a message encouraging the user to try again.

## Summary
The code provides a basic interactive guessing game where the user has 5 chances to guess a randomly generated number between 1 and 20. It gives feedback after each guess, guiding the user to the correct number or indicating how close they are.