#En condicionales solemos usar la sentencia else cuand ouna codnicion no se cumple,
#en while tambien podemos usar esta sentencia apra cuando no se entra dentro del bucle, es una forma directa de realizar condiciones

count = int(input("Por favor ingrese un numero: "))
num_ite = 1
while count < 5:
    print(f"Estas dentro del bucle numero {num_ite}")
    num_ite += 1
    count += 1

else:#Se ejecuta cuando la condicion del bucle while sea falsa
    print(f"No entraste en el bucle")