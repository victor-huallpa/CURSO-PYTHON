#los diccionarios son pares de datos encerrados entre llaves, estos pares tiene la sigeuitne estructura
#llave : valor o key:value y estas se separan de otros pares rodenados por comas,
#en cuanto al tipo de datos, estos pueden ser cualquier tipo de datos a seppcion de listas
#los diccionarios son mutables 

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['gato'])
print(phone_numbers['Suzy'])

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")