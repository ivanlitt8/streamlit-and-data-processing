import csv

"""
Mostrar las cantidades de localidades con cada tipo de conectividad.
"""
"""
Para la consulta 10, abro el archivo en modo lectura, capturo el header y creo un diccionario
donde las llaves son los tipos de conexion y su valor es la cantidad de localidades que son usuarios de este tipo.
Recorriendo el archivo, aumento estos valores en base a si dicen SI (aumenta) o NO (nada)
Luego imprimo para cada llave (tipo de conexion), su valor (cantidad de usuarios)
"""

def localidades_conectividad (archivo):
    with open (archivo, "r", encoding = "utf-8", newline ="") as file: #Abro el archivo de conectividad_internet
        reader = csv.reader(file) #creo un reader para iterar sobre el archivo
        header = next(reader) #Separo el header para saber que tipos de conectividad hay
        tipos = {} #Creo un diccionario para controlar la cantidad por tipos
        for tipo in range (4,13):
            if not (header[tipo] in tipos): #Si el valor no esta en el diccionario lo agrego, inicializandolo en 0
                tipos[header[tipo]] = 0 
        for elem in reader:
            for i in range(4,13): 
                if (elem[i] == "SI"): #Si el elemento actual del reader en el rango de los tipos de conectividad es igual a si, sumo uno a su llave correspondiente en el diccionario
                    tipos[header[i]] +=1 
                    
    print("La cantidad de localidades que poseen conectividad de acuerdo a cada tipo es: ")    
    for key,value in tipos.items(): #Imprimo el diccionario
        print (key , ' : ',value)
