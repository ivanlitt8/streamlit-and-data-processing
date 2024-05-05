import csv

"""Mostrar los diferentes tipos de conectividades."""
"""
Para esta consulta, solo necesito abrir el archivo en modo lectura, capturar el header en una variable aplicandole un slice entre las columnas
(del archivo) que contienen los tipos de conexion
"""

def mostrar_tipos_conectividad (archivo):
    with open(archivo, "r", encoding = "utf-8", newline = "") as arc: #abro el archivo de conectividad_internet
        reader = csv.reader(arc) #creo un reader para iterar sobre el archivo
        header = next(reader)[4:13] #tomo solo la porcion del header que me indica los tipos de conectividad disponibles
    print("Estos son los tipos de conectividad: ")
    for elem in header: #imprimo los tipos de conectividad
        print(elem)