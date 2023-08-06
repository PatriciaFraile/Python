from tkinter import *
from math import *
root = Tk()
root.title("Calculator")
root.geometry("392x555")
width_button = 11
height_button = 3
input = StringVar()
operador = ""


def btnclick(num):
    global operador
    operador = operador+str(num)
    input.set(operador)


def operation():
    global operador
    try:
        result = eval(operador)
    except:
        remove()
        result = ("ERROR")
    input.set(result)


def remove():
    global operador
    operador = ("")
    input.set(operador)


def remove_num():  # error
    global operador
    result = -len[operador]
    input.set(result)


button_one = Button(root, text="%", width=width_button,
                    height=height_button, command=lambda: btnclick("%")).place(x=17, y=180)
button_two = Button(root, text="/", width=width_button,
                    height=height_button, command=lambda: btnclick("/")).place(x=107, y=180)
button_three = Button(root, text="C", width=width_button,
                      height=height_button, command=remove_num).place(x=197, y=180)
button_four = Button(root, text="R", width=width_button,
                     height=height_button, command=remove).place(x=287, y=180)
seven = Button(root, text="7", width=width_button,
               height=height_button, command=lambda: btnclick(7)).place(x=17, y=240)
eight = Button(root, text="8", width=width_button,
               height=height_button, command=lambda: btnclick(8)).place(x=107, y=240)
nine = Button(root, text="9", width=width_button,
              height=height_button, command=lambda: btnclick(9)).place(x=197, y=240)
button_five = Button(root, text="x", width=width_button,
                     height=height_button, command=lambda: btnclick("x")).place(x=287, y=240)
four = Button(root, text="4", width=width_button,
              height=height_button, command=lambda: btnclick(4)).place(x=17, y=300)
five = Button(root, text="5", width=width_button,
              height=height_button, command=lambda: btnclick(5)).place(x=107, y=300)
six = Button(root, text="7", width=width_button,
             height=height_button, command=lambda: btnclick(6)).place(x=197, y=300)
button_six = Button(root, text="-", width=width_button,
                    height=height_button, command=lambda: btnclick("-")).place(x=287, y=300)
one = Button(root, text="1", width=width_button,
             height=height_button, command=lambda: btnclick(1)).place(x=17, y=360)
two = Button(root, text="2", width=width_button,
             height=height_button, command=lambda: btnclick(2)).place(x=107, y=360)
three = Button(root, text="3", width=width_button,
               height=height_button, command=lambda: btnclick(3)).place(x=197, y=360)
button_six = Button(root, text="+", width=width_button,
                    height=height_button, command=lambda: btnclick("+")).place(x=287, y=360)
button_seven = Button(root, text=",", width=width_button,
                      height=height_button).place(x=17, y=420)
zero = Button(root, text="0", width=width_button,
              height=height_button, command=lambda: btnclick(0)).place(x=107, y=420)
spot = Button(root, text=".", width=width_button,
              height=height_button, command=lambda: btnclick(".")).place(x=197, y=420)
equal = Button(root, text="=", width=width_button,
               height=height_button, command=operation).place(x=287, y=420)

text = Entry(root, font=('arial', 20, 'bold'), width=22, textvariable=input, bd=20,
             insertwidth=4, justify="right").place(x=10, y=60)
root.mainloop()
