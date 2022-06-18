print("Welcome to THE WORLD OF GAMES!!!!!!!!")
playing = input("Do you want to play?: (yes/no)")
if playing == "yes":
    print("CONTINUE HERE!!")      
    score = 0     
    name = input("Enter your name: ")
    print("Welcome", name)
    answer = input("1. What is the full form of CPU? ")
    if answer == "Central Processing Unit":
        print("That is the correct answer!!")
        score += 1
        print("The next question will be displayed now!!")
    else:
        print("This is the wrong answer!!")
    answer = input("2. What does RAM do? ")
    if answer == "Stores data in memory temporaryly".lower():
        print("This is the correct answer!!")
        score += 1
        print("The next question will be displayed now!!")
    else:
        print("This is the wrong answer!!")
    answer = input("3. What is the fullform of OOP?")
    if answer == "Object Oriented Programming":
        print("This is the correct answer")
        score += 1
    else:
        print("This is the wrong answer!!")
    print("You got " + str(score) + " questions correct!!")
    print("You got " + str((score/3) * 100) + " !!")
else:
    print("EXIT") 
