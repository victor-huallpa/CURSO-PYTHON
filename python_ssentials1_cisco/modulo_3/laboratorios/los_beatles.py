#Escribe un lagoritmo que realice los cambios de todos los integrantes de los beatles durante toda su carrera
#Considera:
# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles = []

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)
for i in range(2):
    new_inte = input('Ingrese a los nuevos integrantes de la banda de rock: ')
    beatles.append(new_inte)

print(beatles)
del beatles[3]
print(beatles)
del beatles[3]
print(beatles)

beatles.insert(0, 'Ringo Starr')
print(beatles)
