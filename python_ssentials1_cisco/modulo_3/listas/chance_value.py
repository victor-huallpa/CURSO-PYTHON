#Python ofrese una manera de cambiar datos en variables
val1 = 4
val2 = 5


print(val1, val2)#imprime valores originales de las variables
val1, val2 = val2, val1#cmabiamos el valor de las variables una con otra
print(val1, val2)#imprime modificacion

#esta forma de intentar cambiar el valor de la variables es incosnistente no comple con su funcion,
#se recquerirra una varaible axiliar para realizar dicha tarea
val2 = val1
val1 = val2
print(val1, val2)#imprime modificacion

#En listas tambien es util la manera que python ofrece para cambiar variables, ya que podemos ordenar esta lista a nuestro gusto
my_list = [3, 4, 1, 5, 2]
print(my_list)#antes de ordenar la lista
my_list[0], my_list[1], my_list[2], my_list[3], my_list[4] = my_list[2], my_list[4], my_list[0], my_list[1], my_list[3]
print(my_list)#despues de ordenar la lista


length = len(my_list)
for i in range(length//2):
    my_list[i], my_list[length - i -1] = my_list[length - i -1], my_list[i]
print(my_list)
