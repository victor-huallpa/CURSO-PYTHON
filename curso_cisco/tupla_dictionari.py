#crea tublas y diccionarios y iteralas mediante bucles y tambien utiliza las funciones que se pueden realizar con ellas

#un diccionario es mutable, ya que se puede modificar y acceder a ella pero no es una lista.
dic = {"felino":"gato","canido":"perro","ave":"aguila","pez":"atun"}

print(dic)

print(dic['felino'])
#modificando el contenido de acuerdo a la clave
dic['felino'] = 'leon'
print(dic['felino'])

#agregar una clave y su contenido
dic['reptil'] = 'cocodrilo'
print(dic)

#funciones y metodos con diccionarios
del dic['reptil']
print(dic)
#funcion keys()
for item in dic.keys():
    print(item,"->",dic[item])
#funcion items()
for tipo,animal in dic.items():
    print(tipo, "->", animal)
#funcion sorted()
for item in sorted(dic.keys()):
    print(item, "->", dic[item])
#funcion values() es limitada por temas de que solo retorna valores 
for item in dic.values():
    print(item)

#metodo update(), se utiliza para actulizar o agregar mas keys and values al diccionario
dic.update({"insecto":"mosca"})
print(dic)
# una tupla es inmutable no se puede modificar directamente a ecepcion de eliminar la tubla
tup = ("perro","gato","raton")
tup2 = ("vaca","oveja","caballo")


print(tup)
print(tup[0])
print(len(tup))
for item in tup:
    print(item)


#funciones y metodos con tublas
tup3 = tup + tup2 #suma o union de tublas
tup4 = tup * 2 # multiplicar tublas
print (tup3,"\n",tup4)
print(type(tup4))
    
#tuplas y diccionarios juntos
tupla = (1,2,3)
print(type(tupla))
diccionary = {"numeros":tupla}
print(diccionary['numeros'])

for numeros in diccionary["numeros"]:
    print(numeros)
del tup4
print(tup4)

