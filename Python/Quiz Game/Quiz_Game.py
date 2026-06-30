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