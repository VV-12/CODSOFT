import tkinter as tk

root = tk.Tk()
root.title('Simple Calculator')
root.configure(bg = '#576EE4')
root.resizable(0,0)

def enter1():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '1')
    else:
        input_var.set(input_var.get() + '1')
        
def enter2():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '2')
    else:
        input_var.set(input_var.get() + '2')    
def enter3():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '3')
    else:
        input_var.set(input_var.get() + '3')
def enter4():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '4')
    else:
        input_var.set(input_var.get() + '4')
def enter5():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '5')
    else:
        input_var.set(input_var.get() + '5')
def enter6():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '6')
    else:
        input_var.set(input_var.get() + '6')
def enter7():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '7')
    else:
        input_var.set(input_var.get() + '7')
def enter8():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '8')
    else:
        input_var.set(input_var.get() + '8')
def enter9():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '9')
    else:
        input_var.set(input_var.get() + '9')
def enter0():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '0')
    else:
        input_var.set(input_var.get() + '0')

def delete():
    if input_var.get().isalpha():
        input_var.set('')
    else:
        input_var.set(input_var.get()[0:-1])

def plus():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '+')
    else:
        input_var.set(input_var.get() + '+')
def minus():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '-')
    else:
        input_var.set(input_var.get() + '-')
def multiply():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '*')
    else:
        input_var.set(input_var.get() + '*')
def divide():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '/')
    else:
        input_var.set(input_var.get() + '/')
def decimal():
    if input_var.get() == 'Invalid':
        input_var.set('')
        input_var.set(input_var.get() + '.')
    else:
        input_var.set(input_var.get() + '.')
def all_clear():
    input_var.set('')

def calc():
    if input_var.get() == '':
        pass
    else:
        try:
            input_var.set(round(eval(input_var.get()), 12))
        except:
            input_var.set('Invalid')



input_var = tk.StringVar(value = '', master = root)

tk.Label(textvariable = input_var,
         font = ('verdana', 30),
         fg = '#6FE3E1',
         background = '#576EE4').grid(row = 0, column = 0, columnspan = 4)

button1 = tk.Button(text = '1',
                    activebackground= 'black',
                      activeforeground='white',
                      relief = tk.FLAT, bd = 3,
                      background = '#65B4E2',
                      font = ('gothic', 15),
                      command = enter1,
                      padx = 0,
                      pady = 0,
                      height = 2,
                      width = 10).grid(row = 4, column = 0)

button2 = tk.Button(text = '2',
                    activebackground= 'black',
                    activeforeground='white',
                    relief = tk.FLAT,
                    bd = 3,
                    background = '#65B4E2',
                    font = ('gothic', 15),
                    command = enter2,
                    padx = 0,
                    pady = 0,
                    height = 2,
                    width = 10).grid(row = 4, column = 1)

button3 = tk.Button(text = '3',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter3,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 4, column = 2)
button4 = tk.Button(text = '4',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter4,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 3, column = 0)
button5 = tk.Button(text = '5',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter5,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 3, column = 1)
button6 = tk.Button(text = '6',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter6,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 3, column = 2)
button7 = tk.Button(text = '7',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter7,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 2, column = 0)
button8 = tk.Button(text = '8',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter8,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 2, column = 1)
button9 = tk.Button(text = '9',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter9,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 2, column = 2)
button0 = tk.Button(text = '0',
                     activebackground= 'black',
                     activeforeground='white',
                    relief = tk.FLAT,
                     bd = 3,
                    background = '#65B4E2',
                     font = ('gothic', 15),
                     command = enter0,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 5, column = 1)

del_button = tk.Button(text = 'C',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#5C86E4',
                     font = ('gothic', 15),
                     command = delete,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 21).grid(row = 1, column = 2, columnspan = 2)

all_clear_button = tk.Button(text = 'AC',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#5C86E4',
                     font = ('gothic', 15),
                     command = all_clear,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 21).grid(row = 1, column = 0, columnspan = 2)

plus_button = tk.Button(text = '+',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = plus,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 2, column = 3)

minus_button = tk.Button(text = '-', activebackground= 'black', bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = minus,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 3, column = 3)

multiply_button = tk.Button(text = 'x',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = multiply,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 4, column = 3)

divide_button = tk.Button(text = '/',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = divide,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 5, column = 3)

calc_button = tk.Button(text = '=',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = calc,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 5, column = 2)

decimal_button = tk.Button(text = '.',
                     activebackground= 'black',
                     bd = 3,
                     activeforeground='white',
                    relief = tk.FLAT,
                     background='#6ACCE2',
                     font = ('gothic', 15),
                     command = decimal,
                     padx = 0,
                     pady = 0,
                     height = 2,
                     width = 10).grid(row = 5, column = 0)

root.mainloop()
