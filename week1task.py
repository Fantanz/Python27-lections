import random
print('Hello, Welcome to my game(RSP)')
print('"please write with capitalized')
player=input('Please thoes one of them Rock(R),Scissor(S), Paper(P):')

possible_actions = ["R", "P", "S"]
computer = random.choice(possible_actions)

if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "R":
    if computer == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "P":
    if computer == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "S":
    if computer == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print('choose(R,S,P)')        