numbers = [111, 7, 2, 1]
print(len(numbers), " elementos en tu,lista")
print(numbers)

###
value = int(input('ingrese evalor que desea agregar al final de la lista: '))
numbers.append(value)

print(len(numbers), " elementos en tu,lista")
print(numbers)

###
print(f'tiene {len(numbers)} espacios')
value2 = int(input('ingrese el valor que esea ingresar: '))
position = int(input('ingrese la posicion en la que quiere colocar el numero o valor ingresado: '))

numbers.insert(position, value2)
print(len(numbers), " elementos en tu,lista")
print(numbers)

#
