import random


comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "R"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "P"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "S"
    else:
        print("Invalid option")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "R"
    elif comp_choice == 2:
        comp_choice = "P"
    else:
        comp_choice = "S"
    return comp_choice

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "R":
        if comp_choice == "R":
            print("You chose rock. Computer chose rock. It's a tie.")
        elif comp_choice == "P":
            print("You chose rock. Computer chose paper. You lose.")
            comp_wins += 1

        elif comp_choice == "S":
            print("You chose rock. Computer chose scissors. You win.")
            player_wins += 1

    elif user_choice == "P":
        if comp_choice == "R":
            print("You chose paper. Computer chose rock. You win.")
            player_wins += 1
            
        elif comp_choice == "P":
            print("You chose paper. Computer chose paper. It's a tie.")

        elif comp_choice == "S":
            print("You chose paper. Computer chose scissors. You lose.")
            comp_wins += 1

    elif user_choice == "S":
        if comp_choice == "R":
            print("You chose scissors. Computer chose rock. You lose.")
            comp_wins += 1
            
        elif comp_choice == "P":
            print("You chose scissors. Computer chose paper. You win.")
            player_wins += 1
            
        elif comp_choice == "S":
            print("You chose scissors. Computer chose scissors. It's a tie.")
                 
    print("")
    print("Player wins: " +str(player_wins))
    print("Computer wins: " +str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Yes", "yes", "y"]:
        pass
    elif user_choice in ["No", "no", "n"]:
        break
    else:
        break
            
