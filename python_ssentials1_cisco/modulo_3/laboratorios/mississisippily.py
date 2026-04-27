#mississippi es el numbre de un estado y rio de EE.UU, es usa para realizar una cuenta en tiempo de segundos
#importa time y usa sleep para poder controlar el tiempo en segundo dentro del bucle a crear

#crea un algoritmo que cuente asta 5 mississippis y nuestre la cuenta en pantalla
#Si deseas puedes pedir al suario cuantos mississippies desea contar.

import time

tiempo = int(input("Ingrese la cantidad de 'MISSISSIPPIES' a contar: "))

for i in range(tiempo):
    if i == 0:
        print(f"{i+1} MISSISSIPPI")
    else :
        print(f"{i+1} MISSISSIPPIES")
    time.sleep(1)
print(f"\nListos o no, alli voy!")