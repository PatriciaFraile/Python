#Excepciones

f = open ("archivotext-excepciones.txt","w")
f.write("Probando excepciones")
f.close()

nombre = "archivotext-excepciones.txt"
try:
    with open(nombre,'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero')