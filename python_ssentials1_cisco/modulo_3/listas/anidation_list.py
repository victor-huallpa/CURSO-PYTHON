#las lista pueden estar anidadas (una lisata dentro de otralista)

#mylista = [1,2,[1,2,[1,2,[...]]],[]]

one_list = [1,2,3]
two_list = ['hello', 'goobye', 'see you tomorrow']
print(f"listas\n {one_list}\n{two_list}")
total_list = ['numero', two_list, 'saludo', one_list]
print(f"lista final: \n {total_list}\n")

#foram de acceder a cada una de de los elementos de las listas anidadas

for i in range(len(total_list[1])):
    if len(total_list[1]) <= len(total_list[3]):
        print(f"{total_list[3][i]}: {total_list[1][i]}")
    # print(total_list[1][i])

for i in range(len(total_list[3])):
    print(total_list[3][i])