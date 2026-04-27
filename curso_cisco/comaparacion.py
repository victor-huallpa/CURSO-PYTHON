while True:
    print('introdusca 00 para cerrar el bucle')
    num1 = int(input('ingrese un numero: '))
    num2 = int(input('ingrese otro numero: '))

    if num1 != num2:
        if num1 < num2:
            print (num1, ' es menor que ', num2)
        elif num1 > num2:
            print (num1 , ' es mayor que ', num2)
        else:
            print('algo salio mal')
    elif num1 == num2:
        print(num1 , ' es igual que ' , num2)
    
    elif num1 == 00:
        print('isted cerro el bucle')
        break

    else:
        print('algo malio sal')