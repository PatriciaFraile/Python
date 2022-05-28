#Dada las siguientes notas almacenadas en un arreglo:
#[20, 15, 12, 11, 8, 4, 1]
#Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. 
#Luego programáticamente calcule el promedio de notas descontando la nota eliminada.

A = [20, 15, 12, 11, 8, 4, 1]
max = 20
min = max
for i in A :
    if i< min :
        min = i
    print("El promedio minimo es ", min)
A.remove(min)
print (A)

suma = 0
for j in A:
    suma+=j
print (suma)
print (suma/len(A))