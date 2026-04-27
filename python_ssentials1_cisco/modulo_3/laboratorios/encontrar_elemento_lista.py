#crea un algoritmo que identifique en que posicion del indice se encuentra dicho elemento

sistem_list = [1, 2, 3, 'hello']

word = '0'
pos = 1
message = f"El elemento {word} no se encuentra dentro de la lista"
for i in sistem_list:
    if word == i:
        message = f"El elemento {word} es el elemento numero: {pos}\nindice {pos-1}"
        break
    pos += 1
print(message)