from tkinter import *
from tkinter.ttk import *

def check_pswd(pswd, digits, alphas, spec):
    import string as st
    digit_check = 0
    alphabet_check = 0
    spc_char_check = 0
    
    for char in pswd:
        if char.isdigit():
            digit_check = 1
            break
        else:
            continue
    for char in pswd:
        if char.isalpha():
            alphabet_check = 1
            break
        else:
            continue
    for char in pswd:
        if char in st.punctuation:
            spc_char_check = 1
            break
        else:
            continue

    if digits == digit_check and alphas == alphabet_check and spec == spc_char_check:
        return True
    else:
        return False


def generate_pass():
    import random as r
    import string as st

    alpha = list(st.ascii_lowercase + st.ascii_uppercase)
    digit_l = list(st.digits)
    symb = list(st.punctuation)

    available_chars = []

    
    if chars.get() == 1:
        available_chars += alpha
    else:
        pass
        
    if digits.get() == 1:
        available_chars += digit_l
    else:
        pass
    if symbols.get() == 1:
        available_chars += symb
    else:
        pass


    if int(length.get()) > 0 and int(length.get()) >= int(chars.get()) + int(digits.get()) + int(symbols.get()) and int(chars.get()) + int(digits.get()) + int(symbols.get()) > 0:
        while True:
            pswd = ''
            for i in range(int(length.get())):
                char = r.choice(available_chars)
                pswd += char
            if check_pswd(pswd, alphas = chars.get(), digits = digits.get(), spec = symbols.get()):
                break
            else:
                continue
        
        pass_entry.delete(0, len(pass_entry.get()))
        pass_entry.insert(0, pswd)
    
    else:
        pass_entry.delete(0, len(pass_entry.get()))
        pass_entry.insert(0, 'Invalid selection')

root = Tk()
root.configure()
root.title("Password Generator")
root.resizable(0, 0)

password = StringVar(value = '', master = root)
length = IntVar(value = 0, master = root)

chars = IntVar(master = root)
digits = IntVar(master = root)
symbols = IntVar(master = root)

pass_label = Label(text = "Generated password:", font = "Helvetica")
pass_entry = Entry(textvariable = password, font = ('Helvetica', 10))
pass_length_label = Label(text = "Enter length:", font = "Helvetica")
pass_length_entry = Entry(textvariable = length, font = ('Helvetica', 8))
char_checkbtn = Checkbutton(text = 'Alphabets', variable = chars, onvalue = 1, offvalue = 0)
digits_checkbtn = Checkbutton(text = 'Digits', variable = digits, onvalue = 1, offvalue = 0)
symbols_checkbtn = Checkbutton(text = 'Special characters', variable = symbols, onvalue = 1, offvalue = 0)
generate_btn = Button(text = 'Generate', command = generate_pass)

Label(text = 'Password Generator', font = ("Helvetica", 30)).grid(row = 0, column = 0, columnspan = 2, pady = 30, padx = 30)
pass_label.grid(row = 1, column = 0)
pass_entry.grid(row = 1, column = 1)
pass_length_label.grid(row = 2, column = 0)
pass_length_entry.grid(row = 2, column = 1)
char_checkbtn.grid(row = 3, column = 0, columnspan = 2)
digits_checkbtn.grid(row = 4, column = 0, columnspan = 2)
symbols_checkbtn.grid(row = 5, column = 0, columnspan = 2)
generate_btn.grid(row = 6, column = 0, columnspan = 2)

root.mainloop()
