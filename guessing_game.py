import random
#user_guess
def guess(x):
    rand_number=random.randint(1,x)
    guess=0
    while guess!=rand_number:
        guess=int(input(f"enter a number between 1 and 10 {x}: "))
        if guess<rand_number:
            print("sorry ,guess again your guess is too low: ")
        elif guess>rand_number:
            print("sorry, guess again your guess is too high: ")
       
    print(f"congrats the guess the number {rand_number} correctly: ")
         
#computer_guess
def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
            feedback=input(f"is {guess} to high(H),too low(L), or correct(C): ").lower()
            if feedback=='h':
                    high=guess-1
            elif feedback=='l':
                    low=guess+1
    guess(50)
print(f"the computer guess your number {guess},correctly!")

