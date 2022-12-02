primitiva=[]
for i in range(7):
    primitiva.append(int(input("Escribe el numero ganador")))
primitiva.sort()
print("Los ganadores son "+str(primitiva))