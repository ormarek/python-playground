
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer_running = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global timer_running
  global reps

  reps = 0
  timer_running = False
  title_label.config(text="Pomodoro", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  check_marks.config(text="")
  window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  global timer_running

  if timer_running is False:
    timer_running = True
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
      title_label.config(text="20min break", fg=RED)
      count_down(long_break_sec)
    elif reps % 2 == 0:
      title_label.config(text="5min break", fg=PINK)
      count_down(short_break_sec)
    else:
      title_label.config(text="25min work", fg=GREEN)
      count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  global timer_running
  global timer

  count_minutes = math.floor(count / 60)
  if count_minutes < 10:
    count_minutes = f"0{count_minutes}"

  count_seconds = math.floor(count % 60)
  if count_seconds < 10:
    count_seconds = f"0{count_seconds}"

  canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
  if count:
    timer = window.after(1000, count_down, count - 1)
  else:
    timer_running = False
    start_timer()
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += CHECK_MARK

    check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# Wasn't able to remove hightlight with 'highlightthickness' so just changed it's color
# to match backgroung
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
