secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
\n""")
num = int(input('ingrese numero: ')) 
while num != 777:
    print('\n')
    print("""
    jajajaja , estas atrapado en 
    mi juego infinito, puedes 
    llorar si deceas, sigue intentando
    \n""")
    num = int(input('ingrese numero: '))
print(f"""
      \nwooo! lo adivinaste!!!!
      el numeor que te asigne fue {num} """)
    

