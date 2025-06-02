from email import message
import json
import re

score = 0
with open("questions.json", "r") as x:
    # data = x.read()
    data = json.load(x)
    print(data)
    print(type(data))

for question in data:
    print(question["question"])
    for index, option in enumerate(question["options"]):
        print(f"{index+1}. {option}")
    user_choice = int(input("Enter your answer: "))
    question["user_answer"] = user_choice
    

for index, question in enumerate(data):
    if question["correct_answer"] == question["user_answer"]:
        score = score + 1
        result = "Correct"
    else:
        result = "Wrong"
    question_number = index + 1
    message = f"Your answer: {question['user_answer']} | Correct answer: {question['correct_answer']} | {result}"
    print(f"\nQuestion No.{question_number}")
    print(message + "\n")

print(f"Your score: {score}/{len(data)}" + "\n")
