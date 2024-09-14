def calcular_area(base, altura):
    area = base * altura / 2
    return area

def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))


area = calcular_area(base, altura)
print("El área del triángulo es: {:.2f}".format(area))

perimetro = calcular_perimetro(lado1, lado2, lado3)
print("El perímetro del triángulo es: {:.2f}".format(perimetro))