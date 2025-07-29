import random
import sys
''' 
-1 for water
0 for gun
1 for snake

'''
dict = {
    "w" : -1,
    "g" : 0,
    "s" : 1,
}

reversedict = {
    -1 : "water",
    0 : "gun",
    1 : "snake",
}

list = ("s" , "w" , "g")
variable_choice = input("Enter your choice: ")
choice = variable_choice.strip().lower()
if(choice in list):
    pass
else:
    print("You should type only s w or g")
    sys.exit()

you = dict[choice]

computer = random.choice([-1, 0 ,1])
print(f"Your choice :{reversedict[you]}")
print(f"Computer's choice :{reversedict[computer]}")

if(you == computer):
    print("Draw!")
else:
    if(computer == 1 and you == -1):
        print("you win")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == -1 and you == 1):
        print("you lose")
    elif(computer == -1 and you == 0):
        print("you lose")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you lose")
    else:
        print("Try again dumbass")



