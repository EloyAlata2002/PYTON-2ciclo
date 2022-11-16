def funcion(lista,n):
    #numero mayor
    mayor=0
    for x in lista:
        if x>mayor:
            mayor=x
    print("El mayor es:> ", mayor)
    #numero menor
    for y in lista:
        if y<mayor:
            mayor=y
    print("El menor es:> ", mayor)
    #cantidad numero positivo
    cantiposi=0
    for x in lista:
        if x>0:
            cantiposi+=1
    print("La cantidad de numeros positivos es:> ",cantiposi)
    #cantidad numero negativo
    cantinega=0
    for x in lista:
        if x<0:
            cantinega+=1
    print("La cantidad de numeros negativos es:> ",cantinega)
    #promedio de lista
    sum=0
    for x in lista:
        sum+=x
    promedio=sum/n
    print("El promedio es:> ", promedio)
    
lista=[]
n=-1
while n<0:
    n=int(input("Ingresa N:> "))
for x in range(1,n+1):
    x=int(input("Ingrese un numero:> "))
    lista.append(x)

funcion(lista,n)




