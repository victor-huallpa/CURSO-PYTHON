#crea un algoritmo que realice las primera potencias de un numero ingresado por consola
#considera que estas primeras potencias a calcular las puede ingresar el usuario

num_potenica = int(input("Ingrese el numero de potencias a calcular: "))

num_calcular = int(input("Ingrese el numero a elevar a la portencia: "))

for i in range(num_potenica):
    print(f"El numero {num_calcular} elevado a la potencia {i} es {num_calcular**i}")