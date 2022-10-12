print ("ingrese ldo1,ldo2 y ldo3")
lado1=int(input())
lado2=int(input())
lado3=int(input())
if lado1==lado2 and lado2==lado3 and lado1==lado3:
   print ("El triangulo es equilatero")
elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
    print ("El triangulo es escaleno")
else:
    print ("El triangulo es isosceles")