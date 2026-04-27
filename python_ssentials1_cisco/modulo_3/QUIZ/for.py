#crea un algoritmo que cuente del 0 al 10 y meustre solo los numeor impares
#usar bucle for

for i in range(0, 11):
    if i % 2 != 0:
        print(i)
    else:
        continue

for i in range(1, 11, 2):
    print(i)

for i in range(0, 11, 2):
    if i < 10:
        print(i+1)
    else:
        break