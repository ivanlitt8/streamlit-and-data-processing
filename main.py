from pathlib import Path
from models import proceso_1, proceso_2, proceso_3, proceso_4

def procesar_conectividad():
    
    path_conectividad = Path ('datasets') / "Conectividad_Internet.csv"
    
    proceso_2.generar_copia(path_conectividad)
    proceso_2.procesar_conectividad()

def procesar_aeropuertos():
    
    ruta_aeropuertos = Path('datasets') / 'ar-airports.csv'
    ruta_argentina = Path('datasets') / 'ar.csv'

    proceso_1.generar_copia(ruta_aeropuertos)
    proceso_1.cargar_datos_ar(ruta_argentina)
    proceso_1.procesar_airports()

def procesar_lagos ():
    
    ruta_csv = Path ("datasets") / "lagos_arg.csv" # Guarda la ruta del archivo csv en ruta_csv
    ruta_csv_procesada = Path ("new_datasets") / "lagos_arg.csv"

    proceso_3.procesar_dataset_lagos(ruta_csv, ruta_csv_procesada) # Llama a procesar_dataset_lagos enviandole la ruta del dataset original y donde debe guardarlo

def procesar_censo ():

    ruta_csv= Path ("new_datasets") / "c2022_tp_c_resumen_adaptado.csv"
    ruta_origen = Path ("datasets") / "c2022_tp_c_resumen_adaptado.csv"

    proceso_4.crear_copia(ruta_origen)
    proceso_4.procesar_datos_censo(ruta_csv,"new_datasets")
