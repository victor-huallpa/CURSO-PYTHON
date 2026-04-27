numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers)  # Imprimiendo contenido de la lista anterior.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.


del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

