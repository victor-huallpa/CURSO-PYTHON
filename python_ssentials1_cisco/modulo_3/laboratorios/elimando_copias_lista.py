#crea un algoritmo que elimine los elementos repetidos dentro de una lista

lista = [1,2,33,4,4,5,22,33,87,4]
new_list = []

for i in range(len(lista)):
    if lista[i] not in  new_list:
        new_list.append(lista[i])


print(new_list)


