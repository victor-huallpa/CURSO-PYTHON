#Al igaul que en el bucle while, en for tambien se puede inplementar la condicional else
#y tiene la misma funcion que en while.

#La sentencia else se ejecuanta cuando la condicion de la funcion for sea falsa
numer_user = int(input("Por favor ingrese un numero: "))
for i in range(numer_user):
    print(f"Estas dentro del contador {i}")
else:#Se ejecuta cuando la condicion del bucle for sea falsa
    print("Esta fuera del contador ", i)

