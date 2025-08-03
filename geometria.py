import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: Área = pi * r^2
    """
    if radio < 0:
        return "Error: El radio no puede ser negativo."
    
    area = math.pi * radio**2
    return area

if __name__ == "__main__":
    radio_ejemplo = 10
    area = calcular_area_circulo(radio_ejemplo)
    print(f"El área de un círculo con radio {radio_ejemplo} es: {area}")