import random
def adivina_numero(x):
    print("Bienvenido al juego")
    print(f"Selecciona un numero entre 1 y {x} para que el ordenador lo averigue")

    numero_superior= x
    numero_inferior = 1
    respuesta = " "
    while respuesta!="c":
        if numero_inferior!=numero_superior:
            prediccion = random.randint(numero_superior,numero_inferior)
        else:
            prediccion = numero_inferior
        respuesta= input(f"Mi predicción es {prediccion} , si es bajo escribe (A) , si es mas alto escribe (B) y si es correcto escribe (C)".lower)
        
        if respuesta=="a":
            numero_inferior= prediccion+1
        elif respuesta=="b":
            numero_superior= prediccion-1
    print(f"Sii he acertado , con tu prediccion{prediccion}")
