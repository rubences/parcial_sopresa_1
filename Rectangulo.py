from Punto import Punto

class Rectangulo:
    def __init__(self, puntos):
        if len(puntos) != 4:
            raise ValueError("Se necesitan exactamente 4 puntos para definir un rectángulo.")
        self.puntos = [Punto(x, y) for x, y in puntos]

    def base(self):
        # La base es la distancia entre dos puntos horizontales
        return abs(self.puntos[1].x - self.puntos[0].x)

    def altura(self):
        # La altura es la distancia entre dos puntos verticales
        return abs(self.puntos[2].y - self.puntos[0].y)

    def area(self):
        # El área es base * altura
        return self.base() * self.altura()

