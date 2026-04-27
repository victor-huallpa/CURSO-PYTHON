#crea un algoritmo donde el usuario ingrese una palabra y el sistema elimine las vocales de esta palabra
#considera que la palabra ingresada debe convertirse a mayuscula
#considera usar la sentencia continue y el bucle for
#considera que cada alfaveto debe ser impreso en una line diferente
print("|----- Bien venido al deverador de vocales -----|")
while True:

    word_user = input("Ingrese una palabra o escriba '0' para salir: ").upper()

    if word_user == "0":
        break

    for i in range(len(word_user)):
        if word_user[i] == 'A' or word_user[i] == "E" or word_user[i] == "I" or word_user[i] == "O" or word_user[i] == "u":
            continue
        else:
            print(word_user[i])
print("\n\n---------------------------------------------------------------")
print("|--------- Gracias por jugar al devorador de vocales ---------|")
print("---------------------------------------------------------------")
