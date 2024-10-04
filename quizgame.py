import time
questions = ("What is 1+1"
           , "What is 2+2"
           , "What is 3+3",
             "What is 4+4")

options = (("A. 1",
            "B. 2",
            "C. 3",
            "D. 4"),
           ("A. 2",
            "B. 3",
            "C. 4",
            "D. 5"),
           ('A. 5',
            'B. 6',
            'C. 7',
            'D. 8'),
           ("A. 6",
            "B. 7",
            "C. 8",
            "D. 9"))

guesses = []
answers = ("B", "C", "B", "C")
score = 0
question_num = 0
for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter a guess: ").upper()  # Ensures case consistency
    guesses.append(guess)


    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question_num +=1

print(f'Your score is {score * 25}%')
time.sleep(3)


