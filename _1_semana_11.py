class Micalculadora():
    resultado=0
    def mostrar_resultado(self):
        print(self.resultado)
    def suma(self,val1,val2):
        self.resultado=val1+val2
miobjeto=Micalculadora()
miobjeto.suma(10,20)
miobjeto.mostrar_resultado()