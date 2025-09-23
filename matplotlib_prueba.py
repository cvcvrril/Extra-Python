'''
Como usar matplotlib

    INSTALACIÓN

    La instalación es muy sencilla en estos equipos, escribimos lo siguiente en la terminal:

        pip install matplotlib
    
    En caso de que alguien tenga Linux y lo quiera instalar ahi, tendrá que iniciar una variable de entorno e instalarlo de esa forma. (Preguntarme directamente)

'''

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1,2,3,4], [1,4,2,3])
plt.show()


'''
Referencias:

https://matplotlib.org/stable/users/explain/quick_start.html

'''