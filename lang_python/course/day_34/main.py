from source import *
from data import ques_set

question_bank = []
for question in ques_set:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizInterface(question_bank)

print(f"You have finished the quiz with a score of {quiz.score}/{quiz.tot}")