#Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y 
#crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado.

n = int(input("Ingrese el tamaño del arreglo"))
m = int(input("Ingrese el número de múltiplos"))
A = []
for i in range (0,n):
 A.append(i*m)

print (A)
