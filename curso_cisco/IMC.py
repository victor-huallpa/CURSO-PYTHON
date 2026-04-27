# crear un algoritmo que calcule el IMC de una persona mayor a 18 anios, 
# este algoritmo tiene que contar con funciones

# Función para verificar la edad del usuario
def edad_usuario(edad):
    if 18 <= edad < 150:
        return True
    elif edad == 0:
        print('Gracias por usar nuestra app para calcular su IMC. ¡Vuelva pronto!')
        return False
    elif 0 < edad < 18:
        print('Lo siento, aún el sistema no está preparado para calcular el IMC de niños y adolescentes.')
        return False
    else:
        print('Lo siento, la edad que ingresaste no está dentro de los parámetros.')
        return False

# Función para calcular el IMC
def imc(peso, altura):
    return peso / (altura ** 2)

# Función para determinar el estado de IMC
def estado(resultado_imc):
    if 18.5 <= resultado_imc < 25:
        return 'normal'
    elif resultado_imc < 16:
        return 'de delgadez severa\nRecomendamos que visite su nutricionista por temas de salud.'
    elif 16 <= resultado_imc < 17:
        return 'de delgadez moderada\nRecomendamos que visite su nutricionista.'
    elif 17 <= resultado_imc < 18.5:
        return 'de delgadez leve.\nDebe alimentarse mejor.'
    elif 25 <= resultado_imc < 30:
        return 'pre obeso.'
    elif 30 <= resultado_imc < 35:
        return 'de obeso tipo I.'
    elif 35 <= resultado_imc < 40:
        return 'de obeso tipo II.\nRecomendamos que visite su nutricionista.'
    elif resultado_imc >= 40:
        return 'de obeso tipo III.\nRecomendamos que visite su nutricionista por temas de salud.'

# Función para validar los datos de peso y estatura
def validar_datos(peso, estatura):
    if 20 <= peso <= 200 and 1 <= estatura <= 2.10:
        return True
    elif (estatura < 1 or estatura > 2.10) and (peso < 20 or peso > 200):
        print(f'El peso {peso} kg y la estatura {estatura} m no corresponden a una persona. Consulte a su médico.\n')
        return False
    elif (peso < 20 or peso > 200) and 1 <= estatura <= 2.10:
        print(f'El peso {peso} kg no corresponde a una persona. Consulte a su médico.')
        return False
    elif (estatura < 1 or estatura > 2.10) and 20 <= peso <= 200:
        print(f'La estatura {estatura} m no corresponde a una persona. Consulte a su médico.')
        return False
    else:
        print('Lo sentimos, los datos ingresados no son válidos.')
        return False

# Código principal
print('Ingrese "0" como edad para salir.')

while True:
    try:
        edad = int(input('Ingrese su edad en años: '))
        if edad_usuario(edad):
            try:
                peso = float(input('Ingrese su peso en kg: '))
                altura = float(input('Ingrese su estatura en metros: '))
                if validar_datos(peso, altura):
                    resultado_imc = imc(peso, altura)
                    print(f'Su IMC es de {resultado_imc:.2f}. Lo que indica que usted está en estado {estado(resultado_imc)}.')
            except ValueError:
                print('Error: Los datos ingresados no son válidos. Por favor, ingrese números para peso y estatura.')
        elif edad == 0:
            break
    except ValueError:
        print('Error: La edad ingresada no es válida. Por favor, ingrese un número entero.')
