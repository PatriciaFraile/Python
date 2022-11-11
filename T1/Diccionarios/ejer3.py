'Añadir cosas en el diccionario de Harry Potter : apellido, edad , genero y padres'

Diccionario = {
    'nombre' :'Harry',
    'apellido': 'Potter',
    'edad': 18,
    'genero':'Masculino',
    'madre':'Lili',
    'padre':'James',
    'padres':['james','lili']
}
print(Diccionario)
print(Diccionario['apellido'])
print(Diccionario['padres'][0:1])#Sacar solamente un padre
Diccionario['edad']=20 #cambiar el valor de una variable
print(Diccionario['edad'])
Diccionario['Grupo']=""#Añadir un nuevo elemento
print(Diccionario)
Diccionario["Casa"]= Diccionario.pop("Grupo") #Cambiar el nombre del elemento
print(Diccionario)
del Diccionario['apellido'] #Borra el elemento y su valor
print(Diccionario)
print('Longitud')
lon = Diccionario('apellido')
print(len(lon))