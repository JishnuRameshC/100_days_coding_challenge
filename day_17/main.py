from data import question_data
from question_model import Question
from quiz_brain import QueizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answ = question["answer"]
    new_question = Question(question_text, question_answ)
    question_bank.append(new_question)

quiz_brain = QueizBrain(question_bank)
quiz_brain.next_question()

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("your quize is completed ")
print(f" your score : {quiz_brain.score}/{quiz_brain.question_no}")