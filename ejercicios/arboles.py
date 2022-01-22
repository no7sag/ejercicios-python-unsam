# arboles.py - Ejercicio 5.26
# https://programacionpython.ecyt.unsam.edu.ar/material/05_Random_Plt_Dbg/05_Arboles3_plt/
#
# Tomamos el dataset del arbolado porteño (arbolado-en-espacios-verdes.csv)
# para realizar algunos gráficos que nos permitan visualizar los datos.

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Ruta al dataset Arbolado de Espacios Verdes (Buenos Aires Data)
# https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes
# Fecha de actualización: 19 de Mayo de 2021
directorio = os.path.dirname(__file__)
archivo = os.path.join(directorio, "dataset", "arbolado-en-espacios-verdes.csv")


def leer_arboles(nombre_archivo):
    """ Devuelve una lista conteniendo un diccionario por cada árbol
        con todos los datos """
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        # Preestablecemos el tipo de dato de cada columna
        tipos = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
        # Por cada fila en "rows", creamos diccionarios iterando por las tuplas/zips creadas,
        # cuyas claves serán los encabezados y sus valores el valor correspondiente a su respectiva columna
        #  [func(val) for func, val in zip(tipos, row)]  =  lista con los valores
        arboleda = [dict(zip(headers,[func(val) for func,val in zip(tipos, row)])) for row in rows]
        return arboleda


def altos_jacaranda(arboleda):
    """ Devuelve la lista de alturas de los Jacarandás """
    return [float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]


def diam_y_alt(arboleda):
    """ Devuelve una lista con tuplas de longitud 2 (pares) conteniendo
        el alto y el diámetro de cada Jacarandá """
    return [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]


def hist_jacaranda():
    """ Genera un histograma con las alturas de los Jacarandás """
    arboleda = leer_arboles(archivo)
    altos = altos_jacaranda(arboleda)
    
    plt.figure(0)  # Determino en qué plot graficar para no pisar lo que siga
    plt.title("Lista de altos de Jacarandá")
    plt.xlabel("Altura (m)")
    plt.ylabel("Cantidad")
    plt.hist(altos, bins=26)


def scatter_hd(lista_de_pares):
    """ Genera un gráfico de dispersión (scatterplot) para visualizar
        la relación entre altura y diámetro de los Jacarandás """
    # Vectores con cada eje (diámetro y altura)
    d = np.array([ i[0] for i in lista_de_pares ])
    h = np.array([ i[1] for i in lista_de_pares ])
    
    plt.figure(1)
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlabel("Diámetro (cm)")
    plt.ylabel("Altura (m)")
    plt.scatter(d, h, c='#006600', alpha=0.33)


if __name__ == "__main__":
    arboleda = leer_arboles(archivo)
    d_h = diam_y_alt(arboleda)
    hist_jacaranda()
    scatter_hd(d_h)
