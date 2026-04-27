#crear un algoritmo que encuentre la palabra secreta y cuando la encuentre la detenga con la centencia break.
secret = 'chupacabra'

while True:
    ingre=str(input('ingrese la palabra secreta para salir del bucle: '))
    
    if ingre != secret:
        print(f"""
              jajajaja, eres un tontito la palabra {ingre}
              no es la palabra secreta no puedes salir de este infinito
              bucle_______________\n""")
        print("""
              ¿_______________________
              |   sigue intentando   |
              |______________________|\n
              """)
    elif ingre == secret:
        print('no es podible, como lo adivinaste.')
        break
    else :
        print('algo salio mal')

print(f"""
      ___________________________________
      |  bien hecho lograste vencer al  |
      |           buffon                |  
      |la palabra secreta era {ingre}|
      ----------------------------------""")
    