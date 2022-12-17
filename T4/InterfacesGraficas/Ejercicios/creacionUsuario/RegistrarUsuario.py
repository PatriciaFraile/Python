from tkinter import*
from turtle import width

def send_data():
    username_data = username.get()
    password_data = password.get()
    name_data= name.get()
    age_data = age.get()

    print(username_data,"\t",password_data, "\t", name_data,"\t",age_data)

    newfile= open("registration.txt","a")
    newfile.write(username_data)
    newfile.write("\t")
    newfile.write(password_data)
    newfile.write("\t")
    newfile.write(name_data)
    newfile.write("\t")
    newfile.write(age_data)
    newfile.write("\n")
    newfile.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    name_entry.delete(0,END)
    age_entry.delete(0,END)

mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registro")
mywindow.resizable(False,False)
mywindow.config(background="#148F77")
main_title=Label(text="Creación de cuenta", font=("Cambria",13), bg="#56CD63",fg="white", width="550", height="2")
main_title.pack()

username_label = Label(text="Usuario", bg = "#FFEEDD")
username_label.place(x=22, y=70)
password_label = Label(text="Contraseña",bg="#FFEEDD")
password_label.place(x=22, y=130)
name_label = Label(text="Nombre", bg="#FFEEDD")
name_label.place(x=22,y=190)
age_label = Label(text="Edad", bg="#FFEEDD")
age_label.place(x=22, y=250)

username = StringVar()
password = StringVar()
name = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username , width="40")
password_entry = Entry(textvariable=password , width="40", show="*")
name_entry = Entry(textvariable=name , width ="40")
age_entry = Entry(textvariable=age, width="40")

username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
name_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

submit_btn= Button(mywindow, text ="Enviar" , command=send_data, width="30", height="2",bg="#0E6251")
submit_btn.place(x=22,y=320)

mywindow.mainloop()