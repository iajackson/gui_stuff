from tkinter import *
from tkinter import ttk
import random

def check_guess(guess_var, number, answer):
    try:
        if int(guess_var.get()) < number:
            answer.set("Too low!")
        elif int(guess_var.get()) > number:
            answer.set("Too high!")
        else:
            answer.set("You got it!")
    except ValueError:
        pass

def main():
    number = random.randint(1,20)

    window = Tk()
    window.title('Random number guesser!')
    # Sets resizing of frame within window
    window.rowconfigure(0, weight = 1)
    window.columnconfigure(0, weight = 1)
    main_frame = ttk.Frame(window, relief = 'raised', padding = 20)
    # Sets resizing of items within frame
    main_frame.rowconfigure(0, weight = 1)
    main_frame.columnconfigure(0, weight = 1)
    main_frame.rowconfigure(1, weight = 1)
    main_frame.columnconfigure(1, weight = 1)
    # Sticky tells frame to fill entire window
    main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
    guess_lbl = ttk.Label(main_frame, text = 'Guess a number!')
    guess_lbl.grid(column=0, row=0, sticky=(N, W))

    guess_var = StringVar()
    guess_entry = ttk.Entry(main_frame, textvariable = guess_var)
    guess_entry.grid(column=0, row=1, sticky=(S, W))

    answer = StringVar()
    result_lbl = ttk.Label(main_frame, textvariable = answer)
    result_lbl.grid(column=1, row=0, sticky=(N, E))

    # Need lambda to pass arguments to function or it doesn't work
    go_btn = ttk.Button(main_frame, text = 'GO', command = lambda: check_guess(guess_var, number, answer))
    go_btn.grid(column=1, row=1, sticky=(S, E))
    
    window.mainloop()

if __name__ == "__main__":
    main()
