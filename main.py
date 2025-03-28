import math
from Punto import Punto
from Rectangulo import Rectangulo
from Punto import cuadrante, vector, distancia, mas_lejos_origen




if __name__ == "__main__":
    # Crear puntos
    A = (2, 3)
    B = (5, 5)
    C = (-3, -1)
    D = (0, 0)
    print("Puntos:")
    print(f"A: {A}, B: {B}, C: {C}, D: {D}")

    # Consultar cuadrantes
    print("\nCuadrantes:")
    print(f"A pertenece al {Punto.cuadrante(A)}")
    print(f"C pertenece al {Punto.cuadrante(C)}")
    print(f"D pertenece al {Punto.cuadrante(D)}")

    # Consultar vectores
    print("\nVectores:")
    print(f"Vector AB: {Punto.vector(A, B)}")
    print(f"Vector BA: {Punto.vector(B, A)}")

    # Distancias (optativo)
    print("\nDistancias:")
    print(f"Distancia entre A y B: {Punto.distancia(A, B)}")
    print(f"Distancia entre B y A: {Punto.distancia(B, A)}")

    # Punto más lejos del origen (optativo)
    punto_mas_lejos = Punto.mas_lejos_origen(A, B, C)
    print(f"\nEl punto más lejos del origen es: {punto_mas_lejos}")

    # Crear rectángulo y consultar propiedades
    print("\nRectángulo:")
    base, altura, area = Rectangulo(A, B)
    print(f"Base: {base}, Altura: {altura}, Área: {area}")

# Ejemplo de uso corregido
rectangulo = Rectangulo([(1, 2), (4, 2), (1, 6), (4, 6)])
print("Base:", rectangulo.base())  # Salida: 3
print("Altura:", rectangulo.altura())  # Salida: 4
print("Área:", rectangulo.area())  # Salida: 12