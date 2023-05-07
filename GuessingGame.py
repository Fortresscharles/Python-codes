import random
guess_count = 0
guess_limit = 5
while(guess_count<guess_limit):
    AI_guess = random.randint(1,10)
    fortress_guess=int(input("enter a number between 1 - 10 ::"))
    guess_count+=1
    if(fortress_guess== AI_guess):
        print("CORRECT")
        break
    elif(fortress_guess> AI_guess):
        print("your guess is too high")
    elif(fortress_guess< AI_guess):
        print("your guess is too low")
    else:
        print("end")

