# Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

# paso 1: crea una lista vacía llamada beatles;
# paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
# paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append('Jhohn Lennon')
beatles.append('Paul McCartney' )
beatles.append( 'George Harrison')
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    print('Stu Sutcliffe, y Pete Best\n')
    integrantes = input('ingrese los nuevos integrantes de los bealtes: ')
    beatles.append(integrantes)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,'Ringo Starr')
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

