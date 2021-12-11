#Ejercicio del palindromo

cadena=input("Dame una frase :")

inversa = cadena[::-1]

if(cadena==inversa):
    print("Es palindromo")
else:
    print("No es palindromo")
    