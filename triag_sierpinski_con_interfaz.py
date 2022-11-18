import random
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)



#------------------generar triangulo y su grafico-----------------------------#


def punto_medio(punto1, punto2):
    return (punto1 + punto2) / 2


def plotino():
    iterador = int(itera.get())

    semillax = random.uniform(0, 1)
    semillay = random.uniform(0, 1)
    
    pointx = [semillax]
    pointy = [semillay]

    v1x, v1y = 0, 0
    v2x, v2y = 0.5, np.sqrt(3) / 2
    v3x, v3y = 1, 0
    
    for i in range(iterador):
        vertice = random.randint(1, 3)
        if vertice == 1:
            px = punto_medio(pointx[i], v1x)
            py = punto_medio(pointy[i], v1y)
            pointx.append(px)
            pointy.append(py)
    
        elif vertice == 2:
            px = punto_medio(pointx[i], v2x)
            py = punto_medio(pointy[i], v2y)
            pointx.append(px)
            pointy.append(py)
            
        elif vertice == 3:
            px = punto_medio(pointx[i], v3x)
            py = punto_medio(pointy[i], v3y)
            pointx.append(px)
            pointy.append(py)
    
    pointx.append(v1x)
    pointy.append(v1y)
    pointx.append(v2x)
    pointy.append(v2y)
    pointx.append(v3x)
    pointy.append(v3y)


    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.scatter(pointx, pointy, color = 'm', marker = 'o', s = 1)

    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()


#-----------------------------------interfaz-----------------------------------#


window = Tk()
window.title('TRIANGULO DE SIERPINSKI')
window.geometry("600x300")
miframe = Frame(window, width = 600, height = 600)
miframe.pack()

plot_button = Button(window, height = 2, 
                    command = plotino, 
                    width = 15, 
                    text = "Generar triángulo")
plot_button.pack()

itera = Entry(miframe)
itera.grid(row = 10, column = 3, padx = 10, pady = 10)

itetiqueta = Label(miframe, 
                    text = 'Ingrese la cantidad de iteraciones: ')

itetiqueta.grid(row = 10, 
                column = 2, 
                padx = 10, 
                pady = 10)

window.mainloop()