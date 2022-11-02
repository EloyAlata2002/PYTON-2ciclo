#import csv
#with open ('POOejemplo.csv', mode='r') as csv_file:
#    csv_reader=csv.DictReader(csv_file,delimiter=';')
#    line_count=0
#    for row in csv_reader:
#        if line_count==0:
#            print("Nombres de las columnas son:", row.keys())
#            line_count+=1
#        print(row["nombre"],'trabaja en ', row["Area"], 'y nacio en', row["MesNaci"])
#        line_count+=1
#    print("Filas procesadas. ", line_count)

#write csv
#opcion 1
#import csv 
#with open('Libro3.csv',mode='w')as archivo:
#    writer= csv.writer(archivo,delimiter=";", quotechar='*',quoting=csv.QUOTE_MINIMAL)
#    writer.writerow(['Nombre','Area','Mes'])
#    writer.writerow(['John Smith','accounting','November'])
#    writer.writerow(['Erica Meyers','IT','March'])
    
#opcion 2 diccionario
#import csv
#with open('Libro4.csv',mode='w')as archivo:
#    campos=['Nombre','Area','Mes']
#    writer= csv.DictWriter(archivo,delimiter=";",fieldnames=campos)
#    writer.writeheader()
#    writer.writerow({'Nombre': 'John Smith', 'Area':'Accounting','Mes':'November'})
#    writer.writerow({'Nombre': 'Erica Meyers', 'Area':'IT','Mes':'November'})
    
#csv con pandas
#pip install pandas
#import pandas
#df=pandas.read_csv('hrdata.csv',dilimiter=';')
#print(df)
#print(type(df['Hire date'][0]))
##cambio de tipo de dato
#df=pandas.read_csv('hrdata.csv', delimiter=';',index_col='Name', parse_dates=['Hire date'])
#print(df)
#print(type(df['Hire date'][0]))
##cambio de columnas
#df=pandas.read_csv('hrdata.csv',
#                   index_col='Employee',
#                   parse_dates=['Hired'],
#                   header=0,
#                   names=['Employee','Hired','Salary','Sick Days'])
#print(df)
##write csv with pandas
#df=pandas.read_csv('hrdata.csv',
#                   index_col='Employee',
#                   parse_dates=['Hired'],
#                   header=0,
#                   names=['Employee','Hired','Salary','Sick Days'])
#df.to_csv('hrdata_modified.csv')

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel("ordenadas")
plt.xlabel("abcisas")
plt.show()
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel("some numbers")
plt.show()
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 
https://www.w3schools.com/python/python_getstarted.asp