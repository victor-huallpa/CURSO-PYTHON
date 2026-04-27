# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

# Tu tarea es:

# escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
# escribir una línea de código que elimine el último elemento de la lista (Paso 2)
# escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
hat_list = [1, 2, 3, 4, 5] 
hat_list[2]= int (input('reemplace el elemento central de su lista\n ingrese otro numero:'))
del hat_list[4]
print(f"se elimino un elemeto de tu lista ahora solo cuentas con {len(hat_list)} elementso\nlos cuales son {hat_list} ")
print(f"la longitud de tu lista es {len(hat_list)}")