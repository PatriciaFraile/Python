lista = ["\nEscribiendo\n","lista\n","en ficheros"]
with open ("ficheroUno.txt","a") as f:
    f.writelines(lista)
f.close()