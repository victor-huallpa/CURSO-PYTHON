paso = 0 
dato = int(input('ingrese un valor entero: '))
print('\n')

# while dato != 1:
#     if dato%2 == 0:
#         dato //= 2
#         paso += 1
#         print(f"""
#         Paso {paso}:
#         {dato}\n""")
#     elif dato%2 != 0:
#         dato = (3*dato)+1
#         paso += 1
#         print(f"""
#         Paso {paso}:
#         {dato}\n""")
#     else:
#         print('algo salio mal')
# print(f'pasos total: {paso}')


while True:
    if dato%2 == 0:
        dato //= 2
        paso +=1
        print(f'paso n°{paso} resultado {dato} \n')
    elif dato%2 != 0:
        if dato == 1:
            print(f'total pasos {paso}')
            break
        elif dato!= 1:
            dato =(3*dato)+1
            paso += 1
            print(f'paso n°{paso} resuoltado {dato} \n')
            
    else:
        print('alog salio mal')
        break
    
