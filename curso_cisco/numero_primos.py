#crear un algoritmo con funciones que peuda identificar un nuero primo.
def is_prime(num):
    for i in range(2,int(1+ num**0.5)):
        if num%i == 0:
            return False
        return True

        
dato= int(input('ingresa un numero o cero para sair'))
while dato!=0:
    num=int(input('ingresa un muero para saber si es primo: '))
    for i in range(1, num):
        if is_prime(i + 1):
            print(i + 1, end=" ")
    print(is_prime(num))
    dato= int(input('ingresa un numero o cero para sair: '))
    
