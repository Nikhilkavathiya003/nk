print("A joyful pygame ,{Stone,Paper and scissor}")
import random
print("s for stone\n" "p for  paper \n""r for scissor")
i=0
com=0
user=0
pointU=0
pointC=0
list=['s','p','r']
while i<5:
    user=input("enter your choice:")
    com=random.choice(list)
    if user==com:
        print("It's tie")
        print(f"computer choice is {com}")
        print("your choice and computer choice are same here ! Ha Ha Haaaha")

    #for s
    elif user=="s" and com=="p":
        print("computer win this turn")
        print("try to win the next turn , You can do it")
        print(f"computer choice is {com}")
        pointC= pointC + 1
        print(f"your point is {pointU},computer point is {pointC}")

    elif user=="s" and com=="r":
        print("You win this round")
        print(f"computer choice is {com}")
        print("play next turn")
        pointU=pointU+1
        print(f"your point is {pointU},computer point is {pointC}")

    #for p
    elif user=="p" and com=="r":
        print("computer win this round")
        print("try to win the next turn , You can do it")
        print(f"computer choice is {com}")
        pointC = pointC + 1
        print(f"your point is {pointU},computer point is {pointC}")

    elif user=="p" and com=="s":
        print("You win this round")
        print("Play next turn")
        print(f"computer choice is {com}")
        pointU = pointU + 1
        print(f"your point is {pointU},computer point is {pointC}")

    #for r
    elif user=="r" and com=="p":
        print("you win this round")
        print("play next turn")
        print(f"computer choice is {com}")
        pointU = pointU + 1
        print(f"your point is {pointU},computer point is {pointC}")

    elif user=="r" and com=="s":
        print("computer win this round")
        print("try to win the next turn , You can do it")
        print(f"computer choice is {com}")
        pointC = pointC + 1
        print(f"your point is {pointU},computer point is {pointC}")
    else:
        print("enter valid choice")
        print("You loose this game and restart the game to play")
        break

    i=i+1
    print("you have only",5-i,"turns left")

if pointU==pointC:
    print("Game is tie")
elif pointC>pointU:
    print("Sorry ! Computer win the game")
else:
    print("Congratulations ! You win the game")