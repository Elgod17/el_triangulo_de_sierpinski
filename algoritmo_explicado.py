import random
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)



#------------------generar triangulo y su grafico-----------------------------#


def punto_medio(punto1, punto2):
    # esta funcion calcula UNA coordenada de un punto medio
    return (punto1 + punto2) / 2


def plotino():
    # convierte el input de la caja de entrada 'itera' en un entero
    iterador = int(itera.get())

    #se eleccionan al azar las coordenas de un punto tal que sus coordenadas x y y están en el rango [0,1], pero realmente se puede elegir cualquier punto del plano y no impota cuan alejado esté, el algoritmo seguira funcionando
    semillax = random.uniform(0, 1)
    semillay = random.uniform(0, 1)
    
    #por nomenclatura, las variables que lleven una 'x' son las coordenadas en el eje de las abcizas y las coordenas con una x son las coordenadas en el eje de las ordenadas. A cada punto del plano le corresponde una coordenada x en pointx y una coordenada y en pointy tales que estas dos tengan el mismo índice en sus respectivos arrays
    pointx = [semillax]
    pointy = [semillay]

    #se definen los tres vértices del triangulo 
    v1x, v1y = 0, 0
    v2x, v2y = 0.5, np.sqrt(3) / 2
    v3x, v3y = 1, 0
    
    #se empiezan a generar los puntos
    for i in range(iterador):
        #se elige entre el uno, el dos y el tres al azar. Si se elige uno, se calcula el punto medio entre el punto cuyas coordenadas tienen posición 'i' en sus respectivas listas y el vertice con coordenadas (v1x, v1y). Si se elige dos, se calcula el punto medio entre el punto cuyas coordenadas tienen posición 'i' en sus respectivas listas y el certice con coordenadas (v2x, v2y). Para el tres, se sobreentiende. Generadas las coordenadas del punto medio resultante, estas se guardan en las listas de acuerdo al eje al que pertenecen y se repite el ciclo para el punto 'i + 1', o sea, el punto que se generó recientemente
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
    

    #las coordenadas de los vertices se añaden a las listas
    pointx.append(v1x)
    pointy.append(v1y)
    pointx.append(v2x)
    pointy.append(v2y)
    pointx.append(v3x)
    pointy.append(v3y)

    #se crea un objeto que contendrá el gráfico del triangulo
    fig = Figure(figsize = (5, 5), dpi = 100)
    plot1 = fig.add_subplot(111)
    #se genera el grafico
    plot1.scatter(pointx, pointy, color = 'm', marker = 'o', s = 1)
    #se crea el canvas de tkinter que contendrá la figura que contiene el grafico de matplotlib
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()
    #se pone el canvas dentro de la ventana
    canvas.get_tk_widget().pack()
    #se crea un toolbar, que es una barra que tendrá botones que ofrecen opciones tales como descargar la imagen de la grafica que aparece en la interfaz
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    #se ubica el toolbar dentro de la ventana de la intrfaz
    canvas.get_tk_widget().pack()


#-----------------------------------interfaz-----------------------------------#

#se crea la ventana de la interfaz y se define su título y tamaño
window = Tk()
window.title('TRIANGULO DE SIERPINSKI')
window.geometry("600x300")
#se crea el frame que va a contener los widgets(los widgets son los botones, cajas a las que se les ingresan inputs, lineas de texto, imágenes, menús, etc), se define el tamaño del frame y se guarda dentro de la ventan. La ventana contiene al frame y el frame contiene los widgets
miframe = Frame(window, width = 600, height = 600)
miframe.pack()

#genera un botón que al darle click va a activar la función 'plotino'
plot_button = Button(window, height = 2, 
                    command = plotino, 
                    width = 15, 
                    text = "Generar triángulo")
#se guarda la caja del botón en el frame 'miframe'
plot_button.pack()

#esta es la caja de entrada en la que se ingresa el número de puntos que se van a hacer, o que es lo mismo, el número que se va a guardar en la variable 'iterador' de la linea 21
itera = Entry(miframe)
itera.grid(row = 10, column = 3, padx = 10, pady = 10)

#este es un texto que va al lado de la caja de entrada para indicar el dato que se va a recibir, en este caso el numero de puntos a generar para hacer el triangulo
itetiqueta = Label(miframe, 
                    text = 'Ingrese la cantidad de iteraciones: ')
#esto define la ubicación y el tamaño del texto de la variable 'itetiqueta' dentro del frame 'miframe' 
itetiqueta.grid(row = 10, 
                column = 2, 
                padx = 10, 
                pady = 10)

#esto es para que la ventana se mantenga abierta mientras que no se active el evento 'cerrar ventana' al dar click en el botón que tiene unua equiz en la parte superior de la ventana
window.mainloop()