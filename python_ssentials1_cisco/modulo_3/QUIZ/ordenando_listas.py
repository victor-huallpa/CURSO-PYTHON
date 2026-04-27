#Crea un algoritmo que ordene el conteido de una lista donde se almacena numero enteros 
#Si deseas puedes pedir al usuario que ingrese estos daots de la lista.

my_list = [3,11,1,6,5,2,-1,8,8]
print(my_list)
for i in range(len(my_list)):
    if  i<len(my_list)-1:
        # print(i)
        for n in range(len(my_list)):
            if  n<len(my_list)-1:

                if my_list[n] > my_list[n+1]:
                    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]

print(my_list)
my_list = []

swaped = True

num = int(input("Cuantos elementos deseas ordenar?: "))
for i in range(num):
    element = int(input(f"Ingrese el elemento {i+1}: "))
    my_list.insert(0, element)
print(f"Aqui tienes tu lista :\n{my_list}")

form = input('Como desea ordenar tu lista:\n1 asendente\n2 desendente\n').lower()

while swaped:
    swaped = False

    for i in range(len(my_list)-1):
        if form == 'asendente' or form == '1':
            form = 'asendente'
            if my_list[i] > my_list[i+1]:
                swaped = True
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        if form == 'desendente' or form == '2':
            form = 'desendente'
            if my_list[i] < my_list[i+1]:
                swaped = True
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]


print(f"Aqui tienes tu lista ordenada de forma {form}:\n{my_list}")

