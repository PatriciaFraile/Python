from tkinter import*
raiz = Tk()
raiz.title("Primera ventana")

miFrame = Frame(raiz)#Es el marco de la ventana 
miFrame.pack()
miFrame.config(bg="green")#color de fondo
miFrame.config(cursor="pirate")#cursor del ratón
miFrame.config(width=480,height=320)

label = Label(raiz,text='Hola')#Creacion de un label en la raiz
label.pack()
#Siempre el mainloop() es lo ultimo
raiz.mainloop()