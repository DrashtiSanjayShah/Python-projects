import random 

user_pass = input("Enter your password: ")
password = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
guess = ""
while(guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[random.randint(0,25)]
        guess = str(guess_letter)+str(guess_letter)
        print(guess)
print("Your password is: ",guess)        
