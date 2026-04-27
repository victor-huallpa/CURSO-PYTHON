#cre aun algoritmo que realice los siguietne s pasos
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

sistem_list = [1,2,3,4,5]
print(sistem_list)
user_number = int(input("Ingrese un numero: "))

sistem_list[int(len(sistem_list)//2)] = user_number
print(sistem_list)

del sistem_list[-1]
print(sistem_list)
print(f"La longitud de la lista es: {len(sistem_list)}")

