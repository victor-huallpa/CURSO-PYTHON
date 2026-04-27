#existen metodos y funciones para poder trabajar con diccionarios
#en el bucle for no podemos iterar directamente un diccionario pero si usamos 
#el metodo keys esto se veulve realidad

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 
#otra manera es usando el metodo items()

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)

#function sorted(), esta funcion ayuda a que los datos aparescan ordenados
for key in sorted(dictionary.keys()):
    print(spanish, "->", french)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for french in dictionary.values():
    print(french)

#agregar nuevas claves
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)

#eliminar una clave
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

#para eliminar la ultima clave
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}