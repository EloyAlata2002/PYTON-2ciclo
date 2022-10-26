import csv
with open("Libro1.csv") as csv_archivo:
    csv_reader=csv.reader(csv_archivo,delimiter=";")
    cuentalineas=0
    for fila in csv_reader:
        if cuentalineas==0:
            print("Los nombres de las columnas son:> ",fila)
            cuentalineas+=1
        else:
            print("\t"+fila[0]+" trabajo en area de "+fila[1]+ " , y naci en "+fila[2])
            cuentalineas+=1
    print("Lineas procesadas"+str(cuentalineas))