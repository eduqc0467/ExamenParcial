contador=float(0);
dividendo=int(input("Ingrese el dividendo:"));
divisor=int(input("Ingrese Divisor:"));
dividendo=dividendo-divisor;
while(dividendo>=0):
    contador=contador+1;
    dividendo=dividendo-divisor;
    print("El resultado de la division es:"+str(contador));
 