import csv

def localidades_conectividad (archivo):
    with open (archivo, "r", encoding = "utf-8", newline ="") as file:
        reader = csv.reader(file)
        for elem in reader:
            cant = 0
            for i in range (4,14):
                cant = sum (1 for value in elem[4:13] if value =="SI")