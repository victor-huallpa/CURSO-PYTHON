# #es la forma como evaluamos los valores boleanos entre True y False
# #con las expresiones 'and', 'or' y 'not'

user_numbre = int(input("Ingrese un numero: "))

if user_numbre > 0 and user_numbre <= 10:
    print("El numero ingresado esta dentro del rango del 1 al 10")
elif user_numbre > 10 or user_numbre < 0:
    print("El numero ingresado esta fuera del rango del 1 al 10")
else:
    print("Lo ingresado no es un numero valido")

#Leyes de De Morgan
# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

#ejemplo

if not(user_numbre > 0 and user_numbre <=10):
    print("El numero ingrasado esta fuera del rango del 1 al 10 ")
elif not(user_numbre > 10 or user_numbre < 0):
    print("El numero ingresado esta dentro del rango del 1 al 10")
else:
    print("Lo ingresado no es un numero valido")

if(not (user_numbre > 0) or not(user_numbre <= 10)):
    print("El numero ingrasado esta fuera del rango del 1 al 10 ")
elif(not(user_numbre >10) and not(user_numbre <0)):
    print("El numero ingresado esta dentro del rango del 1 al 10")
else:
    print("Lo ingresado no es un numero valido")

i = 0
j = not not i
print(i, j)

