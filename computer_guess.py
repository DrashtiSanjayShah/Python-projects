import random

def computer_guess(x):
    low = 1
    higher = x
    feedback = ''
    while feedback != 'c':
        if low != higher:
            guess = random.randint(low, higher)
        else:
            guess = low
        guess = random.randint(low,higher)
        feedback = input(f"Is {guess} too high (H), too low(L), or correct (C)??").lower()
        if feedback == 'h':
            higher = guess - 1
            if feedback == "l":
               l = guess + 1
    print("YAYYYY! The computer guessed your number " + str(guess) + " correctly!!")
               
               
computer_guess(100)

