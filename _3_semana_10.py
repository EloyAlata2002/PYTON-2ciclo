n=0
while n<1 or n>50:
 numeroalumnos=int(input("Ingrese el numero de alumnos:> "))
contmenos40=0
cont40y50=0
cont50y60=0
contmas60=0
for i in range(n):
    peso=0
    while peso <1:
        peso=int (input("Ingrese peso:> "))
    if peso<40:
        contmenos40=contmenos40+1
    elif peso<=50:
        cont40y50=cont40y50+1
    elif peso<60:
        cont50y60=cont50y60+1
    else:
        contmas60=contmas60+1
print("menos de 40:> ",ccontmenos40)
print("entre de 40 y 50:> ",cont40y50)
print("entre de 50 y 60:> ",cont50y60)
print("60 o mas:> ",contmas60)
