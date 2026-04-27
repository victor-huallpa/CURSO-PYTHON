#crea un algoritmo donde el usuario ingrese por consola un numero, despues este sea evaluado dentro de un bucle, y verifique si el nuemro ingresado es igual al numero alnacenado e nuna variable
#cosnidera poner mensajes si sigue en el bucle y cuando adivine el numero secreto
print("|------ Bien venido al juego de adivina el numero -------|")
num_secreto = 5
num_user = int(input("ingrese un numero: "))
while num_secreto != num_user:
    if num_user < num_secreto:
        print(f"El numero ingresado {num_user} es menor al numero secreto.")
    elif num_user > num_secreto:
        print(f"El numero ingresado {num_user} es mayor al numero secreto.")
    else:
        print(f"El dato ingresado {num_user} no corresponde a un numero valido.")
    print("JAJAJA, Estas atrapado en este bucle mi querido muggle.\n")
    num_user = int(input("ingrese nuevamente el un numero: "))

print(f"Felicidades el numero ingresado {num_user} es correcto.\nSaliste del bucle.")