#La palabra reservada global se usa dentro de una funcion para declarar variables,
#esta varaibles se vuelven globales y pueden ser usadas fuera de la funcion 

#ejemplo

def saludo(name):
    global message#se veulve acesible en cualquier parte del codigo

    message = f"Hola {name}"

saludo('Ana')

print(message)#accedemos desde fuera de la funcion sin ningun problema


my_list = [2,1,3]#esta lista puede ser accedida desde cualquie lugar de codigo

def listas(lista):
    print(lista)
    print(my_list)#accedemos a la lista que esta feura de la funcion sin nungu problema
    del lista[0] #afecta a mabs lista porque ocupan el mismo espacio de memoria
    print(lista)
    print(my_list)
    lista = [6,5,7]#reacigna nuevos valores solo a la lista de la funcion y toma toro espacion
    print(lista)
    print(my_list)
listas(my_list)

#NOTAL: my_list comparte sus valores con lista a un principio y es por eso que ambos pueden ser modifcados si uno sufre una modificacion 