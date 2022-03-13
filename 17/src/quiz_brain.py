class QuizBrain():
  def __init__(self, question_list) -> None:
      self.question_number = 0
      self.score = 0
      self.question_list = question_list

  def has_questions(self):
    return self.question_number < len(self.question_list)

  def check_answer(self, correct_answer, user_answer):
    if correct_answer.lower() == user_answer.lower():
      self.score += 1
      print("Correct!")
    else:
      print(f"Wrong! The correct answer is: \"{correct_answer}\"")
    print(f"Your current score is: {self.score}/{self.question_number} \n")

  def ask(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    answer = input(f"Q.{self.question_number} {current_question.text} (true/false): ")
    self.check_answer(current_question.answer, answer)
