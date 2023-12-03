import hashlib
from tkinter import *

def send_contra():

    cadena = password.get()
    palabra_cifrada = cadena.encode('utf-8')
    hash_obj = hashlib.md5(palabra_cifrada.strip())
    digest = hash_obj.hexdigest()
    trad2 = Label(raiz,text=digest)
    trad2.place(x=140, y=100)

    
raiz = Tk()
raiz.title("Traducir contraseña")
miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(width=480,height=320)
label = Label(raiz, text="Ingrese la contraseña")
label.place(x=22, y=70)
trad = Label(raiz, text = "La contraseña hash : ")
trad.place(x=22 , y = 100)

password = StringVar()
password_entry = Entry(textvariable=password , width="40")
password_entry.place(x=140, y=70)

submit_btn= Button(raiz, text ="Enviar" , command=send_contra, width="20", height="2")
submit_btn.place(x=22,y=150)

raiz.mainloop()