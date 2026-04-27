#crea un algoritmo donde puedas verificar cual es el mayor numero de una lista eh imprimela

sistem_list = [1, 4, 44, 15, 9]
num = sistem_list[0]
for i in range(len(sistem_list)-1):
    if sistem_list[i+1] > num:
        num = sistem_list[i+1]
    
print(num)

sistem_list = [1, 4, 5, 15, 9]
num = sistem_list[0]

for i in sistem_list:
    if i > num:
        num = i
print(num)

sistem_list = [1, 4, 5, 15, 9]
num = sistem_list[0]

for i in sistem_list[1:]:
    if i > num:
        num = i
print(num)