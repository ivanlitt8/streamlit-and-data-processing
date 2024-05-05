import csv

"""Mostrar las provincias para las cuales todas sus ciudades poseen FIBRA ÓPTICA."""

"""
Para la consulta 11, abro el archivo en modo lectura. Creo una lista con todas las provincias de la Republica Argentina para poder comparar
dentro del archivo de conectividad, cuales de las ciudad de la provincia NO tiene fibra optica. Si bien el ejercicio me pide mostrar cuales provincias
si tienen a todas sus ciudades con fibra optica, la opcion mas rentable es preguntar si existe alguna que no, dado el caso de que esto pase, se elimina
a la provincia de la lista de provincias.
"""


"""Lista con todas las provincias que existen en Argentina"""
provincias = [
    "BUENOS AIRES",
    "CABA",
    "CATAMARCA",
    "CHACO",
    "CHUBUT",
    "CORDOBA",
    "CORRIENTES",
    "ENTRE RIOS",
    "FORMOSA",
    "JUJUY",
    "LA PAMPA",
    "LA RIOJA",
    "MENDOZA",
    "MISIONES",
    "NEUQUEN",
    "RIO NEGRO",
    "SALTA",
    "SAN JUAN",
    "SAN LUIS",
    "SANTA CRUZ",
    "SANTA FE",
    "SANTIAGO DEL ESTERO",
    "TIERRA DEL FUEGO",
    "TUCUMAN"
]

def mostrar_provincias (archivo):
    with open (archivo, "r", encoding = "utf-8", newline = "") as arc: #Abro el archivo conectividad_internet en modo lectura
        reader = csv.reader(arc) #Creo un reader para iterar sobre el archivo
        next(reader) #Hago un salto ya que no necesito el header 
        posFibra = 7 #Posicion del archivo que me indica el valor para cada elemento de la fibra optica
        posProv = 0 #Posicion del archivo que me indica la provincia
        for elem in reader:
            if (elem[posProv] in provincias ):
                if (elem[posFibra] == "NO"): #Si existe el caso donde la provincia que se encuentra en la lista no posee fibra optica en 1 de sus ciudades, se eliminara de la lista
                    provincias.pop(provincias.index(elem[posProv]))
    provincias.sort() #Ordeno la lista 
    print ("Las provincias que poseen Fibra Optica son: ")
    for elem in provincias: #Imprimo las provincias cuyas ciudades tienen todas fibra optica
        print(elem)