#La dimenicon de las listas son listas anidadas
#donde puedes ubicar cada una de ella mediante coordenadas Fila,Columna

#crea un algorimit donde sedas esapcios a cada hora del dia durante un mes de 31 dias

temps = [[0.0 for h in range(24)] for d in range(31)]
# for i in range(31):
#     temp = float(input(f"Ingresa la temperatura marcada al media dia del dia {i+1}: "))
#     temps[i][11] = temp 
 
total = 0.0
 
for day in temps:
    print(day[11])
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)
for i in range(31):
    print(f"DIA {i+1}: {temps[i]}")

    highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")

#arreglo tridimencional
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False


vacancy = 0
 
for room_number in range(20):
    for o in range(5,12,3):
        rooms[2][14][o] = True
    if not rooms[2][14][room_number]:
        vacancy += 1
for i in range(3):
    print(f"edificio {i+1}: ")

    for h in range(15):
        print(f"piso {h+1}: {rooms[i][h]}")
print(vacancy)