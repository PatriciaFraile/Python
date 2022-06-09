amount=float(input("Escribe un numero para invertir"))
porcentaje=float(input("Escribe el porcentaje"))
anios =int(input("Años"))
for i in range(anios):
    amount*= 1+ porcentaje/100
    print(" Capital tras " + str(i+1)+ " años: "+ str(round(amount,2)))