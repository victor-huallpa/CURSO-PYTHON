#las funciones son bloques de codigo que ayudan con una tarea especifica(contiene instrucciones  que se agrupan bajo un nombre)
#esta funciones ayduan a modularizar el codigo, hacienod mas legible, reutilizable y facil de mantener 
#Las funciones pueden resivir parametros o argumentos, y devolver resultados

#def nombre (parametros):
    #funcion del condigo
sitema = 'arbis'
num_dato = 1
data_list = []
def entrada_datos(nombre, num_dato):
    add_date = input(f"El sistema {nombre} requiere el dato {num_dato}: ")
    return add_date

num_user = int(input("\nCuantos datos desea ingresar: "))
while num_dato <= num_user  and num_user > 0:
    add_date = entrada_datos(sitema, num_dato)
    data_list.append(add_date)
    num_dato += 1

else:
    print(data_list)
    print(f"Ingreso {num_dato-1} datos")
    num_dato = 0
