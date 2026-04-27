#Una funcion tambien puede resivir una lista como argumento dentro de su parametros

#Ejemplos

def saludar(nombres):#resive como parametro una lista
    for i in nombres:
        print(f"Bien venido {i}")
    
users_names = ['Alexa', 'Roberto', 'Sayi']

saludar(users_names)#Se le esta pasando como argumento una lista definida antes


def suma_elem(elements):
    sum = 0

    for i in elements:#como saven tiene que iterar una lista no una variable de valor entero
        sum += i
    
    return sum

def gen_list(my_list):
    lista = []#lista vacia
    n = 0
    for i in my_list:
        n += i 
        lista.append(n)#agregamos elementos a nuestra lista
    return lista#retornamos la lista de la funcion

lista = gen_list([12,-2,45,23])
print(lista)

# resultado = suma_elem([1,5,34,-3])#se le pasa la lista directamente
# print(f"El resultado de la suma es {resultado}")

# resultado = suma_elem(5)#genera un error de typeerror
# print(resultado)