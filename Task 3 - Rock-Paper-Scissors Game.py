import random
#Program for Rock-Paper-Scissors
print("<==Play Rock-Paper-Scissors==>")
print("[Gaming Rules]")
print('''Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Scissors vs Paper -> Scissors wins''')
choices = ["rock","paper", "scissors"]
playersc = 0
computersc = 0
while True:
    try:
        pchoice = int(input("Your Choice\n[Rock --> 1 Paper --> 2 Scissors --> 3 To Exit --> 0]"))
    except ValueError:
        print("Please enter a number!")
        continue

    if pchoice > 3 or pchoice < 0:
        print("Please enter a valid choice(0,1,2 or 3)!")
        continue

    if pchoice == 1:
        player = "rock"
    elif pchoice == 2:
        player = "paper"
    elif pchoice == 3:
        player = "scissors"
    else:
        print(f"Total player's wins: {playersc} & Computer's wins: {computersc}.")
        break
    print("Player's Choice:", player)

    computer = random.choice(choices)
    print("Computer's Choice:", computer)
    if computer == player:
        print("It is a Draw!\n")
    elif (player =='paper' and computer =='rock') or (player =='rock' and computer =='scissors') or (player == 'scissors' and computer == 'paper'):
        playersc +=1
        print("Player Wins!\n")
    else:
        computersc +=1
        print("Computer Wins\n")
