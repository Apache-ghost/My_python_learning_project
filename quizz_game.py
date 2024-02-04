print("Welcome to the game")
playing=input("Do you want to play? ")
if playing.lower() != "Yes":
    quit()
print("okay Let's begin : ")
score=0
answer=input("what does cpu stand for?  ")
if answer.lower() == "central processing unit ":
    print("correct")
    score +=1
else:
    print("incorrect")

answer=input(" what does Gpu stand for? ")
if answer.lower() == "graphical processing unit ":
    print("correct")
    score +=1
else:
    print("incorrect")

answer=input("what is the full meaning of RAM? ")
if answer.lower() == "random access memory":
    print("correct")
    score +=1
else:
    print("incorrect")

    print("you got"  + str(score) +  "question correct!")
    print("you got" + str((score /4) *100) + "%")