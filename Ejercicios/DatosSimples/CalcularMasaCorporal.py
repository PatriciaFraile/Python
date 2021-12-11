#Pida el peso y la estatura
#Calcular el indice de masa corporal y lo almacene en una variable
estatura = input("Tu estatura es :")
peso = input("Tu peso es:")
total = round(float(peso)/float(estatura)*2,2)
print("Tu masa corporal es :"+ str(total))
