import csv

def obtener_tipos_aeropuerto(archivo_csv):
    
    """
    Esta función extrae los tipos únicos de aeropuertos presentes en un archivo CSV y los devuelve como una lista.

    Args:
        archivo_csv (str): Ruta del archivo CSV que contiene los datos de los aeropuertos.
        columna (int): Índice de la columna en el archivo CSV que contiene el tipo de aeropuerto (contando desde 0).

    """
    columna = 2 # Índice de la columna "type"
    tipos_aeropuerto = set()  # Se usa set (conjunto) para evitar duplicados
    
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Se saltea la primera fila de titulos
        for row in reader:
            tipo = row[columna]
            tipos_aeropuerto.add(tipo)  # Se cargan los tipos al conjunto
    
    return list(tipos_aeropuerto) # Se retorna el conjunto
