#crea un algoritmo que recete el numero almacenado en una variable,
#considera que cada cero del numero debe ser reemplazado por una x
user_numb = str(input("Ingrese un numero: "))
for digit in user_numb:
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
print("")
