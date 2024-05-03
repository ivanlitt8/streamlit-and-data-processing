################## RAMIRO ##################
from pathlib import Path
from models import proceso_2

"""
En este segmento, traigo el path del archivo nuevo para comparar dentro del proceso controlar archivos
"""
path_conectividad = Path ('new_datasets') / "Conectividad_Internet.csv"
proceso_2.controlar_archivos(path_conectividad)

################## IVAN ##################
from models import proceso_1

from pathlib import Path
route1 = Path('datasets') / 'ar-airports.csv'
route2 = Path('datasets') / 'ar.csv'

proceso_1.generar_copia(route1)
proceso_1.cargar_datos_ar(route2)
proceso_1.procesar_airports()

#################### Isidro ######################

from models import proceso_3 
from pathlib import Path
ruta_csv = Path ("datasets") / "lagos_arg.csv" # Guarda la ruta del archivo csv en ruta_csv
proceso_3.procesar_dataset_lagos(ruta_csv, "new_datasets") # Llama a procesar_dataset_lagos enviandole la ruta del dataset original y donde debe guardarlo


##################### Augusto ####################

from models import proceso_4
from pathlib import Path

ruta_csv= Path ("new_datasets") / "c2022_tp_c_resumen_adaptado.csv"
ruta_origen = Path ("datasets") / "c2022_tp_c_resumen_adaptado.csv"

proceso_4.crear_copia(ruta_origen)
proceso_4.procesar_datos_censo(ruta_csv,"new_datasets")
