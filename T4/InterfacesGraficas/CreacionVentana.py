from tkinter import*
raiz = Tk()
raiz.title("Primera ventana")
raiz.config(bg="green")
raiz.config(cursor="pirate")#Poner el cursor en toda la ventana 
miFrame = Frame(raiz)#Es el marco de la ventana 
miFrame.pack()
miFrame.config(bg="green")#color de fondo del frame
'''miFrame.config(cursor="pirate")#cursor del ratón en el frame'''
miFrame.config(width=480,height=320)
label = Label(raiz,text="Frame")#Creacion de un label en la raiz
label.pack(anchor=CENTER)
label.config(bg="green",fg="white")
#Siempre el mainloop() es lo ultimo
raiz.mainloop()