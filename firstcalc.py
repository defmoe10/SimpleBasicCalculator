from tkinter import *

main = Tk()

main.title("Addition Calculator")

def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def add():
    firstnum = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(firstnum)
    e.delete(0,END)
def equal():
    secondnum = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num+int(secondnum))
    elif math == 'subtraction':
        e.insert(0,f_num-int(secondnum))
    elif math == 'multiplication':
        e.insert(0,f_num*int(secondnum))
    elif math == 'divison':
        e.insert(0,f_num/int(secondnum))
    else:
        e.insert(0,"ERROR")


def multiply():
    firstnum = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(firstnum)
    e.delete(0, END)
def divide():
    firstnum = e.get()
    global f_num
    global math
    math = 'divison'
    f_num = int(firstnum)
    e.delete(0, END)
def subtract():
    firstnum = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(firstnum)
    e.delete(0, END)
e = Entry(main, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

one = Button(main,text='1',padx=40,pady=20,command=lambda: click(1))
two = Button(main,text='2',padx=40,pady=20,command=lambda: click(2))
three = Button(main,text='3',padx=40,pady=20,command=lambda: click(3))
four = Button(main,text='4',padx=40,pady=20,command=lambda: click(4))
five = Button(main,text='5',padx=40,pady=20,command=lambda: click(5))
six = Button(main,text='6',padx=40,pady=20,command=lambda: click(6))
seven = Button(main,text='7',padx=40,pady=20,command=lambda: click(7))
eight = Button(main,text='8',padx=40,pady=20,command=lambda: click(8))
nine = Button(main,text='9',padx=40,pady=20,command=lambda: click(9))
zero = Button(main,text='0',padx=40,pady=20,command=lambda: click(0))

add = Button(main,text='+',padx=39,pady=20,command = add)
multiply = Button(main,text='*',padx=40,pady=20,command=multiply)
subtract = Button(main,text='-',padx=41,pady=20,command=subtract)
divide = Button(main,text='/',padx=42,pady=20,command=divide)

equal = Button(main,text='=',padx=91,pady=20,command=equal)
clear = Button(main,text="clear",padx=79,pady=20,command=clear)


one.grid(row=3,column=0)
two.grid(row=3,column=1)
three.grid(row=3,column=2)

four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)

seven.grid(row=1,column=0)
eight.grid(row=1,column=1)
nine.grid(row=1,column=2)

zero.grid(row=4,column=0)

add.grid(row=5,column=0)
multiply.grid(row=6,column=0)
subtract.grid(row=6,column=1)
divide.grid(row=6,column=2)
equal.grid(row=5,column=1,columnspan=2)
clear.grid(row=4,column=1,columnspan=2)


main.mainloop()