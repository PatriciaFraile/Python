'''texto = "Es un hecho establecido hace demasiado tiempo que un lector se distraerá con el contenido del texto de un sitio \n mientras que mira su diseño. El punto de usar Lorem Ipsum es que tiene una distribución más o menos normal \n de las letras, al contrario de usar textos como por ejemplo "
with open ("texto.txt","w") as buscar:
    buscar.write(texto)'''

n = int (input('Escribe un numero'))
with open('texto.txt','r') as buscar:
    for i in range (n):
        print(buscar.readline())