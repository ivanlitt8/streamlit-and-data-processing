import csv


"""
Mostrar para cada provincia su capital y, si se conoce la información para dicha
capital, informar si posee conectividad (campo 'posee_conectividad' creado
previamente). En caso de no conocer la información mostrar el texto “conectividad
desconocida”
"""

"""
Para la consulta 12, abro el archivo en modo lectura, creo un diccionario donde cada provincia tiene su capital. Esto me servira para, cada elemento
que recorra del archivo, comparar si estos se encuentran en el diccionario, es decir, si a la provincia le encuentra su capital, se analizara si
posee algun tipo de conexion (valor en la columna posee_conexion = SI). Si se cumple que se encuentran las provincias y las capitales, se guardan estos datos
en una tupla (por cuestiones de que los datos sean inmutables) y se los inserta en una lista. Si se encuentra en el diccionario
provincias que no fueron procesadas, se comparara con los elementos en la lista de procesadas (provincias
que fueron analizadas) para determinar que su conectividad es desconocida, almacenando en la lista de provincias, estos datos en forma de tupla.
"""


"""Diccionario donde guardo como llave las provincias y como valor su capital"""
dict_prov = {
    "BUENOS AIRES": "La Plata",
    "CATAMARCA": "Catamarca",
    "CHACO": "Resistencia",
    "CHUBUT": "Rawson",
    "CORDOBA": "Cordoba",
    "CORRIENTES": "Corrientes",
    "ENTRE RIOS": "Parana",
    "FORMOSA": "Formosa",
    "JUJUY": "San Salvador de Jujuy",
    "LA PAMPA": "Santa Rosa",
    "LA RIOJA": "La Rioja",
    "MENDOZA": "Mendoza",
    "MISIONES": "Posadas",
    "NEUQUEN": "Neuquen",
    "RIO NEGRO": "Viedma",
    "SALTA": "Salta",
    "SAN JUAN": "San Juan",
    "SAN LUIS": "San Luis",
    "SANTA CRUZ": "Rio Gallegos",
    "SANTA FE": "Santa Fe",
    "SANTIAGO DEL ESTERO": "Santiago del Estero",
    "TIERRA DEL FUEGO, ANTARTIDA E ISLAS DEL ATLANTICO SUR": "Ushuaia",
    "TUCUMAN": "San Miguel de Tucuman"
}

def capital_con_conectividad (arc_conectividad):
    with open (arc_conectividad, "r", encoding= "utf-8", newline = "") as conec: #Abro el archivo conectividad_internet en modo lectura
        reader = csv.reader(conec) #Creo un reader para iterar sobre el archivo
        next(reader) #Salto el header ya que no lo voy a utilizar
        posProv = 0 #Posicion en el archivo donde se encuentran las provincias
        posCap = 2 #Posicion en el archivo donde se encuentran las localidades
        posCon = 16 #Posicion en el archivo que me indica si posee conexion o no
        provincias = [] #Lista de las provincias que si estan conectadas
        procesadas = [] #Lista de las provincias que fueron procesadas
        for elem in reader:
            if (elem[posProv] in dict_prov): #Si la provincia actual figura como llave dentro del diccionario
                if(elem[posCap] == dict_prov.get(elem[posProv])): #Si la localidad del elemento actual es igual al valor de la llave que fue previamente analizada
                    if (elem[posCon] == "SI"): #Si posee conectividad
                        tup = (elem[posProv], elem[posCap], "SI") #Creo una tupla donde guardo nombre de la provincia, nombre de la capital y si dispone de conectividad en una tupla
                        provincias.append(tup) #Agrego la tupla a la lista
                        procesadas.append(elem[posProv]) #Agrego la provincia a la lista de provincias procesadas
    """Esta parte del codigo me permite analizar las provincias que no fueron procesadas, por lo tanto puedo agregarlas en la lista
    de conectividad pero con un tipo desconocido de conexion"""
    for key in dict_prov:
        if not(key in procesadas): #Si la llave del diccionario no se encuentra en la lista de las provincias procesadas
            tup = (key, dict_prov.get(key), "Desconocida") #Creo una tupla donde guardo nombre de la provincia, nombre de la capital y que su conectividad es desconocida
            provincias.append(tup)#Se agrega la tupla a la lista

    for item in provincias: #
        print(f"Provincia: {item[0]} - Capital: {item[1]} - Conectividad: {item[2]}")
