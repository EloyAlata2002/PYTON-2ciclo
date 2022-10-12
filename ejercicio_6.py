print("Area a la que pertenece ")
area=str(input())
print("Ingrese horas que trabaja ")
horas=int(input())
if area=='Logistica' or area=='Recursos humanos':
    if(horas<=48):
        pago=500
    else:
        pago=500+(horas-48)*10
else :
    if area=='Sistemas':
     if(horas<=48):
        pago=750
     else:
        pago=750+(horas-48)*10
    else:
     if(horas<=48):
        pago=600
     else:
        pago=600+(horas-48)*10
print("Su sueldo neto es: ",pago)

    
