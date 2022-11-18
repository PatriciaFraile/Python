'''Contar cuantas veces aparece la letra en el fichero texto.txt'''
with open('texto.txt','r') as f:
    linea = f.readline()
    print(linea.count("e"))
f.close()
