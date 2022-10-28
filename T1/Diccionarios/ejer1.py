nombre = input("Escribe tu nombre")
apellido = input("Escribe tu apellido")
edad = input("Escribe tu edad")
genero = input("Escribe tu genero")
estado = input ("Tu estado civil")
mascota = input("Tu mascota es")
nom = input("El nombre de tu mascota es")

mivida = {
    'Nombre': nombre,
    'apellido': apellido,
    'edad': edad,
    'Genero': genero,
    'Estado civil':estado,
    'Mascota':mascota,
    'Nombre de la mascota': nom

}
#print(mivida)

print("Mi nombre es "+mivida.get('Nombre'))
print("Mi apellido es "+mivida.get('apellido'))
print("Edad "+ mivida.get('edad'))
print("Soy "+mivida.get('Genero'))
print("Mi estado civil es "+mivida.get('Estado civil'))
print("Tengo un "+mivida.get('Mascota'))
print("Y su nombre es "+mivida.get('Nombre de la mascota'))