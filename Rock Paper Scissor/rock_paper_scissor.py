from tkinter import *
import random as rd

def printer():
    comp_choice = rd.choice(['rock', 'paper', 'scissor'])

    if hum_selection.get() != 'default':
        com_selection.set(comp_choice)
        if hum_selection.get() == 'rock':
            if comp_choice == 'paper':
                score_com.set(score_com.get() + 1)
                result.set("You lost")
            elif comp_choice == 'scissor':
                score_hum.set(score_hum.get() + 1)
                result.set("You won!")
            else:
                result.set("Draw")

        elif hum_selection.get() == 'scissor':
            if comp_choice == 'paper':
                score_hum.set(score_hum.get() + 1)
                result.set("You won!")
            elif comp_choice == 'rock':
                score_com.set(score_com.get() + 1)
                result.set("You lost")
            else:
                result.set("Draw")

        elif hum_selection.get() == 'paper':
            if comp_choice == 'rock':
                score_hum.set(score_hum.get() + 1)
                result.set("You won!")
            elif comp_choice == 'scissor':
                score_com.set(score_com.get() + 1)
                result.set("You lost")
            else:
                result.set("Draw")
        else:
            result.set("Select an option")

def reset():
    score_hum.set(0)
    score_com.set(0)

root = Tk()
root.title("Rock Paper Scissor")
root.resizable(0, 0)

hum_selection = StringVar(value = "default")
com_selection = StringVar(value = "default")

score_hum = IntVar(value = 0)
score_com = IntVar(value = 0)
result = StringVar(value = " ")

hum_select_label = Label(root, textvariable = hum_selection, font = ("verdana", 15))
com_select_label = Label(root, textvariable = com_selection, font = ("verdana", 15))
res_label = Label(root, textvariable = result, font = ("verdana", 15))
hum_score_label = Label(root, textvariable = score_hum, font = ("verdana", 15))
com_score_label = Label(root, textvariable = score_com, font = ("verdana", 15))
inst_label = Label(root, text = "Make a choice:", font = ("verdana", 15))
rock_rb = Radiobutton(root, text = "Rock", variable = hum_selection, value = "rock", font = ("verdana", 12))
paper_rb = Radiobutton(root, text = "Paper", variable = hum_selection, value = "paper", font = ("verdana", 12))
scissor_rb = Radiobutton(root, text = "Scissor", variable = hum_selection, value = "scissor", font = ("verdana", 12))

submit_btn = Button(root, text = "Play", command = printer, font = ("Helvetica", 10))
reset_btn = Button(root, text = "Reset", command = reset, font = ("Helvetica", 10))

Label(root, text = "Player score =", font = ("helvetica", 10, "bold")).grid(row = 0, column = 0, padx = 10, pady = 20)
hum_score_label.grid(row = 0, column = 1)
Label(root, text = "Computer score =", font = ("helvetica", 10, "bold")).grid(row = 0, column = 2, padx = 10, pady = 20)
com_score_label.grid(row = 0, column = 3)

Label(root, text = "You chose", font = ("verdana", 15)).grid(row = 1, column = 0, padx = 0)
hum_select_label.grid(row = 2, column = 0, columnspan = 2)
Label(root, text = "Computer chose", font = ("verdana", 15)).grid(row = 1, column = 2)
com_select_label.grid(row = 2, column = 2, columnspan = 2)
res_label.grid(row = 3, column = 0, columnspan = 4)
inst_label.grid(row = 4, column = 0, columnspan = 4)
rock_rb.grid(row = 5, column = 0, columnspan = 4)
paper_rb.grid(row = 6, column = 0, columnspan = 4)
scissor_rb.grid(row = 7, column = 0,columnspan = 4)
submit_btn.grid(row = 8, column = 0, columnspan = 2, ipadx = 10)
reset_btn.grid(row = 8, column = 2, columnspan = 2, ipadx = 10)


root.mainloop()
