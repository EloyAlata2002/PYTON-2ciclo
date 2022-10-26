class Triangulo:
    __base=0 #atributo privado
    __altura=0 #atributo privado
    #def __init__(self,base,altura):
        #self.__base=base
        #self.__altura=altura
    def area(self):
        return self.__base*self.__altura/2
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def set_base(self,base):
        self.__base=base
    def set_altura(self,altura):
        self.__altura=altura
    def perimetro(self):
        hipotenusa=(self.__base**2+self.__altura**2)**0.5
        return self.__base+self.__altura+hipotenusa

base=float(input("Ingrese la base:> "))
altura=float(input("Ingrese la altura:> "))
objeto=Triangulo()
objeto.set_altura(altura)
objeto.set_base(base)
print("Area:> ",objeto.area())
print("Perimetro:> ",objeto.perimetro())
