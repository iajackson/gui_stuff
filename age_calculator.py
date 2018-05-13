from tkinter import *
from tkinter import ttk

#enter age in years
#age_in_years = input("What is your age in years? ")
#age_in_years = int(age_in_years)

#calculate age in days
def calculate_age():
    try:
        age_in_days.set(int(age.get()) * 365)
    except ValueError:
        pass
    

#output age in days
#print("You are " + str(age_in_days) + " days old!")

root = Tk()
root.title("Age calculator")

frame = ttk.Frame(root, width = 640, height = 480, relief='raised', padding = "20")
frame.grid(column=0, row=0, sticky=(N, S, E, W))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

label = ttk.Label(frame, text = "What is your age in years?")
label.grid(column=0, row=0)

age = StringVar()
text_entry = ttk.Entry(frame, width=10, textvariable=age)
text_entry.grid(column=1, row=0)

go_button = ttk.Button(frame, text = 'Calculate!', command = calculate_age)
go_button.grid(column=0, row=2)

age_in_days = StringVar()
label2 = ttk.Label(frame, text = "Your are this many days old:")
label2.grid(column=0, row=3)

label3 = ttk.Label(frame, textvariable = age_in_days)
label3.grid(column=1, row=3)

root.mainloop()
