'''
MATPLOTLIB

    INSTALACIÓN
    -----------

    La instalación es muy sencilla en estos equipos, escribimos lo siguiente en la terminal:

        pip install matplotlib
    
    En caso de que alguien tenga Linux y lo quiera instalar ahi, tendrá que iniciar una variable de entorno e instalarlo de esa forma. (Preguntarme directamente)

'''

'''
    USO DE LA LIBRERÍA
    -----------
    Importamos de esta forma la librería matplotlib (lo encontramos en la página del tutorial).
    También agrego numpy en caso de que necesitemos manejar funciones complejas.

'''

import matplotlib.pyplot as plt
import numpy as np

'''

Varios tipos de gráficos: Pairwise, Statistical distributions, Gridded data, Irregularly gridded data, 3d.
En este corto tutorial me voy a centrar en los de tipo Pairwise, Statistical y Gridded.

'''

def ejemplo_plot_sencillo():
    fig, ax = plt.subplots()                                    #definimos la figura (fig) y los ejes (ax)
    ax.plot([1,2,3,4], [1,4,2,3])                               #primera línea; primer array marca las x's, segundo array marca las y's
    ax.plot([1,2,5], [2,4,3], 'ro')                             #segunda línea, le hemos establecido que sustituya la línea por puntos
    plt.title('Ejemplo Plot Sencillo')                          #el título del gráfico
    plt.ylabel('y')                                             #de esta forma establecemos un texto en el eje y
    plt.xlabel('x')                                             #de esta forma establecemos un texto en el eje x
    plt.show()                                                  #llamamos a la función show(), que se encargará de enseñar el gráfico generado


def ejemplo_scatter_sencillo():
    np.random.seed(3)                                           #generamos una semilla random
    x = 4 + np.random.normal(0, 2, 24)                          #vamos a generar 24 valores random para x
    y = 4 + np.random.normal(0, 2, len(x))                      #vamos a generar 
    sizes = 10
    colors = 'b'
    fig, ax = plt.subplots()
    ax.scatter(x,y,s = sizes, c = colors, vmin=0, vmax=100)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()


def ejemplo_bar_sencillo():
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


'''

EJECUCIONES
-----------

'''

#ejemplo_plot_sencillo()
#ejemplo_scatter_sencillo()
ejemplo_bar_sencillo()

'''
REFERENCIAS
-----------

https://matplotlib.org/stable/users/explain/quick_start.html
https://matplotlib.org/stable/plot_types/index.html
https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py

'''