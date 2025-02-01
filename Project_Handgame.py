import random

'''
stone = 0
paper = 5
scissor = 2

'''

computer = random.choice([0, 5, 2])
user = input("choose any shape STONE, PAPER, SCISSOR : ")
dict = {"stone" : 0,
        "paper" : 5,
        "scissor" : 2}
reversedict = {0 : "stone",
               5 : "paper",
               2 : "scissor"}
you_num = dict[user]

print(f"You Choose {reversedict[you_num]}\nComputer Choose {reversedict[computer]}")

if(computer == you_num):
    print("Its a Draw, both have same shape ")
else:
    if(computer == 0 and you_num == 5):
        print("You are WIN ,CONGRATULATION !")

    elif(computer == 5 and you_num == 0):
        print("You are LOSS ,Better luck next time !")

    elif(computer == 5 and you_num == 2):
        print("You are WIN ,CONGRATULATION !")

    elif(computer == 2 and you_num == 5):
        print("You are LOSS ,Better luck next time !")

    elif(computer == 0 and you_num == 2):
        print("You are LOSS ,Better luck next time !")

    elif(computer == 2 and you_num == 0):
        print("You are WIN ,CONGRATULATION !")

    else:
        print("Code is Error , CHECK AGAIN ")