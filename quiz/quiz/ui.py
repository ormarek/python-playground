from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:
  def __init__(self, quiz_brain: QuizBrain):
    self.is_locked = False
    self.quiz = quiz_brain 
    self.window = Tk()
    self.window.title("Quiz")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    self.score_label = Label(text=f"Score: 0", fg="white")
    self.score_label.grid(row=0, column=1)

    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2)

    true_image = PhotoImage(file="./quiz/images/true.png")
    false_image = PhotoImage(file="./quiz/images/false.png")
    self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
    self.true_button.grid(row=2, column=0, pady=20)

    self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
    self.false_button.grid(row=2, column=1, pady=20)

    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")

    if self.quiz.still_has_questions():
      self.is_locked = False
      self.score_label.config(text=f"Score: {self.quiz.score}")
      question = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text=question)
    else:
      self.canvas.itemconfig(self.question_text, text="You've reqched the end of the quiz")

  def true_pressed(self):
    if not self.is_locked:
      self.give_feedback(self.quiz.check_answer("True"))

  def false_pressed(self):
    if not self.is_locked:
      self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right):
    self.is_locked = True
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
