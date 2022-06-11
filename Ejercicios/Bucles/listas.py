palabra = int(input("Numero de palabras"))

if palabra < 1 :
    print("No se puede hacer nada")
else :
    lista = []
    for i in range (palabra):
        print("La palabra es " , str(i+1) ,":" ,end="")
        palabra = input()
        lista += [palabra]
    print(lista)

