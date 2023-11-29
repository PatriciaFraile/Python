'Buscar en el diccionario palabras'

matricula = {
    "alumno1":54654,
    "alumno2" : 789965,
    "alumno3" : 546788
}

buscar = input("Que alumno quieres buscar: ")

if buscar in matricula.keys() :
    print ("La matricula es : ",matricula[buscar])
