quizz={
    "question1":{
        "question":"what is the capital of France",
        "answer":"Paris"
    },
     "question2":{
        "question":"what is the capital of Germany",
        "answer":"Berlin"
    },
     "question3":{
        "question":"what is the capital of Spain",
        "answer":"Madrid"
    },
     "question4":{
        "question":"what is the capital of Italy",
        "answer":"Rome"
    },
     "question5":{
        "question":"what is the capital of Portugal",
        "answer":"Lisbon"
    },
     "question6 ":{
        "question":"what is the capital of Switzerland",
        "answer":"Bern"
    },
}
score=0
for key,value in quizz.items():
    print(value['question'])
    answer=input("answer? ")
    if answer.lower()==value['answer'].lower():
        print('correct')
        score+=1 
        print('your score is ',str(score))
        print('')
        print('')
    else:
        print('wrong!')
        print('The answer is: '+ value['answer'])
        print('your score is ',str(score))
        print('')
        print('')
print('you got',str(score),"out of 6 correctly ")
print('your percentage is ',str(int(score/6*100)),"%")