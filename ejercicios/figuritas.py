# figuritas.py - Ejercicio 5.15
# https://programacionpython.ecyt.unsam.edu.ar/material/05_Random_Plt_Dbg/04_Figuritas/
#
# Simulación de llenado de "n_repeticiones" álbums de "figus_total" figuritas,
# devuelva el número estimado de figuritas que hay que comprar, en promedio,
# para completar el álbum.

import random
import numpy as np


def crear_album(figus_total):
    """ Devuelve un álbum (vector) vacío con figus_total espacios
        para pegar figuritas """
    return np.zeros(figus_total, dtype=int)


def album_incompleto(A):
    """ Recibe un vector A y devuelve True si el álbum no está completo
        o False si está completo """
    return min(A) == 0


def comprar_figu(figus_total):
    """ === Simulación de compra de figurita ===
        Recibe el número total de figuritas que tiene el álbum
        (dado por el parámetro figus_total) y devuelve un número entero
        aleatorio que representa la figurita que nos tocó """
    return random.randint(1, figus_total)


def cuantas_figus(figus_total):
    """ Recibe el tamaño del álbum (figus_total) y genera un álbum nuevo,
    simula su llenado y devuelve la cantidad de figuritas que se debieron
    comprar para completarlo """
    # Variable donde contabilizaremos la cantidad de compras necesarias
    cant_compras = 0
    
    album = crear_album(figus_total)
    while album_incompleto(album) == True:
        compra = comprar_figu(figus_total)
        # Necesitamos el índice de cada figurita (0-669). Como la función
        # "comprar_figu" retorna enteros de 1 a 670, le restamos 1
        album[compra-1] += 1
        cant_compras += 1
    return cant_compras


def experimento_figus(n_repeticiones, figus_total):
    """ Simula el llenado de n_repeticiones álbums de figus_total figuritas y
        devuelve el número estimado de figuritas que hay que comprar (en promedio)
        para completar el álbum """
    l = [ cuantas_figus(figus_total) for _ in range(n_repeticiones) ]
    return np.mean(l)


if __name__ == "__main__":
    figus_total = 670
    n_repeticiones = 50
    prom = experimento_figus(n_repeticiones, figus_total)
    print(f"  Luego de realizar {n_repeticiones} experimentos, se estima que")
    print(f"  el promedio de figuritas a comprar para llenar un álbum es de {prom}.")
