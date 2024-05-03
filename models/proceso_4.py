from pathlib import Path 
import csv 

ruta_copia = "new_datasets/c2022_tp_c_resumen_adaptado.csv"
ruta_origen = "datasets/c2022_tp_c_resumen_adaptado.csv"

"""
Funcion crear_copia

se encarga de crear una copia del archivo con la que es cargada

args: direccion del datasets a copiar
return: ---
"""

def crear_copia(archivo):
  "se abre el archivo en modo lectura"
  with open(archivo, "r", encoding='utf-8', newline='') as file:
    data = csv.reader(file) 
    header = next(data)    
    list = []          
    list.append(header)
    "se salta la primera fila (header) y luego la agrega a la lista"     
    for line in data:
      list.append(line)
      "se agrega a la nueva lista todas las lineas de el archivo"      
    copia_censo = Path('new_datasets') / 'c2022_tp_c_resumen_adaptado.csv'
    "se abre un archivo nuevo en la direccion de copia_censo y se guarda la lista nueva "
    with open(copia_censo, 'w',encoding='utf-8', newline="") as copy:
      writer = csv.writer(copy)
      for elem in list:
        writer.writerow(elem)


"""
Funcion modificar_lista

se encarga de revisar cada dato de la lista y reemplazarlo de ser necesario

args: la lista a revisar y una variable con los caracteres a reemplazar
return: devuelve la misma lista modificada

"""




def modificar_lista(lista,reemplazables):
  porc = lambda x,y: (x*100) / y
  "Se crea un lambda que hace una regla de tres simples para sacar el porcentaje de gente en situacion de calle"
  for dato in range(13):
    if lista[dato] in reemplazables:
      lista[dato] = "0"
  "Se recorre la lista en busca de un elemento que pertenezca a reemplazables, si se lo encuentra se lo reemplaza con 0"
  Porc_pobreza = porc(int(lista[4]),int(lista[1]))
  lista.append(str(Porc_pobreza))
  "Se crea una variable con el porcentaje de poblacion en situacion de calle y se la agrega a la lista"
  return lista


"""
Funcion procesar_datos_censo

se encarga de modificar el archivo recibido, agrega una columna con el porcentaje de poblacion viviendo en la calle y reemplaza los caracteres "///","-"por "0" y guarda en los nuevos datasets el archivo modificado

args: la direccion del archivo a modificar y la direccion en la que se lo debe guardar
return: ---

"""


def procesar_datos_censo(censo_csv,csv_direccion):
  with open(censo_csv, encoding="utf-8") as file_csv:
      csv_reader = csv.reader(file_csv, delimiter=',')
      "Se abre el archivo en modo lectura"
      header, archivo = next(csv_reader), list(csv_reader)
      "Se crean dos variables, una con la primera linea de valores y otra con las siguientes"
      header.append("Porcentaje_en_situacion_de_calle")
      new_list=[]
      "Se crea una variables con los caracteres a reemplazar"
      reemplazables = "///","-"
      new_list.append(header)
      for lista in archivo:
        lista = modificar_lista(lista,reemplazables)
        new_list.append(lista)
      "Se recorre la lista de listas y se modifican usando la funcion modificar_lista"
  csv_modificado="c2022_tp_c_resumen_adaptado.csv"
  direccion= Path(csv_direccion)/csv_modificado
  "Se guarda en la la variable direccion la direccion del archivo a modificar"
  with open(direccion,"w",encoding="utf-8",newline="") as archivo_mod:
     csv_writer=csv.writer(archivo_mod)
     for fila in new_list:
        csv_writer.writerow(fila)
     "Se guarda el archivo modificado en new_datasets"

ruta_csv= Path ("new_datasets") / "c2022_tp_c_resumen_adaptado.csv"
ruta_origen = Path ("datasets") / "c2022_tp_c_resumen_adaptado.csv"

crear_copia(ruta_origen)
procesar_datos_censo(ruta_csv,"new_datasets")