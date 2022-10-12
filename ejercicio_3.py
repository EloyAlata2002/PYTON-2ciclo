print("Ingrese cantidad de GB")
GB=int(input())
if GB<=4:
    pago=50
elif GB<8:
    pago=85
else:
    pago=85+(GB-8)*4,5
print("monto a pagar", pago)