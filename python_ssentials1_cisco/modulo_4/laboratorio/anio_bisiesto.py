#Crea un algoritmo que calculo a partir de la entrada de anio del usuario, si el anio es bisiesto o no 
#recierda usar fucniones

def calcular(anio):
    result = []

    for i in anio:

        if i%4 == 0 and i%100 != 0:
            result.append(True)
        
        elif i%100 == 0 and i%400 == 0 and i%4 ==0:
            result.append(True)
        
        else:
            result.append(False)

    return result


def datos(n):
    anios = []
    for i in range(0,n):
        anio_dato = int(input(f"Ingrese el anio {i+1}: "))
        anios.append(anio_dato)
    return anios

print('------------------------------------------------------')
print('|--------- Bien venido a calculando el anio ---------|')
print('------------------------------------------------------\n')

while True:
    print('Si desea salir digite "0"')
    num_anios = int(input("Por favor ingrese la cantidad de anios que ingresara: "))

    if num_anios == 0:
        break

    list_anios = datos(num_anios)
    validate_anios = calcular(list_anios)
    for i in range(len(list_anios)):
        yr = list_anios[i]
        v_yr = validate_anios[i]
        print(f"{yr} -> {v_yr}")
    

print('\n-------------------------------------------------------------')
print('|--------- Gracias por juagar a calculando el anio ---------|')
print('-------------------------------------------------------------\n')