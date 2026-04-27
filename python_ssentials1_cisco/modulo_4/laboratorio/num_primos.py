#crea un algoritmo que detecte si un numero es primo o no 
#considera que imprima los primos que se encuentran e ndicho numero

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False
num = 2000209
if is_prime(num):
    print(f"El numero {num} no es primo")
else :
    print(f"El numero {num} es primo")

for i in range(1, num):
    if not is_prime(i+1):
        print(i+1, end=' ')
    
print('')