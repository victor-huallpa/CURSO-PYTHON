# # my_list = []  # Creando una lista vacía.
 
# # for i in range(5):
# #     my_list.insert(0, i + 1)
 
# # print(my_list)

# # total = 0

# # for i in range(len(my_list)):
# #     total += my_list[i]

# # print(total)
# # indi = -1

# # for i in range(len(my_list)):
# #     indi += 1
# #     print(f'{my_list[indi]}, ',end='') 
 
    
# # my_list = [10, 1, 8, 3, 5]
# # total = 0
 
# # for i in my_list:
# #     total += i
 
# # print('\n',total)

# # my_list = [10, 1, 8, 3, 5]
 
# # my_list[0], my_list[4] = my_list[4], my_list[0]
# # my_list[1], my_list[3] = my_list[3], my_list[1]
 
# # print(my_list)

# # # for i in range(length // 2):
# # #     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# # # print(my_list)
# # my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
# # for color in my_list:
# #     print(color)
    
# # my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# # swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# # while swapped:
# #     swapped = False  # no hay intercambios hasta ahora
# #     for i in range(len(my_list) - 1):
# #         if my_list[i] > my_list[i + 1]:
# #             swapped = True  # ¡ocurrió el intercambio!
# #             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# # print(my_list)


# # i = 0
# # while i <= 5:
# #     i += 1
# #     if i % 2 == 0:
# #         break
# #     print("*")

# for i in range(1):
#     print("#")
# else:
#     print("#")
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
#     print(var)
    
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
 
# print(c + d + e)

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

def anio_tipo(datoA):
    if (datoA % 4 == 0 and datoA%100!=0) or (datoA%400==0):
        print('bisiesto')
        return True
    elif (datoA % 4 != 0 and datoA%100==0) or (datoA%400!=0):
        return False
    else:
        print('algo salio mal')
def parametro(datoA,datoM):
    if datoA<1582 or datoM<1 or datoM>12 :
        return None
    mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = mes[datoM-1]
    if datoM == 2 and anio_tipo(datoA)==True:
        res=29
    return res

def cal_dia_anio(datoA,datoM,datoD):
    dias_total=0
    
    for m in range(1, datoM):
        # print(mes[i])
        md = parametro(datoA,m)
        if md ==None:
            return None
        dias_total +=md
    md = parametro(datoA, datoM)
    if datoD >=1 or datoD <= md:
        return datoD + dias_total
    else:
        return None
dato = int(input('ingrese\n1 para continuar y \ncialquier tecla para salirpara salir'))
while dato == 1:
    datoA = int(input('ingrese el año: '))
    datoM = int(input('ingrese el mes: '))
    datoD = int(input('ingrese dia del mes: '))
        
    print(cal_dia_anio(datoA,datoM,datoD))