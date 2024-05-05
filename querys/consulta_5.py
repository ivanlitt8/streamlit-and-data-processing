import csv


# Diccionario de Provincias-Capitales para hacer validación
capitales_provinciales = {
    "Buenos Aires": "La Plata",
    "Catamarca": "Catamarca",
    "Chaco": "Resistencia",
    "Chubut": "Rawson",
    "Cordoba": "Cordoba",
    "Corrientes": "Corrientes",
    "Entre Rios": "Parana",
    "Formosa": "Formosa",
    "Jujuy": "San Salvador de Jujuy",
    "La Pampa": "Santa Rosa",
    "La Rioja": "La Rioja",
    "Mendoza": "Mendoza",
    "Misiones": "Posadas",
    "Neuquen": "Neuquen",
    "Rio Negro": "Viedma",
    "Salta": "Salta",
    "San Juan": "San Juan",
    "San Luis": "San Luis",
    "Santa Cruz": "Rio Gallegos",
    "Santa Fe": "Santa Fe",
    "Santiago del Estero": "Santiago del Estero",
    "Tierra del Fuego, Antartida e Islas del Atlantico Sur": "Ushuaia",
    "Tucuman": "San Miguel de Tucuman"
}

# Función para quitar tildes
def quitar_tildes(texto):
    
    tildes = {      # dicionario de sustitucion de tildes
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

def imprimir_aeropuertos_por_provincia(archivo_csv):
    
    """
    Imprime una lista de aeropuertos para cada capital de provincia.

    Args:
        archivo_csv (str): Ruta del archivo CSV que contiene los datos de los aeropuertos.

    No devuelve ningún valor.

    """
    
    aeropuertos_por_provincia = {capital: [] for capital in capitales_provinciales.values()}

    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Se saltea la primera fila de titulos
        for row in reader:
            ciudad = quitar_tildes(row[13])  # Se eliminan los tildes de la ciudad
            provincia = quitar_tildes(row[24])   # Se eliminan los tildes de la provincia
            aeropuerto = row[3] # Se obtiene el nombre del aeropuerto

            capital_provincia = capitales_provinciales.get(provincia) # Se obtiene la capital de la provincia con el diccionario
            if capital_provincia and quitar_tildes(ciudad.lower()) == quitar_tildes(capital_provincia.lower()):
                aeropuertos_por_provincia[capital_provincia].append(aeropuerto) # Se agrega el aeropuerto a la lista de la capital
                

    for capital, aeropuertos in aeropuertos_por_provincia.items():
        
        """
        Recorre el diccionario aeropuertos_por_provincia e imprime una lista de aeropuertos para cada capital de provincia.
        """
        print(f"--- Aeropuertos en {capital} ---")
        for aeropuerto in sorted(aeropuertos): # Se imprimen los aeropuertos ordenados
            print(aeropuerto)
