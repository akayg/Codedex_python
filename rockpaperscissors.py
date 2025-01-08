player=int(input("Enter 1 for rock, \n2 for paper, \n3 for scissors: \n"))
import random
computer=random.randint(1,3)
if computer == 1:
  print("Computer chose rock")
elif computer == 2:
    print("Computer chose paper")
else:
    print("Computer chose scissors")
if player == computer:
  print("It's a draw")
elif player == 1:
    if computer == 2:
        print("Computer wins!")
    elif computer == 3:
        print("Player wins!")
elif player ==2 :
    if computer ==1 :
        print ("playerwins!")
    elif computer ==3 :
        print("Computer wins!")
elif player ==3 :
    if computer == 1:
        print("computer wins!")
    elif computer ==2:
        print("player wins!")
else:
    print("Invalid input")