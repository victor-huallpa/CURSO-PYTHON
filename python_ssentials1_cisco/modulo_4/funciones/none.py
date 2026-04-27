#La palabra reservada 'None', teinde a utilizarce para no asignar ningun valor a una variable
#o para comparar el valor interno de una variable

#Ejemplo:

variable = None#asignamos None a la varaible para decir que esta vacia


if variable is None:#comparamos la variable para verificar si esta vacia oes None
    print("No contiene nada tu variable")

#NOTA: en caso de las funciones si estas no contiene algun elemento que retornen se cosnidera por defauilt que deveulven None

def saludo():
    print("hola")
    #Al no tener algo que retornar por default retornara None
saludar = saludo()#gurada None

if saludar is None :#vavalida que es none el contenido de la variable saludar
    print("Tu funcion no retorna nada por ende tiene NONE")

