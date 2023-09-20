from random import choice

p_wins = 0
comp_wins = 0

print("...Rock")
print("......Paper")
print(".........Scissors\n")
winning_score = int(input("Set the score to win: "))
print("Enter 'q' or 'quit' at any time to leave.\n")

while p_wins < winning_score and comp_wins < winning_score:
    print(f"Player Score: {p_wins}    Computer Wins {comp_wins}")
    rps = ["rock", "paper", "scissors"]
    comp = choice(rps)
    player = input("Choose rock, paper, scissors: ").lower().strip()

    if player in rps or player == "quit" or player == "q":
        print(f"\nComputer plays {comp}.")
        if player in ("quit", "q"):
            break
        elif comp == player:
            print("It's a tie!")
        elif comp == "rock" and player == "paper":
            print("You win the match!")
            p_wins += 1
        elif comp == "paper" and player == "scissors":
            print("You win the match!")
            p_wins += 1
        elif comp == "scissors" and player == "rock":
            print("You win the match!")
            p_wins += 1
        else:
            print("Computer wins the match!")
            comp_wins += 1
    else:
        print("Enter a valid choice")
print()
if winning_score == 0 or player in ("quit", "q"):
    print("Goodbye!")
elif p_wins > comp_wins:
    print("Congratulations! You won the game!")
elif p_wins == comp_wins:
    print("The game is a tie!")
else:
    print("Oh no! The computer won the game.")
print(f"FINAL SCORES...Player Score: {p_wins}    Computer Score: {comp_wins}")