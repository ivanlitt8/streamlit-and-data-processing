import csv

def mostrar_menu():
    
    """
    Muestra un menú con las opciones disponibles para el usuario.

    No recibe parámetros.

    No devuelve ningún valor.
    """
    
    print("Seleccione una opción:")
    print("1. Bajo")
    print("2. Medio")
    print("3. Alto")

def elegir_opcion():
    
    """
    Solicita al usuario que ingrese una opción del menú y la valida.

    No recibe parámetros.

    Devuelve:
        str: La opción elegida por el usuario ("bajo", "medio" o "alto").

    """
    opcion = input("Ingrese el número de la opción que desea: ")
    if opcion == '1':
        return "bajo"
    elif opcion == '2':
        return "medio"
    elif opcion == '3':
        return "alto"
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
        return elegir_opcion()

def procesar_archivo(archivo_csv, opcion_elegida):
    
    """
    Recorre un archivo CSV y muestra los nombres de los aeropuertos que tienen la elevación especificada por el usuario.

    Args:
        archivo_csv (str): Ruta del archivo CSV que contiene los datos de los aeropuertos.
        opcion_elegida (str): La opción de altura elegida por el usuario ("bajo", "medio" o "alto").

    """
    
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Se saltea la primera fila de titulos
        for row in reader:
            if row[23] == opcion_elegida:  # Columna 23 posee los tipos de altura
                print("Nombre aeropuerto: ", row[3])     # Se imprime columna 3 que posee los nombres de aeropuertos

def main():
    
    """
    Función principal del programa.

    No recibe parámetros.

    No devuelve ningún valor.
    """
    
    archivo_csv = 'new_datasets/ar-airports.csv'  # Ruta temporal de archivo (Cambiar con Path)
    mostrar_menu()
    opcion_elegida = elegir_opcion()
    print("Ha elegido la altura:", opcion_elegida)
    procesar_archivo(archivo_csv, opcion_elegida)

if __name__ == "__main__":
    main()