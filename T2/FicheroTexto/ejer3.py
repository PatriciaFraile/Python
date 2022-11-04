#Creación de un nuevo fichero

#texto = "Este es mi primer programa de python"
fichero = 'fichero'+'.txt'
with open (fichero,'w') as f:
    f.write("escribe esto")
    f.close()
