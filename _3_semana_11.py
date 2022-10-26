class dog:
    #atributo
    species="mammal"
    #inicializador
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #instance method
    def description(self):
        return self.name+" is "+str(self.age)+" years old "
    #instance method
    def speak(self,sound):
        return self.name+" says "+sound
    
dog1=dog('Pluto',5)
dog2=dog('Milu',3)
type(dog1)
#__main__.dog
#acceder a los atributos de instancia
print("{} is {} and {} is {}".format(dog1.name,dog1.age,dog2.name,dog2.age))
#es mamifero
if dog1.species=="mammal":
    print("{0} is a {1}!!".format(dog1.name,dog1.species))
#llamar a los metodos
print(dog1.description())
print(dog1.speak("Gruff Gruff"))