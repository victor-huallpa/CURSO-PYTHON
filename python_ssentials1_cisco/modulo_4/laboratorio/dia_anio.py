#crea un algoritmo que de detecte que dia del anio es a partir de del tipo de anio y mes del anio
def is_year_leap(year):
    if (year%4 == 0 and year % 100 != 0) or year%400 == 0:
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

def day_of_year(year, month, day):
    if day > 31 or day < 0:
        return f"El dia {day} sobre sale de los dias de un mes normal\ndia normal esta entre \n1 y 31 \n1 y 30 \n1 y 29 en caso bisiseto\n1 y 28 \nRecuerda que depende del mes en que te encuentres."
    if days_in_month(year, month) == 29 and day > 29:
        return F"Lo siento el segundo mes del anio {year} solo tiene 29 dias como maximo"
    if days_in_month(year, month) == 28 and day > 28:
        return F"Lo siento el segundo mes del anio {year} solo tiene 28 dias como maximo"

    days = 0
    for i in range(month-1):
        result = days_in_month(year, i+1)
        print(result)
        days += int(result)
    days += day
    return days
    

    
print(day_of_year(2001, 2, 36))
