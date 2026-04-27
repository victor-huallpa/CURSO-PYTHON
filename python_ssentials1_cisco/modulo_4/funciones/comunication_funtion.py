#Funciones Paramtrizadas: son la manera como se manejan los argumentos pasandos atravez de la funcion
#que despues de argumentos pasan a llamarce parametros de la funcion

def message(number): #al argumento pasado lo nombra como parametro number, esto solo cumple solo dentro de la funcion fuera no existe
    print("Ingresa un número:", number)#imprime mensaje mas parametro
 
number = 1234#variable
message(1)
print(number)#imprime variable


#parametros posicionales: consiste en el orden de los parametros asignados es igual a al oreden de los argumentos pasados
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


#paso de argumentos de palabra clave: es la forma que se pasa ragumentos por palabra clave y no posicionamiento
def introduction(first_name, last_name):#establece dos parametros a pasarce a la funcion
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")#se le otorga un valor al argumento por su nombre
introduction(last_name = "Skywalker", first_name = "Luke")#se le otorga un valor al argumento por su nombre

#convinando argumentos por clave y argumentos posicionales

def suma (a, b ,c):
    print(f"la suma de {a} + {b} + {c} es : {a+b+c} ")
a = 5
suma(a, b=2, c=7)
suma(4,c=9,b=2)
#nota una ves que empizas a pasar argumentos por clavetienes que psar todo por clave, por ende si deseas pasar argumentos posicionales teiens que hacer al principio


#argumetnos predifinidos o parametrso predifinidos con un valor por default

def saludo(hello="hello world"): #definimos el valor por default del parametro en caso no se le pase algun argumento
    print(hello)

saludo()#no le pasamos un argumento
saludo("Buenas noches")#le pasamos un argumento