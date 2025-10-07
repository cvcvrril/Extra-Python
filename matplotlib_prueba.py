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
    fig, ax = plt.subplots()                                            #definimos la figura (fig) y los ejes (ax)
    ax.plot([1,2,3,4], [1,4,2,3])                                       #primera línea; primer array marca las x's, segundo array marca las y's
    ax.plot([1,2,5], [2,4,3], 'ro')                                     #segunda línea, le hemos establecido que sustituya la línea por puntos
    plt.title('Ejemplo Plot Sencillo')                                  #el título del gráfico
    plt.ylabel('y')                                                     #de esta forma establecemos un texto en el eje y
    plt.xlabel('x')                                                     #de esta forma establecemos un texto en el eje x
    plt.show()                                                          #llamamos a la función show(), que se encargará de enseñar el gráfico generado


def ejemplo_scatter_sencillo():
    np.random.seed(3)                                                   #generamos una semilla random
    x = 4 + np.random.normal(0, 2, 24)                                  #vamos a generar 24 valores random para x
    y = 4 + np.random.normal(0, 2, len(x))                              #vamos a generar 
    sizes = 10                                                          #establecemos que el tamaño de las bolitas sea 10
    colors = 'b'                                                        #establecemos que el color de las bolitas sea el azul
    fig, ax = plt.subplots()                                            #definimos la figura (fig) y los ejes (ax)
    ax.scatter(x,y,s = sizes, c = colors, vmin=0, vmax=100)             #dibujamos el gráfico
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),                         #límites de x
       ylim=(0, 8), yticks=np.arange(1, 8))                             #límites de y
    plt.show()                                                          #llamamos a la función show(), que se encargará de enseñar el gráfico generado


def ejemplo_bar_sencillo():
    x = 0.5 + np.arange(8)                                              #generamos los valores de posición x para las barras (del 0.5 al 7.5)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]                        #generamos los valores de posición y, es decir, la altura de las barras
    fig, ax = plt.subplots()                                            #definimos la figura (fig) y los ejes (ax)
    ax.bar(x, y, width=1, edgecolor="black", linewidth=0.7)             #dibujamos el gráfico, establecemos que el borde sea negro
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),                         #eje x
       ylim=(0, 8), yticks=np.arange(1, 8))                             #eje y
    plt.show()                                                          #llamamos a la función show(), que se encargará de enseñar el gráfico generado

def ejemplo_hist_sencillo():
    np.random.seed(1)                                                   #establecemos la semilla para generar valores aleatorios con random
    x = 4 + np.random.normal(0, 1.5, 200)                               #vamos a generar 200 valores aleatorios, 
    fig, ax = plt.subplots()                                            #definimos la figura (fig) y los ejes (ax)
    ax.hist(x, bins=8, linewidth=0.5, edgecolor="purple")               #dibujamos el histograma, establecemos que el borde sea rojo
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),                         #establecemos el eje x, con sus limites
        ylim=(0, 56), yticks=np.linspace(0, 56, 9))                     #establecemos el eje y, con sus limites
    plt.show()                                                          #llamamos a la función show(), que se encargará de enseñar el gráfico generado

def ejemplo_pie_sencillo():
    x = [1, 2, 3, 4]                                                    #los valores para las proporciones de cada gráfico
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))        #vamos a establecer la gama de colores a usar, en este caso de rojos
    fig, ax = plt.subplots()                                            #definimos la figura (fig) y los ejes (ax)
    ax.pie(x, colors=colors, radius=3, center=(4, 4),                   #dibujamos el pastel con los valores, el color, el radio, y la posicion central
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)   #el estilo de los bordes
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),                         #se configura el eje x
       ylim=(0, 8), yticks=np.arange(1, 8))                             #se configura el eje y
    plt.show()                                                          #llamamos a la función show(), que se encargará de enseñar el gráfico generado

'''

EJECUCIONES
-----------

'''

#ejemplo_plot_sencillo()
#ejemplo_scatter_sencillo()
#ejemplo_bar_sencillo()
#ejemplo_hist_sencillo()
ejemplo_pie_sencillo()

'''
REFERENCIAS
-----------

Primeros pasos: https://matplotlib.org/stable/users/explain/quick_start.html
Tipos de gráficos: https://matplotlib.org/stable/plot_types/index.html
Tutorial pyplot: https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py
Turorial histogramas: https://matplotlib.org/stable/gallery/statistics/hist.html
Tutorial pie: https://matplotlib.org/stable/plot_types/stats/pie.html#sphx-glr-plot-types-stats-pie-py

'''