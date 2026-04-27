#comunmente en python puden surgir error ya sea nde sintaxis, de tipos de tipos de datos entre otros, 
#estas excepciones pueden ser manejadas deuna mera conveniente para el desarrollador
#con try y except

try:
    num = int(input("ingrese un numero: "))
except:
    print("lo siento lo que ingreso no es lo requerido")

#NOTA:
#al amnra como manejamos la excepicon es muy general ya que podemos manejarla de manera mas presisa

try:
    num = int(input("ingrese un nemero: "))
    print(4/num)
except ZeroDivisionError:
    print("no se puede  dividir entre cero")
except:
    print("lo quei ngresaste no esta dentro de lo requerido")

#NOTA:
#como observas la operacion realizada en except centra si se divirada entrese cero si es ahci te manda a la excepcion
#caso contrario si es texto te manda a la segunda excepcion
