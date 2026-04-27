#crea un algoritmo donde el usuario ingrese un palabra y el sistema evalue esta palabra dentro de unm bucle
#considera que las palabras ingresadas por el usuario no deben ser impresas en consola
#usa while
print("|------ Bien venidos al juego de la cabra -------|")
word = input("Ingrese una palabra: ")

word_secret = "chupacabras"

while True: 
    if word == word_secret:
        print(f"Has dejado el bucle con exito!.")
        break
    print("JAJAJA, Estas atrapado en este bucle de la cabra.\n")
    word = input("Ingrese neuvamenteuna palabra: ")
