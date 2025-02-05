
import random

trial = 3
player_score = 0
computer_score = 0

while True:
    player_choice = input("(rock/paper/scissors) Enter a choice: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == "rock" and computer_choice == "paper" or player_choice == "scissor" and computer_choice == "rock" or player_choice == "paper" and computer_choice == "scissors":
        print(f"You chose {player_choice} and Computer chose {computer_choice}")
        print("Computer Wins and You lose!")
        computer_score += 1
        print(f"""
        Score Board
        Computer {computer_score} | You {player_score}""")
        trial -= 1
        print(f"{trial} trials left!")
    elif computer_choice == "rock" and player_choice == "paper" or computer_choice == "scissor" and player_choice == "rock" or computer_choice == "paper" and player_choice == "scissors":
        print(f"You chose {player_choice} and Computer chose {computer_choice}")
        print("You Win and Computer lose!")
        player_score += 1
        print(f"""
        Score Board
        Computer {computer_score} | You {player_score}""")
        trial -= 1
        print(f"{trial} trials left!")
    elif player_choice == computer_choice:
        print(f"You chose {player_choice} and Computer chose {computer_choice}")
        print("Tie!")
        print(f"""
        Score Board
        Computer {computer_score} | You {player_score}""")
        trial -= 1
        print(f"{trial} trials left!")
    if trial == 0:
        if computer_score > player_score:
            print("computer wins!")
        elif player_score > computer_score:
            print("You win!")
        else:
            print("Tie!")
        break
        

#rock paper p
#rock scissors r
#paper scissors s
