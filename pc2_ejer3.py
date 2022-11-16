class Persona():
    __nombre=""
    __horas_de_trabajo=0.0
    __tarifa_pagada__hora=0.0
    __sueldo=0
    def __init__(self,nombre,horas,tarifa):
        self.__nombre=nombre
        self.__horas_de_trabajo=horas
        self.__tarifa_pagada__hora=tarifa
    def calcular_sueldo(self):
        self.__sueldo=self.__horas_de_trabajo*self.__tarifa_pagada__hora
        print("El sueldo que le corresponde es de:> ",self.__sueldo )
    def get_sueldo(self):
        return self.__sueldo
    def get_nombre(self):
        return self.__nombre
    def get_hora(self):
        return self.get_hora
                

class Lista():
    lista=[]
    def agregar(self, obj):
        self.lista.append(obj)
    def get_lista(self):
        return self.lista
    
obj=Lista()
nombre=""
horas=0
tarifa=0
n=-1
while n<0:
    n=int(input("Ingrese cantidad de empleados:> "))

for x in range(n):
    while nombre =="":
      nombre=input("Ingrese su nombre:> ")
      horas=int(input("Ingrese las horas trabajadas:> "))
      tarifa=float(input("Ingrese la tarifa por hora trabajada:> "))
    empleado=Persona(nombre,horas,tarifa)
    empleado.calcular_sueldo()
    obj.agregar(empleado)

#for x in obj.get_lista():
#    print("Los empleados que ganan mas de 1000 son:> ")
#    if empleado.get_sueldo()>1000:
#        print(x)
#
#for x in obj.get_lista():
#    print("Los empleados que trabajan mas de 48 horas son:> ")
#    if empleado.get_hora()>48: 
#        print(x)
   





          


