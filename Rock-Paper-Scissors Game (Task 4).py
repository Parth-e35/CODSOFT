import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user= 0
        self.computer= 0
        self.choices = ["rock", "paper", "scissors"]

    def computer_choice(self):
        return random.choice(self.choices)

    def winner(self, user, computer_choice):
        if user== computer_choice:
            return "It's a tie!"
        elif (user == "rock" and computer_choice == "scissors") or (user == "scissors" and computer_choice == "paper") or (user == "paper" and computer_choice == "rock"):
            self.user += 1
            return "You win!"
        else:
            self.computer += 1
            return "Computer wins!"

    def display(self):
        print("Score: You -",self.user_score,"Computer - ",self.computer_score)

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    
    game = RockPaperScissorsGame()
    
    while True:
        user = input("Enter Rock, Paper, or Scissors (or 'quit' to stop): ").lower()

        if user == 'quit':
            print("Thanks for playing!")
            break

        if user not in game.choices:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = game.computer_choice()
        result = game.determine_winner(user, computer_choice)
        
        print("\nYou chose: ",user)
        print("Computer chose: ",computer_choice)
        print(result)
        
        game.display()
        
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "no":
            print("Thanks for playing!")
            break
