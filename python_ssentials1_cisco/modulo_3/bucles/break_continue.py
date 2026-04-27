#Al usar bucles existen algunas formas de detener estas instrucciones o saltarlas
#en esta caso tenemos 'BREAK y CONTINUE'

for i in range(5):
    if i == 3:
        print(f"El valor de la variable i es: {i}\n por ende se detiene el bucle")
        break#detiene completamente el bucle
    print(f"{i}")
print(f"Gracias por participar en el bucle\n")

for i in range(5):
    if i == 3:
        print(f"Te saltas este termino del bucle {i}")
        continue#el bucle se salta y procede con la siguiente iteracion en caso exista
    print(f"estas en el {i}")
print(f"Gracias por participar en el bucle\n")
