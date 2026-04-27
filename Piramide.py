#Crea un algoritmo que permita construir un paramide a partir de la cantidad de materiales ingreasdos por el usuario
#recuerda que, si en caso falte material el sistema debe informarlo y terminar el bucle de consctruccion
#tambien recuerda que debe indicar la cantidad de material que falta para terminar la piramide y indicar tambie nque altura tendra la piramide
while True:
    n=int(input("\nMateriales: "))
    if n==0:break
    i=1
    c=0
    while n>=i :
        n-=i
        i+=1
    print((i)*" "+"_")
    while i>0:
        i-=1
        print(i*" "+"|_|"+c*"_|")
        c+=1
    print("\nNumero de pisos de la Piramide:\t\t",c)
    print("Material Faltante para el proximo Piso:\t",(c-n+1))

