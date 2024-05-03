import csv

"""
Funcion tomar_max_brecha

se encarga de la consulta_8, tiene que informar la jurisdiccion con mayor brecha entre hombres y mujeres

args: la direccion del archivo modificado
return: ---

"""

def tomar_max_brecha(archivo_csv):
    with open(archivo_csv,encoding="utf-8") as archivo:
        datos=csv.reader(archivo,delimiter=",")
        "se abre el archivo en modo lectura"
        next(datos)
        next(datos)
        "se adelantan dos filas ya que una es el header y la otra contiene los datos de todo el pais"
        brecha=("",0)
        comp=0
        "se crea una tupla con la jurisdiccion y el numero de personas y una variable para comparar valores"
        for fila in datos:
          "se recorren las filas de la lista datos y si fila[5] y fila[9] son diferentes a 0, continua"
          if ((fila[5] != "0") and (fila[9] != "0")):
            aux = abs(( ( int(fila[5]) * 100 ) / int(fila[1]) ) - ( (int(fila[9]) * 100) / int(fila[1]) ))
            "se guarda en la variable aux la diferencia entre el porcentaje de hombres en el total de poblacion y el porcentaje de mujeres, ese numero representa la brecha"
            if (aux>comp):
              "se compara con el valor ya guardado y si es mayor se actualiza la variables comp con el porcentaje y en la variable brecha se actualiza la jurisdiccion y la cantidad de personas"
              comp=aux
              brecha=(fila[0],abs(int(fila[5])-int(fila[9])))
    print (brecha)
    "se imprime la variable brecha"



