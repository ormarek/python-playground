from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
  question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

while quiz.has_questions():
  quiz.ask()

print(f"""
Congratulations! You've completed quiz!
Your final score was: {quiz.score}/{len(quiz.question_list)}
""")
