#desarrola un algoritmo que realice calculos matematicos mediante en la entrada de dayos por consola 
#considera usar funciones, condicionales bucles

import time

def menu():
    bucle = True

    while bucle:
    
        print('|------ Bien venido a la calculeitor Basic -------|')
        oper = input('Que operacion desea realizar:\n1. suma\n2. resta\n3. mulitplicacion\n4. dividir\n5. salir\nIngrese operacion: ')
        oper = oper.lower()

        if(oper == "51" or oper == 'salir'):
            print("Gracias por usar nuestro calculeitor basic!")
            break
        
        datos = ingresar_datos()
        resul = validar_operacion(oper, datos)
        imprimir_resultado(resul)

    return



def ingresar_datos():
    
    datos = []
    cant = int(input(f"ingresa la cantidad de datos a operar: "))
    n = 1
    while cant > 0:
        dato = float(input(f"ingrese el dato {n}: "))
        datos.append(dato)
        cant -= 1
        n+=1
    return datos

def validar_operacion(oper, datos):
    if(oper == 'suma' or oper == '1'):
        oper = 'suma'
        resul = suma(datos)
    elif(oper == 'resta' or oper == '2'):
        oper = 'resta'
        resul = resta(datos)

    elif(oper == 'multiplicacion' or oper == '3'):
        oper = 'multiplicacion'
        resul = multiplicacion(datos)

    elif(oper == 'divicion' or oper == '4'):
        oper = 'divicion'
        resul = divicion(datos)

    else:
        print('El operador ingresado no es valido\n Vuelva a seleccionar la operacion')
        menu()
    final = [oper, resul]
    return final
def imprimir_resultado( operacion):
    if(operacion[0] == 'divicion' or operacion[0] == 'suma' or operacion[0]== 'multiplicacion' or operacion[0] == 'resta'):
        print(f"el resultado de la {operacion[0]} es: {operacion[1]}\n\n")
        print('presiona "enter" o espre durante 5 segundos para volver al menu')
        time.sleep(5)

def suma (dato):
    n = len(dato)
    sf = 0
    for i in range(n):
        sf += dato[i]
    return sf
def resta (dato):

    n = len(dato)
    sf = 0
    for i in range(n):
        sf -= dato[i]
    return sf

def multiplicacion (dato):
    n = len(dato)
    sf = dato[0]
    for i in range(n):
        if i+1 < len(dato)  :
            sf *= dato[i+1]
        else:
            break
    return sf

def divicion (dato):
    n = len(dato)
    sf = dato[0]
    for i in range(n):
        if(i+1 < len(dato)):
            sf /= dato[i+1]
        else:
            break
    return sf

menu()








