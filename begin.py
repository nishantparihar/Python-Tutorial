import random


def get_choices():
    choice = ["rock", "paper", "scissors"]
    player_choice = int(input("Give player choice (1: rock, 2: paper, 3: scissors): "))
    player_choice = choice[player_choice-1]
    computer_choice = random.choice(choice)

    choices = {"player":player_choice, "computer":computer_choice}

    return choices

#choices = get_choices()

def check_win(player, computer):
    print(f"Player chose {player} and computer chose {computer}")
    if player == computer:
        return "it's a tie!!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!! You won!!"
        else:
            return "Papper covers rock, You loose"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors, You loose"
        else:
            return "Scissors cuts papper!!, You won!!"
    elif player == "paper":
        if computer == "rock":
            return "Papper covers rock!!, You won!!"
        else:
            return "Scissors cuts papper, You loose"



choices = get_choices()
out = check_win(choices["player"], choices["computer"])
print(out)