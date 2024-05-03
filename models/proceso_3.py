import csv
from pathlib import Path
def generar_copia(ruta_csv, ruta_nueva):
    '''Esta función recibe la ruta del csv y crea una copia de su contenido, luego la guarda en la nueva ruta'''
    with open(ruta_csv, encoding="utf-8", newline="") as archivo:
        lista_datos = [] # Lista para almacenar los datos del csv
        csv_reader = csv.reader(archivo) # Carga los datos del csv en csv_reader
        for fila in csv_reader:
            lista_datos.append(fila) # Copia cada fila del csv en la lista
    with open(ruta_nueva, "w", encoding="utf-8", newline="") as archivo_csv: # Crea el nuevo csv
        csv_writer = csv.writer(archivo_csv) 
        for fila in lista_datos: # Copia los datos en el nuevo csv
            csv_writer.writerow(fila) 

def cambiar_coordenadas(coords):
    '''Esta funcion recibe coordenadas en formato GMS y devuelve su equivalente en latitud y longitud'''
    characters = ("'", "°", '"')
    coords_separadas = coords.split(" ")
    # Limpia los caracteres especiales
    for character in characters:
        coords_separadas[0] = coords_separadas[0].replace(character, " ")
        coords_separadas[1] = coords_separadas[1].replace(character, " ")
    coords_separadas[0] = coords_separadas[0].replace("Â", "")
    coords_separadas[1] = coords_separadas[1].replace("Â", "")
    # Crea listas para la conversion a GS (las listas contienen los grados, minutos y segundos)
    lat_valores = coords_separadas[0].split(" ")
    lon_valores = coords_separadas[1].split(" ")
    # Conversion a GS
    latitud = float(lat_valores[0]) + float(lat_valores[1]) / 60 + float(lat_valores[2]) / 3600
    longitud = float(lon_valores[0]) + float(lon_valores[1]) / 60 + float(lon_valores[2]) / 3600
    latitud = -latitud if lat_valores[3] == 'S' else latitud
    longitud = -longitud if lon_valores[3] == 'O' else longitud
    return latitud, longitud

def get_tamaño(tamaño):
    '''Esta función retorna chico, medio o grande segun el tamaño de la superficie recibido'''
    if tamaño <= 17:
        return "chico"
    elif tamaño <= 59:
        return "medio"
    else:
        return "grande"
    
def actualizar_datos(ruta, lista_actualizada):
    '''Esta funcion recibe los datos actualizados dentro de lista_actualizada y los escribe en la copia del csv'''
    with open(ruta, "w", encoding="utf-8", newline="") as archivo_csv: 
        csv_writer = csv.writer(archivo_csv)
        csv_writer.writerows(lista_actualizada) # Escribe los datos actualizados en el csv

def procesar_dataset_lagos(csv_ruta, csv_ruta_procesada):
    '''Esta función recibe la ruta del archivo csv a procesar, donde se le agregan 3 nuevas columnas: Sup tamaño, Latitud y Longitud, y se
    elimina la columna de coordenadas. Luego crea el nuevo csv y lo almacena en la ruta enviada por parametro'''
    generar_copia(csv_ruta, csv_ruta_procesada)
    with open(csv_ruta_procesada, encoding="utf-8", newline="") as archivo:
        csv_reader = csv.reader(archivo)
        header = next(csv_reader)
        # Agrega la columna sup tamaño al header
        header.append("Sup tamaño")
        lista_actualizada = []
        lista_actualizada.append(header) 
        for fila in csv_reader:
            # Agrega el tamaño de superficie correspondiente
            fila.append(get_tamaño(int(fila[2])))
            # Llama a la funcion cambiar_coordenadas y devuelve los valores de la latitud y longitud
            latitud, longitud = cambiar_coordenadas(fila[5])
            # Se actualiza el formato de las coordenadas
            fila[5] = str(latitud) + " " + str(longitud)
            # Se agrega la fila entera a la nueva lista para luego ser agregado a otro csv
            lista_actualizada.append(fila)
    # Actualiza los datos en el csv
    actualizar_datos(csv_ruta_procesada, lista_actualizada)