#Crea un array o arreglo unidimensional donde le indiques el tamaño por teclado y 
#crear una función que rellene el array o arreglo con los múltiplos de un número pedido por teclado.

tamanio = int(input("Ingrese el tamaño del arreglo"))
numero = int(input("Ingrese el número de múltiplos"))
A = []
for i in range (0,tamanio):
 A.append(i*numero)

print (A)
