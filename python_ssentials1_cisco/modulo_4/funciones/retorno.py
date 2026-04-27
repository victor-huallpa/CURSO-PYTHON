#Las fuciones tienen algo que las puede detener en cualquier punto y devolver siertas cosas ya sea ntextos, varaibles, listas o lo que desees
#pero pueden devolver, y esto lo hace ngracias a la palabra reservada return\

#Ejemplo

def saludo(nombre):
    message = f"Bien venido {nombre}"#creamos o asignamos el mensaje a la variable de la funcion
    return message#retornamos el mensaje

user_name = input("Por favor ingrese su nombre: ")

retorno = saludo(user_name)#guradamos el resultado q2ue retorna la funcion en una variable
print(retorno)#imprimimos el resultado

