import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if player_choice == 'exit':
            print("Thanks for playing! See you next time.")
            break
        
        if player_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(options)
        print(f"Computer chooses: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
if __name__ == "__main__":
    rock_paper_scissors()