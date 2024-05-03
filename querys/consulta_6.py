import csv
from pathlib import Path
def ingreso_valor():
    '''Esta funcion pide y retorna el parametro de busqueda que ingreso el usuario'''
    param_valido = ("chico", "medio", "grande") # Tupla para validar que se ingreso un tamaño valido
    parametro_de_busqueda = input("Ingrese parametro de busqueda (chico, medio, grande): ").lower()
    if parametro_de_busqueda not in param_valido:
        print("Por favor, ingrese un valor valido (chico, medio o grande)")
        return ingreso_valor()
    return parametro_de_busqueda

def consulta_6():
    '''Esta funcion muestra en pantalla los lagos cuya superficie coincide con la ingresada por el usario'''
    route_csv = Path ("new_datasets") / "lagos_arg.csv" # Ruta del dataset
    with open(route_csv, "r", newline="") as archivo: # Se carga el archivo
        csv_reader = csv.reader(archivo) 
        next(csv_reader) # Se saltea el header
        parametro_de_busqueda = ingreso_valor() # Guardo el parametro ingresado
        for fila in csv_reader:
            if fila[6] == parametro_de_busqueda: # Recorro el csv buscando los lagos que coincidan con el parametro para mostrarlos
                print(fila[0])