import numpy as np
import random
import matplotlib.pyplot as plt

iteraciones = int(input('ingrese el número de iteraciones a generar: '))

def punto_medio(punto1, punto2):
    return (punto1 + punto2) / 2

def triangulo_sierpinski(iteraciones):
    semillax = random.uniform(0, 1)
    semillay = random.uniform(0, 1)
    
    pointx = [semillax]
    pointy = [semillay]
    
    v1x, v1y = 0, 0
    v2x, v2y = 0.5, np.sqrt(3) / 2
    v3x, v3y = 1, 0
    
    for i in range(iteraciones):
        vertice = random.randint(1, 3)
        if vertice == 1:
            puntox = punto_medio(pointx[i], v1x)
            puntoy = punto_medio(pointy[i], v1y)
            pointx.append(puntox)
            pointy.append(puntoy)
    
        elif vertice == 2:
            puntox = punto_medio(pointx[i], v2x)
            puntoy = punto_medio(pointy[i], v2y)
            pointx.append(puntox)
            pointy.append(puntoy)
            
        elif vertice == 3:
            puntox = punto_medio(pointx[i], v3x)
            puntoy = punto_medio(pointy[i], v3y)
            pointx.append(puntox)
            pointy.append(puntoy)
    
    pointx.append(v1x)
    pointy.append(v1y)
    pointx.append(v2x)
    pointy.append(v2y)
    pointx.append(v3x)
    pointy.append(v3y)
    
    plt.figure(dpi=100)
            
    plt.scatter(pointx, pointy, 0.5, color = 'm')
    plt.show()


triangulo_sierpinski(iteraciones)