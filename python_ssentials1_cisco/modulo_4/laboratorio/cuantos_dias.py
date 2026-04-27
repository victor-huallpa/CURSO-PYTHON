#Crea un algoritmo donde una funcion tome dos argumentos (anio y un mes) y devuelva el nuermo de dias del mes respecto de anio dado
#consider que febrero es sensible al valor year, tu funcion deveria ser universal

#haz que tu funcion devuelva none si los argumentos no tiene sentido


def is_year_leap(year):
    if (year%4 and year % 100 != 0) or year%400 == 0:
        return True
    return False

def days_in_month(year, month):
    list_month1 = [1,3,5,7,8,10,12]
    list_month2= [2,4,6,9,11]

    if month in list_month2:
        if month == 2:
            result = is_year_leap(year)
            if result:
                return 29
            return 28
        return 30
    elif month in list_month1:
        return 31
    else:
        return

print('------------------------------------------------------')
print('|--------- Bien venido a calculando el anio ---------|')
print('------------------------------------------------------\n')

while True:
    print('Si desea salir digite "0"')
    year_user = int(input("Por favor ingrese el anios: "))
    if year_user == 0:
        break
    month_user = int(input("ingrese en numero el mes del anio: "))



    day = dey_month = days_in_month(year_user, month_user)

    if is_year_leap(year_user):
        year = 'biciesto'
    else:
        year = 'normal'
    print(f"El anio {year_user} es {year} y el mes {month_user} tiene {day}\n")
    

print('\n-------------------------------------------------------------')
print('|--------- Gracias por juagar a calculando el anio ---------|')
print('-------------------------------------------------------------\n')
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")