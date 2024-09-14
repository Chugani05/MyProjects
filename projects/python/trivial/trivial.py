import random

# Define the questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "How many planets are in the solar system?": "8",
    "Who wrote 'One Hundred Years of Solitude'?": "Gabriel García Márquez",
    "What is the longest river in the world?": "Nile",
    "In which year did man land on the Moon?": "1969"
}

def play_trivia():
    score = 0
    questions_list = list(questions.keys())
    random.shuffle(questions_list)
    
    for question in questions_list:
        user_answer = input(question + " ").strip()
        if user_answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {questions[question]}")
    
    print(f"Game over. Your score is {score} out of {len(questions)}")

# Start the game
if __name__ == "__main__":
    play_trivia()