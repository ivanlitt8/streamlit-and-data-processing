from pathlib import Path
import csv

"""El modulo funciona de la siguiente forma:  Al ser invocado desde trabajo_integrador, se le pasa como parametro el path del archivo que
debe ser copiado. Se abre el archivo en modo lectura y con un reader que provee el csv y se agregan en una lista todos los elementos dentro de el.
Luego se genera un archivo con el mismo nombre pero en otra carpeta. 
Realizado esto, se genera un writer con el modulo csv y se escriben todos los elementos de la lista generada anteriormente, sobre el archivo."""
def generar_copia (archivo): #Recibo el archivo como parametro cuando es llamado desde trabajo_integrador
    with open(archivo, "r", encoding='utf-8', newline='') as file:
        info = csv.reader(file)
        header = next(info)
        lista = [] #Creo una lista para agregar los datos dentro del archivo
        lista.append(header) #Agrego el encabezado
        for line in info:
            lista.append(line) #A cada linea que itero del archivo la agrego dentro de la lista
    copia_conectividad = Path("new_datasets") / "Conectividad_Internet.csv" #Genero un archivo con el mismo nombre (pero en otra carpeta) donde voy a escribir los datos del original
    with open(copia_conectividad, 'w',encoding='utf-8', newline="") as copy:
        writer = csv.writer(copy) #Asigno un writer que va a escribir sobre el archivo copia
        for elem in lista:
            writer.writerow(elem) #A cada elemento dentro de la lista lo escribo en el archivo


"""
Este modulo efectua las modificaciones que pedia el apartado de Procesamiento en el inciso 2, donde se pedia que a cada elemento que sea '--'
se lo reemplace con un 'No', ademas de controlar que las regiones que se encontraban en el archivo cuenten con internet. Verificados estos datos se debia armar una
nueva columna llamada 'Posee Conectividad', donde sus valores son si o no dependiendo del resultado que de el control de conexion.
Para esto llamo al archivo que fue copiado (de esta forma no se altera el original), en modo lectura. Con un reader empiezo a iterar sobre sus elementos
para posteriormente guardarlos sobre una lista, si encuentro elementos como '--' los cuento con la funcion sum y luego los reemplazo por la palabra 'NO'.
Una vez procesado todo el archivo, lo sobreescribo (por cuestiones de eficiencia no leo y escribo al mismo tiempo, ya que podria presentar errores) 
"""
def procesar_conectividad():
    file = Path("new_datasets") / "Conectividad_Internet.csv" #Traigo la copia del archivo
    with open(file, 'r', encoding='utf-8', newline='') as arc:
        info = csv.reader(arc)
        header = next(info)
        header.append('Posee Conectividad') #Agrego la columna Posee Conectividad solicitada por el inciso
        lineas = [header]
        for line in info:
            cant = sum(1 for elem in line[4:13] if elem == "--") #Sumo la cantidad de veces que aparece un '--' en cada linea del archivo
            for i in range(4, 13):
                if line[i] == "--":
                    line[i] = "NO"  #Si es verdadero el caso, reemplazo las lineas por un NO
            if cant == 9:
                line.append("NO") #Llegado al caso donde el contador cant es igual a 9 (ya que 9 son los tipos de conexion disponibles), esto indica
                                    #que la localidad no posee conexion, por ende se agrega el no al final de la lista, quedando al margen de la columna Posee Conectividad
            else:
                line.append("SI") #Caso de que cant no sea 9, indica que tiene una forma de conexion, por lo que se le agrega si al final de la lista, al margen de Posee Conectividad
            lineas.append(line) #

    with open(file, 'w', encoding='utf-8', newline='') as arc:
        writer = csv.writer(arc)
        writer.writerows(lineas) #Se sobreescriben las lineas de la lista sobre el archivo, dejando los datos modificados correctamente
            

def controlar_archivos (archivo):
    try: #Si el archivo se abre exitosamente, el programa imprimira en pantalla que el archivo ya existe
        with open(archivo, "r", encoding='utf-8', newline='') as file:
            print('El archivo ya existe') #Si el archivo se abre exitosamente, 
    except: #caso contrario, genera una copia del arhivo original y lo procesa
        original = Path ("datasets") / "Conectividad_Internet.csv"
        generar_copia(original)
        procesar_conectividad()
        print ('Copia del archivo generada y procesada')
