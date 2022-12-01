'''Crea un programa que a partir del fichero de texto: "prueba1.txt", el cual contiene exactamente esto
A,1
B,2
C,3
D,4'''

texto =  ("A"+","+str(1)+"\n"+"B"+","+str(2)+"\n"+"C"+","+str(3)+"\n"+"D"+","+str(4))

nombre_fichero = 'prueba1'+'.txt'
with open (nombre_fichero,'w') as f:
    f.write(texto)
f.close()

texto.split


