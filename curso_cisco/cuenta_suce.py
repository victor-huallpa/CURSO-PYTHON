#crear un algoritmo de cuenta sucesiva.
# for i in range(-2,11):
#     # if i%2 != 0:
#     #     print(f'ceunta sucesica {i}')
#     # i+=1
    
#     i = str(i)
#     if i in '2,4,6,8,10':
#         continue
#     print(f'ceunta sucesica {i}')
#     i = int(i)
    
#     i+=1   
# print('despegen')
enla = ''
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    enla += ch
    print(ch, end="")
print(f'\n{enla}')