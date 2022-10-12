print ("Ingrese zona (1-2):> ")
tipo_zona=int (input())
print ("Ingrese consumo:> ")
consumo=int(input())
if tipo_zona==1:
    monto=50
    if consumo>=100:
     primeros100=0.75
    else:
      extra=(consumo-100)*0.9
else:
   if tipo_zona==2:
    monto=25
    if consumo>=100:
        primeros100=0.30
    else:
        extra=(consumo-100)*0.7
     
print("El monto a pagar es:>",primeros100+extra)



