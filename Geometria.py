print("Bienvenidos al calculador geometrico de figuras")
print("vamos a calcular el area y perimetro de las siguientes figuras:")



print("vamos con el cuadrado")

ing_l1c = float(input("Ingrese el Lado 1: "))
ing_l2c = float(input("Ingrese el Lado 2: "))
ing_l3c = float(input("Ingrese el Lado 3: "))
ing_l4c = float(input("Ingrese el Lado 4: "))

class area_cuadrado():

    def __init__ (self, L1, L2):
        self.L1 = L1
        self.L2 = L2
    
    def calculador_cuad_area(self):
        print("El area final de cuadrado sera", self.L1 * self.L2, "M2")

class perimetro_cuadrado():

    def __init__ (self, L1, L2, L3, L4):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.L4 = L4

    def calculador_cuad_sup(self):
        print("El perimetro final del cuadrado sera", self.L1 + self.L2 + self.L3 + self.L4, "Cm")

area_final = area_cuadrado(ing_l1c,ing_l2c)
area_final.calculador_cuad_area()

sup_final = perimetro_cuadrado(ing_l1c, ing_l2c, ing_l3c, ing_l4c)
sup_final.calculador_cuad_sup()




print("vamos con el triangulo")

ing_l1t = float(input("Ingrese el Lado 1: "))
ing_l2t = float(input("Ingrese el Lado 2: "))
ing_l3t = float(input("Ingrese el Lado 3: "))

class area_triangulo():

    def __init__ (self, L1, L2):
        self.L1 = L1
        self.L2 = L2

    def calculador_triang_area(self):
        print("El Area final del triangulo sera", ((self.L1 * self.L2) / 2 ) ,"cm")


class perimetro_triangulo():

    def __init__ (self, L1, L2, L3):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def calculador_triang_perimetro(self):
        print("El perimetro final del triangulo sera", self.L1 + self.L2 + self.L3 ,"Cm")

calculo_final_triang = area_triangulo(ing_l1t, ing_l2t)
calculo_final_triang.calculador_triang_area()

calculo_final_triang_b = perimetro_triangulo(ing_l1t, ing_l2t, ing_l3t)
calculo_final_triang_b.calculador_triang_perimetro()

mensaje = float(input("gracias por usar el programa :)"))

