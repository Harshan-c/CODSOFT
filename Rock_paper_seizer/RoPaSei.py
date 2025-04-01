import random

def get_user_choice():
    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1-3): ")
        
        if choice in ['1', '2', '3']:
            return ['rock', 'paper', 'scissors'][int(choice)-1]
        print("Invalid input! Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    winning_combinations = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    return 'user' if winning_combinations[user] == computer else 'computer'

def display_result(user, computer, result, scores):
    print("\n" + "="*30)
    print(f"You chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    print("-"*30)
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins! ")
    
    print(f"\nScore - You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
    print("="*30)

def play_game():
    """Main game function with score tracking"""
    scores = {'user': 0, 'computer': 0, 'tie': 0}
    
    print("\n" + "="*10)
    print("ROCK-PAPER-SCISSORS GAME")
    print("="*10)
    print("Rules: Rock beats scissors, scissors beat paper, paper beats rock")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        scores[result] += 1
        
        display_result(user_choice, computer_choice, result, scores)
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Scores:")
            print(f"You won {scores['user']} times")
            print(f"Computer won {scores['computer']} times")
            print(f"Ties: {scores['tie']}")
            print("\nThanks for playing! ")
            break

if __name__ == "__main__":
    play_game()