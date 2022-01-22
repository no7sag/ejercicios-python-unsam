# plot_bbin_vs_bsec.py - Ejercicio 6.20
# https://programacionpython.ecyt.unsam.edu.ar/material/06_Organizacion_y_Complejidad/07_graficos_de_complejidad/
#
# Usando las funciones experimento_secuencial_promedio y experimento_binario_promedio,
# las cuales devuelven la cantidad de comparaciones que realizan en promedio
# la búsquedas secuencial y la búsqueda binaria sobre una lista pasada como parámetro, 
# graficamos los resultados de estos experimentos para listas de largo entre 1 y 256.

import random
import matplotlib.pyplot as plt
import numpy as np

def generar_lista(n, m):
    """ Devuelve una lista con k elementos de números
        entre 0 y m """
    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m-1)


def busqueda_secuencial(lista, x):
    """ Si x está en la lista devuelve el índice de su primera aparición, 
        de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
        que hace la función. """
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def busqueda_binaria(lista, x):
    """Búsqueda binaria"""
    comps = 0  # Contador de comprobaciones
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio      # Elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # Descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos, comps


def experimento_secuencial_promedio(lista, m, k):
    """Devuelve el promedio de comprobaciones en búsqueda secuencial"""
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    """Devuelve el promedio de comprobaciones en búsqueda binaria"""
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom


def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1  # Estos son los largos de listas que voy a usar
    # Promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_sec_promedio = np.zeros(256)
    comps_bin_promedio = np.zeros(256)
    
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)  # Genero lista de largo n
        comps_sec_promedio[i] = experimento_secuencial_promedio(lista, m, k)
        comps_bin_promedio[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos,comps_sec_promedio, label = "Búsqueda Secuencial")
    plt.plot(largos,comps_bin_promedio, label = "Búsqueda Binaria")
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()  # Mostrar referencia de cada curva
    plt.ylim(0,25)
    plt.show()


if __name__ == "__main__":
    m = 10000  # Rango de números
    n = 100  # Cant. de elementos en lista de números random ordenada
    k = 1000  # Cantidad de experimentos
    graficar_bbin_vs_bseq(m, k)
