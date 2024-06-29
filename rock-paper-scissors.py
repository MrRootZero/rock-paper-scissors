options = ["rock", "paper", "scissors"]

user1 = input("User 1: Enter rock, paper, or scissors: ").lower()
user2 = input("User 2: Enter rock, paper, or scissors: ").lower()

if user1 not in options or user2 not in options:
    print("Invalid input! Please enter rock, paper, or scissors.")
else:
    if user1 == user2:
        print("It's a tie!")
    elif (user1 == "rock" and user2 == "scissors") or (user1 == "paper" and user2 == "rock") or (user1 == "scissors" and user2 == "paper"):
        print("User 1 wins!")
    else:
        print("User 2 wins!")
