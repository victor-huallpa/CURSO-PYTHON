# # def is_year_leap(year):
# #     if year % 4 != 0:
# #         return False
# #     elif year % 100 != 0:
# #         return True
# #     elif year % 400 != 0:
# #         return False
# #     else:
# #         return True

# # def days_in_month(year,month):
# #     if year < 1582 or month < 1 or month > 12:
# #         return None
# #     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #     res  = days[month - 1]
# #     if month == 2 and is_year_leap(year):
# #         res = 29
# #     return res

# # test_years = [1900, 2000, 2016, 1987]
# # test_months = [ 2, 2, 1, 11]
# # test_results = [28, 29, 31, 30]
# # for i in range(len(test_years)):
# #     yr = test_years[i]
# #     mo = test_months[i]
# #     print(yr,mo,"-> ",end="")
# #     result = days_in_month(yr, mo)
# #     if result == test_results[i]:
# #         print("OK")
# #     else:
# #         print("Fallido")
# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
def anio_tipo(datoA):
    if (datoA % 4 == 0 and datoA%100!=0) or (datoA%400==0):
        print('bisiesto')
        return True
    elif (datoA % 4 != 0 and datoA%100==0) or (datoA%400!=0):
        return False
    else:
        print('algo salio mal')
def parametro(datoA,datoM):
    if datoA<1582 or datoM<1 or datoM>12 :
        return None
    mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = mes[datoM-1]
    if datoM == 2 and anio_tipo(datoA)==True:
        res=29
    return res

def cal_dia_anio(datoA,datoM,datoD):
    dias_total=0
    
    for m in range(1, datoM):
        # print(mes[i])
        md = parametro(datoA,m)
        if md ==None:
            return None
        dias_total +=md
    md = parametro(datoA, datoM)
    if datoD >=1 or datoD <= md:
        return datoD + dias_total
    else:
        return None
dato = int(input('ingrese\n1 para continuar y \ncialquier tecla para salirpara salir'))
while dato == 1:
    datoA = int(input('ingrese el año: '))
    datoM = int(input('ingrese el mes: '))
    datoD = int(input('ingrese dia del mes: '))
        
    print(cal_dia_anio(datoA,datoM,datoD))
