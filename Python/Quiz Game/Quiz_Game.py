quizes = {
    "questions":[
        {"question":"what is the capital of Ethiopia?",
         "options":["A, Addis Ababa", "B, Nairobi", "C, Cairo", "D, Khartoum"],
         "answer":"A, Addis Ababa"},            
        {"question":"what is 2+2?",
         "options":["A, 3", "B, 4", "C, 5", "D, 6"],
         "answer":"B, 4"},
        {"question":"what is the antonym for the word 'thin'",
         "options":["A, slim", "B, skinny", "C, fat", "D, lean"],
            "answer":"C, fat"}                
    ]
}

score = 0

def add(quizes):
    question = input("Enter a new question: ")
    option = [opt.strip() for opt in input("Enter the options (comma-separated): ").split(",")]
    answer = input("Enter the right answer: ")
    
    new = {
        "question": question,
        "options": option,
        "answer": answer
    }
    
    quizes["questions"].append(new)
    print("question added successfully")
    return quizes

def play(quizes):
    count = 0
    for q in quizes["question"]:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans = input("Enter your answer: ")
        if user_ans.lower() == q["answer"].strip().lower():
            print("correct answer")
            score += 1
        elif user_ans.lower() != q["answer"].strip().lower():
            print("incorrect answer the answer was", q["answer"])
        else:
            print("you entered an invalid value")
        count += 1
    
    print("your score is", score, "//", count) 
         
    ave = (score/count)*100
    if ave >= 70:
        print("excellent")
    elif ave >= 50:
        print("good")
    else:
        print("poor")
    return quizes
    

while True:   
    print("what do you want to do")
    print("1. add question to the quiz")
    print("2. play")
    choice = int(input("enter your choice"))

    match choice:
        case 1:
            new_quizes = add(quizes)
        case 2:
            new_quizes = play(new_quizes)
        case _:
            print("invalid input")
    do = input("do you want to do again? y/n ").lower()
    if do != 'y':
        break