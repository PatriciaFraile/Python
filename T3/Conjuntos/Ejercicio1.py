'Iterar elementos con el set'

A = set()
type(A)

A = {5,2,3}
print(A)

B = {5,2,3,5,2,3}
print(B)

if A == B : 
     print(True)
else:
    print(False)


numeros = {1,2,3,1,2,3,1,2,3}
C = set(numeros)
print(C)

for n in A :
     print(n)


# Los set no soporta el indexing



B.clear()
print(B)

B.add(8)
B.add(9)

union = A|B
print(union)

interseccion = A&B
print(interseccion)

A.add(8)
interseccion = A&B
print(interseccion) #Numero igual entre los dos variables

if A<B:
    print (True)
else:
     print(False)

if B< set([7,8,9]):
    print(True)
else:
     print(False)

diferencia = A-B
print(diferencia)

diferencia2 = B-A
print(diferencia2)

simetrica = A^B
print(simetrica)