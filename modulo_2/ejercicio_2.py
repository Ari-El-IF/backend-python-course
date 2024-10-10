print("Ingrese 2 puntos para calcular su distancia euclidiana")
x_1 = float(input("Ingrese x1 : "))
y_1 = float(input("Ingrese y1 : "))

x_2 = float(input("Ingrese x2 : "))
y_2 = float(input("Ingrese y2 : "))

distancia = (((x_2 - x_1)**2) + ((y_2 - y_1)**2))**(1/2)

print("La distancia entre los 2 puntos es: ", distancia)
