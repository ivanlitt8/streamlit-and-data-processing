import csv

"""
Funcion tomar_top_5

se encarga de la consulta_7, debe devolver las 5 jurisdicciones con mayor porcentaje de gente en situacion de calle

args: la direccion del archivo modificado
return: ---

"""


def tomar_top_5(archivo_csv):
    with open(archivo_csv) as archivo:
        datos=csv.reader(archivo,delimiter=",")
        "se abre el archivo en modo lectura"
        next(datos)
        next(datos)
        "se adelantan dos filas ya que una es el header y la otra contiene los datos de todo el pais"
        top_5=[]
        "se crea una lista donde se guardaran las 5 jurisdicciones"
        for fila in datos:
          if(fila[13] != "0.0"):
            "si el valor de fila[13] es diferente a 0.0 se continua"
            if len(top_5) < 5 or fila[13] > top_5[-1][1]:
              "si la longitud de la lista es menor a 5 o si el ultimo valor de la lista es menor que fila[13] (es decir el porcentaje) se continua"     
              if len(top_5) == 5:
                top_5.pop()
                "si la longitud de la lista es igual a 5 la lista hace un pop si no sigue como esta"                                
              aux=(fila[0],fila[13])
              top_5.append(aux)
              top_5.sort(key=lambda x: x[1], reverse=True)
              "se agregan a la lista la jurisdiccion y el porcentaje y se hace un sort de mayor a menor de la lista top_5 tomando como referencia el segundo valor"
    for jurisdiccion in top_5:
      print(jurisdiccion)
      "se informa en pantalla las 5 jurisdicciones y los porcentajes"


"""
En "for fila in datos" se esta recorriendo todas las filas de la lista, si el porcentaje no es cero se sigue con el codigo
luego se ve si hay espacion en la lista o si el nuevo dato es mayor al ultimo, si hay espacio se agrega sin mas pero si no hay 
se hace un pop y se guarda el nuevo valor que es mayor al ultimo, luego se hace un sort para acomodar la lista y asi poder tomar 
como parametro al ultimo numero sin que genere conflicto con los demas.
"""




