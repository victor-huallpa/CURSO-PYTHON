#crear un algoritmo que calcule el teorema de pitagoras.
x = input('que desesa calcular \n 1. HIPOTENUZA.\n 2. CATETO\n ..')
def cateto(h, co):
    if h == 0 or co == 0 or h < co or h == co:
        print ('lo siento mucho los valores ingresados son incorrectos o no\ncumplen con el reglamento de pitagoras y los triangulos rectagulos')
    elif h > co: 
        resul= ((h**2)-(co**2))**0.5
        if resul < co:
            print('el CATETO ADYACENTE es:', resul)
        elif resul > co:
            print('el CATETO OPUESTO es:', resul)
    else:
        print('lo que introduciste no es valido')
        
if (x == 'HIPOTENUZA' or x == '1'):
    
    ca= int(input('ingrese el primer valor\"cateto adyacente\''))

    co= int(input('ingrese el segundo valor\"cateto opuesto\''))
    if ca == 0 or co == 0 :
        print('lo sentimos lo que tratas de allar no es un triangulo rectangulo')
    elif ca <= co or ca >= co:
        resul= ((ca**2)+(co**2))**0.5
        print('la hipotenuza es:', resul)
    else:
        print('lo que introduciste no es valido')

elif (x == 'CATETO' or x == '2'):
    h = int(input('ingrese la\"hipotenusa\": '))
    co= int(input('ingrese el \"cateto\": '))
    cateto(h, co)
else:
    print('algo salio mal')
