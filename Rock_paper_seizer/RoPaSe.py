import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def display_score(user_score, computer_score, ties):
    print("\nCurrent Score:")
    print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    print("-----------------------------")

def play_game():
    print("Welcome to Rock Paper Scissors with Score Tracking!")
    print("-----------------------------")
    
    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            user_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("It's a tie!")
        
        display_score(user_score, computer_score, ties)
        
        play_again = input("\nPlay another round? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Results:")
            print("-----------------------------")
            print(f"Total Rounds Played: {user_score + computer_score + ties}")
            print(f"You won: {user_score} rounds")
            print(f"Computer won: {computer_score} rounds")
            print(f"Ties: {ties}")
            
            if user_score > computer_score:
                print("\nCongratulations! You are the overall winner!")
            elif computer_score > user_score:
                print("\nComputer is the overall winner. Better luck next time!")
            else:
                print("\nThe game ended in a tie overall!")
            
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()