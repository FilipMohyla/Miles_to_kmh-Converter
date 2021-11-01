from tkinter import *

window = Tk()
window.title("Mile to KmH Converter")
window.minsize(150, 170)
window.config(padx=50, pady=50)
user_input = Entry(width=8)
user_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=2)

result_label = Label(text="0")
result_label.grid(column=1, row=2)

kmh_label = Label(text="Km/h")
kmh_label.grid(column=2, row=2)

def hit_calculate():
    
    result_label.config(text=round(int(user_input.get()) * 1.6, 2))


calculate_button = Button(text="Calculate", command=hit_calculate)
calculate_button.grid(column=1, row=3)


window.mainloop()