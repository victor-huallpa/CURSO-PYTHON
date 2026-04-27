#Crea un algoritmo que te permita calcular la hipotesis de collatz, a partir de un numero ingresado por el usuario
#considera usar el bucle while y evaluar la varaible del usuario

#Hipotesis de Collatz si:
#Es para todo numero natural n mayor o igual que 1
#Si n es par, a n se divide entre 2
#Si n es impar, a n se multiplica por 3 y se le suma 1

#recuerda calcular la cantidad de iteraciones realizadas para llegar a 1
print("--------------------------------------------------------------")
print("|----- Bienvenido a comprobando la hipotesis de Collatz -----|")
print("--------------------------------------------------------------\n")


while True:
    print("Si desea salir digite el numero '0'\n")
    number_user = int(input("Por favor ingrese un numero: "))
    iteration = 1

    if number_user == 0:
        break
    print("\n\nCalculando hipotesis de Collatz...\n")
    while number_user > 1:

        if number_user % 2 == 0:
            number_user /= 2
        else:
            number_user = (number_user * 3) + 1
        iteration += 1
        
        print(int(number_user))

    print(f"\nPasos realizados: {iteration-1}")
    print("\n--------------------------------------------------\n")

print("\n\n--------------------------------------------------")
print("|----- Gracias usar el algoritmo de Collatz -----|")
print("--------------------------------------------------\n")