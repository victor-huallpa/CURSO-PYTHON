fijo = 85528
while True:
    ingre = float(input('intodusca su ingreso anual de año anterior: '))
    ingre = round(ingre, 0)

    if ingre <= fijo:
        impuesto = ingre*0.18 -556.2
        if impuesto <= 0:
            print(' buen trabajo usted no pagara impusto alguno\n')
            print('se le retornara todo su ingreoso '+ str(ingre) + ' pesos\n________________')
            print('que tenga buen dia\n-----------------\n')
        elif impuesto >0:
            retor = ingre - impuesto
        
            print('el impuesto que debe de pagar es de ' + str(impuesto) + 'pesos')
            print('se le retornara un total de ' + str(retor) + ' pesos')
        
    elif ingre > fijo:
        impuesto = 14838.2 + ((ingre % fijo)*0.32)
        retor = ingre - impuesto
        print('el impuesto que debe de pagar es de ' + str(impuesto) + 'pesos')
        print('se le retornara un total de ' + str(retor) + ' pesos')