import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'javascript', 'server', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 10
    guessed_word = display_word(word, guessed_letters)

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nCurrent word: " + guessed_word)
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts -= 1

        guessed_word = display_word(word, guessed_letters)

        if '_' not in guessed_word:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
