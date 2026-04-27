#El bucle for se ejecuta mientras la condicion sea true, esta clase de bulce se suele usar para iterar elementos de una coleccion de datos
#tambien se suele usar para ser presisos en contar el nuemr ode iteraciones del bucle

#FOR tiene una variable de control , esta se e ncarga de cada iteracion del bucle

for i in range(5):#in representa la introducciion de un rango, y el range es una funcion que se utiliza para crear un rango, cosnidera que  empiza de cero en caso de ingresar un muero entero positivo
    #ya que es paresico a una lista indexada
    print(f"estas dentro del bucle {i}")
print("Saliste del bucle")
print("\n\n")

for i in range(4,12):#En range se introduce dos parametros 4 y 12 esto significa que empezra en 4 y terminara en 11, recuerda que esta funcion range no solo puede resivir 1 o 2 parametros
    print(f"estas dentro del bucle {i}")
print("Saliste del bucle")
print("\n\n")

for i in range(4,12,2):#En range se introduce dos parametros 4 y 12 esto significa que empezra en 4 y terminara en 11, recuerda que esta funcion range no solo puede resivir 1 o 2 parametros
                        #tambien puede resivir 3 parametros range(inicio,final,incremento)
    print(f"La variable i tiene el valor: {i}")

print("\n\n")
for i in range(4,12,2):#funcion range resive tres parametros inicio, final y por ultimo el incremento de la varaible i
    print(f"El valor de la variable i es: {i}")
print("\n\n")

for i in range(1,1):
    print(f"El valor de la variable i es: {i}" )

print("\n\n")

for i in range(5,1):
    print("El valor de la variable i es: ", i)
#NOTA

"""
Recuerda que la funcion range teine que ser en forma acendente caso contrario no impirme nada
"""