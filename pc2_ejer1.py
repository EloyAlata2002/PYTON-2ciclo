def tippo_trian(val1,val2, val3):
    if val1==90 or val2==90 or val3==90:
        print("Es un triangulo rectangulo")
    elif val1>90 or val2>90 or val3>90:
        print("Es un triangulo obtusangulo")
    else:
        print("Es un triangulo acutangulo")

n1=int(input("Ingrese angulo 1:> "))
n2=int(input("Ingrese angulo 2:> "))
n3=int(input("Ingrese angulo 3:> "))
tippo_trian(n1,n2,n3)
