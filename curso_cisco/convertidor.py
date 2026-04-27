oneKilo = 1.61
def calculark(kilometers, oneKilo):
    kilometers_to_miles = kilometers/oneKilo
    print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas\n")
    
def calcularm(miles, oneKilo):
    miles_to_kilometers = miles * oneKilo
    print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros\n")
while True:
    q=input('que desea calcular \n1. miles to kilometers.\n2. kilometers to miles\n3. salir\n')

    if q == 'miles' or q == '1':
        miles = float(input('ingrese la cantidad de miles: '))
        calcularm(miles, oneKilo)
        
    elif q == 'kilometers' or q == '2':
        kilometers = float(input('ingrese la cantidad de kilometers: '))
        calculark(kilometers, oneKilo)
    
    elif q == 'salir' or q == '3':
        print('gracias por usar nuestra app de convercion\n-------------\n')
        break
        
    else:
        print('Algo salio mal en todo esto')

