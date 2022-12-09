from tkinter import*
raiz = Tk()
raiz.title("Primera ventana")
raiz.config(cursor="pirate")
miFrame = Frame(raiz)
miFrame.config(width=480,height=320)
label = Label(raiz, text="Nombre")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
#Cajas de texto
entrada = Entry(raiz)
#Donde se situan
entrada.grid(row=0, column=1, padx=5, pady=5)
entrada.config(justify="right", state="normal")
raiz.mainloop()