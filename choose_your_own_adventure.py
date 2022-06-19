user_name = input("Type your name:\n")
print("Welcome", user_name, "to this adventure")

answer = input("You are on a dirt road! You can turn left or right! Choose your path: ").lower() 
if answer == "left": 
    answer = input("You are in a river! You can swim across it or walk around. type walk to walk or swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across the river and were eaten by a crocodile!")
    elif answer == "walk":
        print("You walk around the river and died because of dehydration!! You lost the game!!")
    else:
        print("Invalid input!")

elif answer =="right":
    answer = input("You have come across a bridge but, it does not look to strong! Do you wish to continue?(yes/no)")
    if answer == "yes":
        answer = input("you were half way through when you heard a roap snapping! \nYou turn around to see that the bridge is going to fall. But there is a rope. Do you want to use the rope?(y/n)")
        if answer == "y":
            print("You managed to save yourself!")
        elif answer == "n":
            print("You fall off of the bridge and die!")    
        else:
            print("You lost the game!!")  
    
    elif answer == "no":
        print("You could not make it through the bridge!!")
        print("You lost!!")
    else:
        print("Invalid input!")          
else:
    print("Not a valid input!")
print("Thank you", user_name)