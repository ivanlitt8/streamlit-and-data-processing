import csv
from pathlib import Path


def generar_copia(archivo):
    
    """
    Genera una copia del archivo CSV especificado en el argumento 'archivo'.

    Args:
        archivo (str): La ruta al archivo CSV que se desea copiar.

    Returns:
        None
    """
    
    # Abrir el archivo CSV original en modo lectura con codificación UTF-8
    with open(archivo, "r", encoding='utf-8', newline='') as file:
        info = csv.reader(file) # Crear un objeto lector CSV a partir del archivo
        header = next(info)    # Leer la fila de encabezado del archivo CSV
        list = []           # Crear una lista vacía para almacenar los datos
        list.append(header)     # Agregar la fila de encabezado a la lista
        
        # Leer las filas restantes del archivo CSV y agregarlas a la lista
        for line in info:
            list.append(line)
            
    # Crear un objeto de ruta para el archivo de copia
    copia_airports = Path('new_datasets') / 'ar-airports.csv'
    
    # Abrir el archivo de copia en modo escritura con codificación UTF-8
    with open(copia_airports, 'w',encoding='utf-8', newline="") as copy:
        
        # Crear un objeto escritor CSV a partir del archivo de copia
        writer = csv.writer(copy)
        
        # Escribir todas las filas de la lista de datos en el archivo de copia
        for elem in list:
            writer.writerow(elem)

# Función para quitar tildes
def quitar_tildes(texto):
    
    """
    Esta funcion elimina las tildes del texto dado.

    Args:
        texto (str): El texto del que se desea eliminar las tildes.

    Returns:
        str: El texto sin tildes.
    """
    
    tildes = {                           # dicionario de sustitucion de tildes
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U'
    }
    
    # Obtener la equivalencia sin tilde de los caracteres y los agrega al texto retornado
    return ''.join(tildes.get(c, c) for c in texto)

# Función para cargar los datos del archivo "ar.csv" en un diccionario
datos_ar = {}
def cargar_datos_ar(archivo):
    
    """
    Carga los datos del archivo CSV especificado en el argumento 'archivo' en un diccionario.

    Args:
        archivo (str): La ruta al archivo CSV que se desea cargar.

    Returns:
        dict: Un diccionario donde la clave es el nombre de la ciudad sin tildes y el valor es el valor de la columna 5 del archivo CSV (provincia).

    """
    
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Saltear la primera fila (titulos)
        for fila in lector_csv:
            ciudad = quitar_tildes(fila[0])  # Eliminar tildes de los nombres
            valor = fila[5]
            datos_ar[ciudad] = valor  # Guardar el valor de la columna 5 con el nombre de la ciudad como clave
    return datos_ar

def procesar_airports():
    
    """
    Procesa el archivo CSV "ar-airports.csv" y agrega dos nuevas columnas: "elevation_name" y "prov_name".

    Args:
        None

    Returns:
        None
    """
    
    file = Path('new_datasets') / 'ar-airports.csv' # Ruta al archivo CSV
    data = []   # Lista para almacenar los datos del archivo CSV
    
    # Nuevos títulos para las columnas que se agregan
    new_title1= 'elevation_name'
    new_title2 = 'prov_name'
    
    # Abrir el archivo CSV en modo lectura
    with open(file, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)    # Crear un objeto lector CSV
        encabezados = next(lector_csv)  # Leer la fila de títulos
        
        # Agregar los nuevos títulos a la lista de encabezados
        encabezados.append(new_title1)
        encabezados.append(new_title2)
        data.append(encabezados)    # Agregar la lista de encabezados modificada al comienzo de la lista
        
        # Procesar cada fila del archivo CSV
        for fila in lector_csv:
            try:
                elevation = int(fila[6])  # Convertir el valor de la columna 6 (elevación) a un número entero
                
                # Clasificar la elevación y agregarla a la fila
                if elevation <= 131:
                    fila.append('bajo')
                elif elevation > 131 and elevation <= 903:
                    fila.append('medio')
                elif elevation > 903:
                    fila.append('alto')
            except ValueError:
                # Si el valor está vacío, agregar "sin datos"
                fila.append('sin datos')
            data.append(fila)    # Agregar la fila procesada a la lista

    # Buscar cada valor de la columna 14 en el diccionario y agregarlo a la columna 25
    for fila in data[1:]:  # Empezar desde la segunda fila para saltear los titulos
        valor_columna_13 = quitar_tildes(fila[13])
        if valor_columna_13 in datos_ar:
            valor_diccionario = datos_ar[valor_columna_13]
            fila.insert(24, valor_diccionario)  # Insertar el valor en la columna 25 (índice 24)
        elif valor_columna_13.strip() == "":
            fila.insert(24, "SIN DATO")  # Insertar "SIN DATO" en la columna 25 (índice 24)
        else:
            fila.insert(24, "No Encontrado")  # Insertar "No Encontrado" en la columna 25 (índice 24)
            
    # Escribir los datos actualizados en un nuevo archivo CSV
    with open(file, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(data)