'Tabla de multiplicar'

n = int (input("Escribe un numero"))
nombre_fichero = 'tabla del '+str(n)+'.txt'
with open (nombre_fichero , 'w') as f:
    for i in range (1,11):
        f.write(str(i) + 'x'+str(n)+'='+str(i*n)+'\n')
f.close()