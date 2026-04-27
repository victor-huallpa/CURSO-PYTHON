#Crea un algoritmo que recete el correo almacenado en una varible,
#considera que el correo de la variable debe ser resseteado a partir del signo '@'
#y una vez llege a este punto debe imprimir lo que le antesede a este signo de arroba
reset_email = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        print(f"El correo es: {reset_email}")
        break
    reset_email += ch


for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")