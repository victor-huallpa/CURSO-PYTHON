#Crea un algoritmo que permita construir un paramide a partir de la cantidad de materiales ingreasdos por el usuario
#recuerda que, si en caso falte material el sistema debe informarlo y terminar el bucle de consctruccion
#tambien recuerda que debe indicar la cantidad de material que falta para terminar la piramide y indicar tambie nque altura tendra la piramide
import time
print("-------------------------------------------------")
print("|----- Bienvenido a construyendo piramides -----|")
print("-------------------------------------------------\n")
while True:
    print("Si desea salir digite el numero '0'\n")
    material = int(input("Por favor ingrese la cantidad de material para la piramide: "))
    print("\n")
    num = 1
    if( material == 0):
        break
    print("Contruyendo piramide...")
    while material:
        time.sleep(1)
        if material == num:
            time.sleep(1)
            print(f"Fila {num}: {'*'*num}")
            print(f"\nMaterial usado: {int(num*(num+1)/2)}")
            print(f"\nEl material ingresado es preciso para construir una piramide de {num} de alto\n")
            break
        elif material < num:
            print(f"\nMaterial usado: {int((num-1)*((num-1)+1)/2)}")
            print(f"Material restante: {material}")
            print(f"\nTe faltan {num -material} de material para completar la sigueinte fila de la piramide\ny la altura actual de la piramide es de {num-1} de alto\n")
            break
        print(f"Fila {num}: {'*'*num}")
        # print(f"Fila {num}:",end='*'*num)
        material -= num
        num+=1
    print("--------------------------------------------------------")
    

print("\n\n--------------------------------------------------------")
print("|----- Gracias por jugar a construyendo piramides -----|")
print("--------------------------------------------------------\n")