#una tupla es una coleccion de datos que no se pueden remover, estas inician con parentesis separados por comas
# o simplemente se almacenan separadas por comas.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(type(tuple_1))

#las tuplas tambien se puede nsumar y multiplicar
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#las tuplas tambien puede ncambiar o ciruclar sus valores entre tuplas
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
 