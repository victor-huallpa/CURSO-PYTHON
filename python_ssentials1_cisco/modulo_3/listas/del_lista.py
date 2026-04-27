#En una lista tambien se puede eliminar los elementos que contiene esta con la sentencia 'del'
#del lista_name[index]

my_list = ['a', 1, 'hello world', 2]
print(my_list,'\nEliminamos los elementos con indice 0 y 2')

del my_list[0]#Elimanos elemento y el inidice cambia(elementos se desplazan)
del my_list[1]#Elimanos elemento y el inidice cambia
print(my_list)

#Nota: recuerda que cuando eliminas un elemento de una lista este modifica su inidce de tal manera que los demas elementos se desplazan segun corresponda