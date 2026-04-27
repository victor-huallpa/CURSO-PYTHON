#crea un algoritmo que cuente del 0 al 10 y meustre solo los numeor impares
#usar bucle while

x = 1
while x < 11:
    print(x)
    x += 2
x = 1
while x <= 10:
    if x%2 != 0:
        print(x)
    x += 1