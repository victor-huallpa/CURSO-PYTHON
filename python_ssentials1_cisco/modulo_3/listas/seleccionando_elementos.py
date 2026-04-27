#Crea un algoritmo donde se pueda seleccionar cualquier elemento de una lista ya declarada con mas de 5 elementos
#Si deseas puedes pedir al usuario estos elementos y despues almacenarlos en una lista
#considera si le piedes al usuario ingresar los elementos que tendran la lista, tambien que le pida que cantidad de datos a almacenar
#Considera que el algoritmo tambien tiene que darle la opcion de modificar, eliminar o seguir agregando los elementos de la lista en caso lo queira el usuario

memory_list = []
print('-------------------------------------------------------------------------')
print('|------------ Bienvenido a este numdo de jugando con listas ------------|')
print('-------------------------------------------------------------------------\n')

while True:
    print(f"Elementos actuales en la lista : {len(memory_list)}")
    if len(memory_list) == 0:
        print('\nLe recomiendo agregar elementos a la lista')
    print('Ingrese el numero cero "0" para salir ')

    modify = input("Que accion desea realizar con los elementos de la lista?\n1 modificar\n2 eliminar\n3 agregar\n...").lower()
    print(f"Los elementos de su lista son {len(memory_list)}")
    for i in range(len(memory_list)):
        print(f"Elemento {i+1}: {memory_list[i]}")
    if modify == "modificar" or modify == '1':

        elemetn_to_modify = input("Que elemento de la lista desea modificar?\nIngrese el numero o nombre del elemento: ")

        if (elemetn_to_modify in memory_list) or (memory_list[int(elemetn_to_modify)-1] in memory_list):
            for i in range(len(memory_list)):
                if memory_list[i] == elemetn_to_modify or i == int(elemetn_to_modify)-1:
                    elemetn_to_modify = i
                continue
            new_element = input(f"Ingrese la modificacion del elemento '{memory_list[elemetn_to_modify]}': ")
            memory_list[elemetn_to_modify] = new_element
            print(memory_list)
    elif modify == 'eliminar' or modify == '2':
        elemetn_to_modify = input("Que elemento de la lista desea eliminar?\nIngrese el numero o nombre del elemento: ")
        if elemetn_to_modify in memory_list or memory_list[int(elemetn_to_modify)-1] in memory_list:
            del memory_list[int(elemetn_to_modify)-1]
        print(memory_list)
    elif modify == 'agregar' or modify == '3':
        num_elements = int(input("Cuantos elementos desea ingresar: "))
        print('')
        for i in range(num_elements):
            element = input(f"por favor ingrese el elemento {i+1}: ")

            if element not in memory_list:
                memory_list.append(element)
            elif element in memory_list:
                while True:

                    res = input(f"El elemento {element} ya existe dentro de la lista\ndesea agregarlo (si/no): ").lower()
                    if res == 'si':
                        memory_list.append(element)
                        break
                    elif res == 'no':
                        element = input(f"por favor ingrese nuevamente el elemento {i+1}: ")
                        break
                    else :
                        print(f"No existe la opcion {res}, vuevla a introducir la decicion")
                memory_list.append(element)
        print(memory_list)
                
    elif modify == '0':
        print('asta la proxima ')
        break


