import csv
from pathlib import Path


def ingreso_parametros():
    '''Esta función retorna los parametros de busqueda ingresados por el usuario'''
    opciones = {"1": "mayor", "2": "menor"}  # Diccionario para mapear las opciones a los valores de búsqueda
    
    while True:
        numero_poblacion = input("Ingrese el numero de poblacion que desee: ")
        try:
            numero_poblacion = int(numero_poblacion)  # Intenta convertir la entrada a entero
            break  # Sale del bucle si la conversión tiene éxito
        except ValueError:  # Captura el error si la conversión falla
            print("No se ingreso un valor valido, intente de nuevo")
    
    print("Seleccione una opción:")
    print("1. Mayor")
    print("2. Menor")
    
    while True:
        opcion = str(input("Ingrese el número de la opción: "))
        if opcion in opciones:  # Verificar si la opción está en las claves del diccionario opciones
            mayor_menor = opciones[opcion]  # Asignar la opción elegida a mayor_menor
            break  # Salir del bucle si la opción es válida
        else:
            print("Opción inválida, por favor seleccione 1 o 2.")
    
    return numero_poblacion, mayor_menor # Retorna los parametros ingresados 

def proceso_provincias(valor, mayor_menor):
    '''Esta función recibe los parametros a usar y busca las provincias dentro del dataset c2022_tp_c_resumen_adaptado.csv que los cumplan, luego las retorna en una lista'''
    ruta1 = Path ("new_datasets") / "c2022_tp_c_resumen_adaptado.csv" # Ruta del archivo
    with open(ruta1, "r", encoding="utf-8", newline="") as archivo: 
        csv_reader = csv.reader(archivo) # Objeto iterador con los contenidos del csv
        next(csv_reader) # Se salta el header, la 1ra fila y la 2da fila, ya que estas representan el total del pais y a CABA
        next(csv_reader)
        next(csv_reader)
        lista_provincias = [] # Lista que guarda el nombre de las provincias que cumplen el parametro
        if mayor_menor == "mayor": # Se decide el criterio de busqueda dependiendo lo ingresado por el usuario
            for fila in csv_reader:
                if int(fila[1]) > valor: # Guarda el nombre de las provincias con mayor poblacion que el parametro
                    lista_provincias.append(fila[0].lower())
        else:
            for fila in csv_reader:
                if int(fila[1]) < valor: # Guarda el nombre de las provincias con menor poblacion que el parametro
                    lista_provincias.append(fila[0].lower()) 
    return lista_provincias # Devuelve la lista con las provincias

def tipo_conec(lista_prov):
    '''Esta función recibe la lista de las provincias e imprime los tipos de conectividad existentes en dichas provincias'''
    ruta1 = Path ("new_datasets") / "Conectividad_Internet.csv"
    with open(ruta1, "r", encoding="utf-8", newline="") as archivo:
        csv_reader =  csv.reader(archivo) # Objeto iterador con los contenidos del csv
        header = next(csv_reader) # Guardo el header
        prov_act = "" # Variable que guarda la provincia actual
        lista_conec =[] # Lista que tendra los tipos de conectividad disponibles en cada prov
        csv_reader = sorted(csv_reader, key = lambda x: x[0]) # Ordena los datos del csv por provincia
        for fila in csv_reader:
            if fila[0].lower() in lista_prov:
                if prov_act != fila[0].lower(): 
                    if len(lista_conec) > 0: # Si existen tipos de conectividad los imprime
                        print(lista_conec)
                    prov_act = fila[0].lower() # Cambia la provincia actual
                    lista_conec =[] # Reinicia la lista contadora de tipos
                for i in range(4,13): 
                    if fila[i] == "SI" and header[i] not in lista_conec: 
                        lista_conec.append(header[i]) # Si existe el tipo de conectividad y no esta en la lista, lo agrega
        if len(lista_conec) > 0:
            print(lista_conec) # Imprime los datos de la ultima provincia valida

def lagos(lista_prov):
    '''Esta función recibe la lista de provincias e imprime los lagos que existan en dichas provincias'''
    ruta1 = Path ("new_datasets") / "lagos_arg.csv"
    with open(ruta1, "r", encoding="utf-8", newline="") as archivo:
        csv_reader = csv.reader(archivo) # Objeto iterador con los contenidos del csv
        next(csv_reader)
        for fila in csv_reader:
            prov = limpiar_tildes(fila[1].lower())
            if prov in lista_prov: # Si la provincia donde se encuentra el lago esta en la lista, imprime el nombre del lago
                print(fila[0])

def aeropuertos(lista_prov):
    '''Esta función recibe la lista de provincias e imprime los aeropuertos existentes en dichas provincias'''
    ruta1 = Path ("new_datasets") / "ar-airports.csv"
    with open(ruta1, "r", encoding="utf-8", newline="") as archivo:
        csv_reader = csv.reader(archivo) # Objeto iterador con los contenidos del csv
        next(csv_reader) # Saltea el header
        for fila in csv_reader:
            if fila[24].lower() in lista_prov: # Si la provincia esta en la lista, imprime el nombre del aeropuerto
                print(fila[3])

def limpiar_tildes(lista):
    '''Esta función limpia los tildes de un string o lista ingresada por parametro'''
    caracs = {
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
    if type(lista) == str: # Si se ingresa un string, se devuelve sin tildes
        palabra_sin_tildes = lista.translate(str.maketrans(caracs))
        return palabra_sin_tildes
    else:
        new_lista = [] # Lista nueva
        for item in lista:
            new_lista.append(item.translate(str.maketrans(caracs))) # Le agrega a la lista las palabras sin tildes
        return new_lista # Devuelve la lista sin tildes

def consulta_4():
    '''Esta función realiza la consulta 4, informando los lagos, aeropuertos y tipos de conectividad existentes en las provincias con poblacion mayor o menor (depende como lo decida el usuario) a un numero ingresado por el usuario'''
    param_valor, param_tipo = ingreso_parametros() # Llama a ingreso parametros donde se deciden los parametros de busqueda y los guarda en variables
    lista_provincias = proceso_provincias(param_valor, param_tipo) # Llama a proceso_provincias que devuelve una lista con las provincias que cumplen con los requisitos
    lista_provincias = limpiar_tildes(lista_provincias) # Limpia las tildes
    tipo_conec(lista_provincias) # Informa los tipos de conectividad 
    lagos(lista_provincias) # Informa los lagos
    aeropuertos(lista_provincias) # Informa los aeropuertos