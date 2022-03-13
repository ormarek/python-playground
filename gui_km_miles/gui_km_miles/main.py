from tkinter import *

window = Tk()
window.title("Miles/Km Converter")
window.config(padx=20, pady=20)


def convert():
  miles = float(miles_input.get())
  km = miles * 1.609
  result_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to")
result_label = Label(text="0")
km_label = Label(text="km")
calculate = Button(text="Calculate", command=convert)

miles_input.grid(column=2, row=1)
miles_label.grid(column=3, row=1)
equal_label.grid(column=1, row=2)
result_label.grid(column=2, row=2)
km_label.grid(column=3, row=2)
calculate.grid(column=2, row=4)

window.mainloop()
