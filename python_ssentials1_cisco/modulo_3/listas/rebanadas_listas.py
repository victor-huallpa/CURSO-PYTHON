#En python asignar una lista otra y lugo modificar la primera lista implica que la segunda lista tambie nse modifique el  conteido
#ya que esta tomando el lugar de almacenamiento de la primera lista y no una copia almacenada en otro

lista = [1, 2]
lista2 = lista#asignamos a esta lista la lista 1
print(lista2)

lista[1] = 4 #modifcamos la el indice 1 de la lista 1 

print(lista2)#se meustra la modificacion de la lista 1

#como ya mencione est ose debe aque en realidad no estamos realizando una copia de la lista sino que tome el estacio de lista 1, o simples palabras casmbiar de nombre lista2 a lista1
#claro no se observa porque como digo es el espacio tomado

#para realizar una copia de una lista se tiene que realizar rebanas de lista
lista1 = [1, 2]
lista3 = lista1[0:2]#lista[inicio:fin] recuerda que el fin no significa que tome ese indici si no fin - 1
#tambien si restas fin - inicio sabras la canitda de elementos que estas clonando
#tambien puedes realizar con numero negativos como en indexaion
lista4 = lista1[-1:2]
print(lista3)
lista1[1] = 4 #modifcamos la el indice 1 de la lista 1 
print(lista3) #no cambia su contenido 
print(lista4) #no cambia su contenido 

#metodo del y rebanadas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#in y not in
#son palabras que identifican si esta dentro o no de una lista una varaible evaluada
#devuelve valores boleanos True or False
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


