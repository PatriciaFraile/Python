class Triangulo():
    def __init__(self):
        self.lado1 = int(input("Lado 1"))
        self.lado2 = int(input("Lado 2 "))
        self.lado3 = int(input("Lado 3"))

    def mostrarDatos(self):
        print("Los lados del triangulo son:")
        print("Lado 1 : ", self.lado1)
        print("Lado 2 :", self.lado2)
        print("Lado 3 : ", self.lado3)

    def mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es :", self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayr es :", self.lado2)
        else:
            print("El lado mayor es:", self.lado3)

    def tipoTiangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Triangulo equilatero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Triangulo escaleno")
        else:
            print("Triangulo isosceles")


triangulo1 = Triangulo()
triangulo1.mostrarDatos()
triangulo1.mayor()
triangulo1.tipoTiangulo()
