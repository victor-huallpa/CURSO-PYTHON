#crea un algoritmo utilizando listas, tuplas y diccionarios, para calcular la nota de alumnos de un colegio
#de acuerdo al curso

# Diccionario para almacenar los cursos y las notas de los alumnos
cursos = {}

# Función para validar si la nota está en el rango válido (0-20)
def validar_nota(nota):
    """
    Valida que la nota esté entre 0 y 20.
    
    Args:
        nota (float): La nota a validar.
    
    Returns:
        bool: True si la nota es válida, False en caso contrario.
    """
    if 0 <= nota <= 20:
        return True
    else:
        print('Lo siento, la nota que ingresó no es válida. Vuelva a intentarlo.')
        return False

# Función para almacenar o actualizar un curso con la nota del alumno
def save(curso, nota):
    """
    Almacena la nota en el curso correspondiente. Si el curso ya existe, agrega la nota a la lista existente.
    Si el curso no existe, lo crea y agrega la nota.
    
    Args:
        curso (str): El nombre del curso.
        nota (float): La nota del alumno.
    
    Returns:
        None
    """
    if curso in cursos:
        cursos[curso].append(nota)
    else:
        cursos[curso] = [nota]
    return

# Función para calcular el promedio de notas por curso
def promedio_cursos(cursos):
    """
    Calcula y muestra el promedio de notas para cada curso almacenado en el diccionario 'cursos'.
    
    Args:
        cursos (dict): Un diccionario con los cursos como claves y las notas como valores (listas).
    
    Returns:
        None
    """
    for materia, notas in cursos.items():
        if notas:
            promedio = sum(notas) / len(notas)
            print(f'{materia}: Promedio: {promedio:.2f}')
        else:
            print(f'{materia}: No hay notas disponibles para calcular el promedio')
while True:
    curso = input('Ingrese el nombre del curso: ')
    try:
        nota = float(input("Ingrese la nota del alumno del 0-20: "))
        if validar_nota(nota):
            save(curso, nota)
    except ValueError:
        print('\nIngrese una nota válida, debe ser un número no otro tipo de texto.')
    
    continuar = input("¿Desea ingresar otra nota? (s/n): ").lower()
    if continuar != 's':
        print("\nPromedios de los cursos:")
        promedio_cursos(cursos)
        break
