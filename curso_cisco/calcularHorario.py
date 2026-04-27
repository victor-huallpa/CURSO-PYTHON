while True:
    hour = input("Hora de inicio (horas): ")
    mins = input("Minuto de inicio (minutos): ")
    dura = input("Duración del evento (minutos): ")
    def conver(hour, mins, dura):
        hour = int(hour)
        mins = int(mins)
        dura = int(dura)
        tiem_cal(hour, mins, dura)
        
    def tiem_cal(hour, mins, dura):
        mindu = (dura+mins)%60
        hourdu = (((mins + dura)//60)+hour)%24
        hourf  = str(hourdu)+':'+str(mindu)
        print('el evento termina a las '+hourf+' horas')
        
    if (hour <= '23' and hour >= '0' and mins <= '59' and mins >= '0' ):
        conver(hour, mins, dura)
    
    elif (hour == '24' and mins == '60') or (hour == '0' and mins == '60') or (hour == '24' and mins == '0'):
        print('ten cuidado las 24 hours es igual 00 hours or 60 mins es igual 00 mins ')
        conver(hour, mins, dura)
        
    else:
        print('los datos ingresados son incorrectos.\n vuelva intentarlo\n recordatorio la zona horaira es de 24 horas y 60 minutos')
        
        

# Escribe tu código aquí.