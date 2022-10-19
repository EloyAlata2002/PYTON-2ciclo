def suma(N):
    sumatoria=N**2
    for N in range (1,N*2,2):
        if(N%2!=0):
            print (N)
    print("El cuadrado del valor es: ",sumatoria)
  
N= int(input("Ingrese N :> "))
suma(N)
