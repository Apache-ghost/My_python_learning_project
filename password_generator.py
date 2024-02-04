import string
import random
character=list(string.ascii_letters+string.digits+"!@#$%^&*()?")
def generate_password():
    password_length=int(input("how long would you like your password to be ? "))
    random.shuffle(character)
    password=[]
    for x in range(password_length):
        password.append(random.choice(character))
        random.shuffle(password)
        password=''.join(password)
        print(password)
option=input("Do you want to generate a password(yes or no)? ")
if option=="YES".lower():
    generate_password()
elif option.lower()=="NO":
    print("program terminated")
    quit()
else:
    print("invalid input , please enter yes or no!")
    quit()