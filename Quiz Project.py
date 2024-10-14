from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")