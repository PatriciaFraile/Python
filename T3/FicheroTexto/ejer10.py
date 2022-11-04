'''Escribe un programa que pida por teclado un numero del 1 al 10
y guarde en un fichero. Que muetre todas las tablas de multiplicar hasta el numero introducido'''

n = int(input('Introduce un numero'))
with open ('tablas.txt','w') as escribir:
    for i in range (1,n+1):
        for j in range (1,11):
            escribir.write(str(i)+"x"+str(i)+"="+str(i*j)+'\n')
    escribir.close()