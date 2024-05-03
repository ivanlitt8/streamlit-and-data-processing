import csv

def pedir_altura():
    
    """
    Solicita al usuario que ingrese un número que represente una altura y lo valida.

    No recibe parámetros.

    Devuelve:
        float: La altura ingresada por el usuario.

    """
    
    altura = input("Ingrese un número que represente una altura: ")
    
    # Sino se ingresa un dato de tipo float se vovera a pedir una altura    
    try:
        altura = float(altura)
        return altura
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return pedir_altura()

def pedir_opcion():
    
    """
    Muestra un menú con las opciones disponibles para el usuario y solicita al usuario que ingrese una opción.

    No recibe parámetros.

    Devuelve:
        str: La opción elegida por el usuario ("mayor" o "menor").

    """
    
    print("Seleccione una opción:")
    print("1. Mayor")
    print("2. Menor")
    opcion = input("Ingrese el número de la opción que desea: ")
    if opcion == '1':
        return 'mayor'
    elif opcion == '2':
        return 'menor'
    else:
        print("Opción inválida. Por favor, ingrese '1' o '2'.")
        return pedir_opcion()

def procesar_archivo_alturas(archivo_csv, altura, opcion_elegida):
    
    """
    Recorre un archivo CSV y muestra los nombres de los aeropuertos que tienen una altura mayor o menor (según la opción elegida) a la altura especificada por el usuario.

    Args:
        archivo_csv (str): Ruta del archivo CSV que contiene los datos de los aeropuertos.
        altura (float): La altura ingresada por el usuario.
        opcion_elegida (str): La opción elegida por el usuario ("mayor" o "menor").

    No devuelve ningún valor.
    """
    
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Se saltea la primera fila con titulos
        for row in reader:
            # Se usa try por posibles espacios en blanco
            try:
                # Toma la altura de la celda y valida segun las opciones e imprime
                altura_en_archivo = float(row[6])
                if opcion_elegida == 'mayor' and altura_en_archivo > altura:
                    print("Nombre Aeropuerto:", row[3]) 
                elif opcion_elegida == 'menor' and altura_en_archivo < altura:
                    print("Nombre Aeropuerto:", row[3])
            except ValueError:
                pass # Se saltean las celdas sin valores

def main():
    
    """
    Función principal del programa.

    No recibe parámetros.

    No devuelve ningún valor.
    """
    
    archivo_csv = 'new_datasets/ar-airports.csv'  # Ruta temporal de archivo (Cambiar con Path)
    altura = pedir_altura()
    opcion_elegida = pedir_opcion()
    procesar_archivo_alturas(archivo_csv, altura, opcion_elegida)

if __name__ == "__main__":
    main()