temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
# print(len(temps))
for i in range(len(temps)):
    tem = float(input('ingrese la tempreatura de hoy a las 12pm: '))
    temps[i][11]= tem
for i in range(len(temps)):
    print(temps[i])
    
total = 0.0

for i  in range(31):
    total += temps[i][11]

average = total / 31

print("Temperatura promedio al mediodía:", average)

