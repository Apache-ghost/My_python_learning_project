name=input("Enter your name: ")
print("welcome ",name,"to this adverture")

answer=input("You are on a dirt road,it has come to an end and you can go left or right. which way would you like to go ?").lower()

if answer == "left":
    print("You come to a river you can walk around it or swim accross .Type walk to walk around or swim to swim accross: ").lower()

    if answer == "swim":
        print("you swim around and you eaten by an alliagator ")
    elif answer == "walk":
        print("you walk around and you lost the game")
    else:
        print("you didnot enter a valid option , you lost the game")

elif answer == "right":
    print("you come accross a brigde ,do you want to cross it or head back(cross/back)? ")

    if answer == "cross":
        print("you ran many miles ran out of water and lose the game ")
        answer=input("you cross the bridge and met some strangers do you talk to them (yes/no)? ")
        if answer == "yes":
            print("you talk to the stranger and they gave you a ticket.you won!")
        elif answer == "no":
            print("you ignore the stranger, and they are offended. you lose!")
        else:
            print("you did not enter a valid option, you lose!")

    elif answer == "back":
        print("you go back and lose")
    else:
        print("you didnot enter a valid option , you lost the game")
        print("thankyou for trying",name)
