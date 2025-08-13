valores = [1, 3, 0, -1, -3, 2+3j, True,'hola']
from math import pi
def area(r):
    areaC = pi*(r**2)
    return areaC
for v in valores:
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)