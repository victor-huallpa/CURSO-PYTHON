#crea un algoritmo que pueda validar la creacion de un triangulo a partir de la longitud de sus lados
#considere que un triangulo solo se puede construir si dos de sus lados sumados son mayor al lado que no se
#sumo.
def validar_triangulo(lado1, lado2, lado3):

    suma1_lados = lado1 + lado2
    suma2_lados = lado3 + lado2
    suma3_lados = lado1 + lado3
    #verificamos si se puede construir un triangulo
    if((suma1_lados > lado3) and (suma2_lados > lado1) and (suma3_lados > lado2)):
        msj = 'los lados que tienes pensado para tu triangulo si son validos y formaran un triangulo'
    elif((suma1_lados == lado3) or (suma2_lados == lado1) or (suma3_lados == lado2)):
        if(suma1_lados == lado3):
            msj = f'La suma de dos lados no puede ser igual al lado no sumado\nLado 1: {lado1}\nLado 2: {lado2}\nsuma: {suma1_lados} = al lado 3: {lado3}'
        elif(suma2_lados == lado1):
            msj = f'La suma de dos lados no puede ser igual al lado no sumado\nLado 2: {lado3}\nLado 3: {lado3}\nsuma: {suma2_lados} = al lado 1: {lado1}'
        elif(suma3_lados == lado2):
            msj = f'La suma de dos lados no puede ser igual al lado no sumado\nLado 1: {lado1}\nLado 3: {lado3}\nsuma: {suma3_lados} = al lado 2: {lado2}'
    if((suma1_lados < lado3) or (suma2_lados < lado1) or (suma3_lados < lado2)):
        if(suma1_lados < lado3):
            msj = f'La suma de dos lados no puede ser menor al lado no sumado\nLado 1: {lado1}\nLado 2: {lado2}\nsuma: {suma1_lados} es menor al lado 3: {lado3}'
        elif(suma2_lados < lado1):
            msj = f'La suma de dos lados no puede ser menor al lado no sumado\nLado 2: {lado3}\nLado 3: {lado3}\nsuma: {suma2_lados} es menor al lado 1: {lado1}'
        elif(suma3_lados < lado2):
            msj = f'La suma de dos lados no puede ser menor al lado no sumado\nLado 1: {lado1}\nLado 3: {lado3}\nsuma: {suma3_lados} es menor al lado 2: {lado2}'
    return msj
#datos
print('Ten en cuenta que si quieres armar un traingulo, la suma de\ndos lados deben ser mayores al lado no sumado\n')
while(True):
    print('\nIngresa el numero cero 0 en el primer lado para salir\n')
    try:
        lado1 = float(input('Ingrese la longitud del primer lado en cm : '))
        if(lado1 == 0):
            print('Gacias por usar este algoritmo para ver si tu triangulo a crear es valido\nVuelve pronto')
            break 
        lado2 = float(input('Ingrese la longitud del segundo lado en cm: '))
        lado3 = float(input('Ingrese la longitud del tercer lado en cm : '))
        #imprimir resultado
        print(f'\nEl resultado es: \n{validar_triangulo(lado1, lado2, lado3)}')
    except ValueError:
        print('\nIngresa numeros no otros caracteres o campos vacios\n')