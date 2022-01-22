# random_walk.py - Ejercicio 7.12
# https://programacionpython.ecyt.unsam.edu.ar/material/07_Plt_Especificacion_y_Documentacion/07_Matplotlib/
#
# 12 caminatas al azar graficadas, tomando datos de las mismas.
# Ver docstring de la función graficar_caminatas para más información.

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(N):
    """ Genera una caminata al azar de N pasos """
    pasos = np.random.randint(-1, 2, N)
    return pasos.cumsum()  # Suma acumulativa ([2,5,4] -> [2,7,11])


def graficar_caminatas(N, C):
    """ === Caminatas al azar ===
        Grafica tres subplots en una figura que contiene:
        - Arriba, grande, C trayectorias aleatorias con N pasos c/u.
        - Abajo a la izquierda la trayectoria que más se aleja del origen.
        - Abajo a la derecha la trayectoria que menos se aleja del origen. """
    
    # Guardamos cada caminata en una lista para
    # después determinar la más y menos alejada
    trayectorias = []
    
    plt.figure(figsize=(10, 6), dpi=80)
    
    # Gráfico 1: 12 Caminatas (arriba)
    plt.subplot(2, 1, 1)
    plt.title("12 Caminatas al azar")
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.xticks([])  # Sin ticks en el eje x
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    
    for i in range(C):
        caminata = randomwalk(N)
        trayectorias.append(caminata)
        plt.plot(caminata, linewidth=0.9)
    
    # Usamos la primera caminata como la más y menos
    # alejada como predeterminada (invariante)
    mas_alejado = trayectorias[0]
    menos_alejado = trayectorias[0]
    
    for i in trayectorias:
        # Valor absoluto más alto en cada caminata
        if max(abs(mas_alejado)) < max(abs(i)):
            mas_alejado = i
        # Valor absoluto más bajo de los más altos en cada caminata
        if max(abs(menos_alejado)) > max(abs(i)):
            menos_alejado = i
    
    # Gráfico 2: Más alejado (abajo-izquierda)
    plt.subplot(2, 2, 3)
    plt.title("Caminata más alejada")
    plt.xticks([])
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    plt.plot(mas_alejado, linewidth=0.9)
    
    # Gráfico 3: Menos alejado (abajo-derecha)
    plt.subplot(2, 2, 4)
    plt.title("Caminata menos alejada")
    plt.xticks([])
    plt.ylim(-1000, 1000)
    plt.yticks([-500, 0, 500])
    plt.plot(menos_alejado, linewidth=0.9)
    
    plt.show()


if __name__ == "__main__":
    N = 100000  # Cantidad de pasos
    C = 12  # Cantidad de trayectorias
    graficar_caminatas(N, C)
