'''
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
    [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
     {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
     {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
     {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
     {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}] 

Construir una función que permita hacer búsqueda de inmuebles en función 
de un presupuesto dado. La función recibirá como entrada la lista de 
inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio 
sea menor o igual que el dado. Los inmuebles de la lista que se devuelva 
deben incorporar un nuevo par a cada diccionario con el precio del 
inmueble, donde el precio de un inmueble se calcula con la siguiente 
fórmula en función de la zona:
•Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 
15000) * (1-antiguedad/100)
•Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 
15000) * (1-antiguedad/100) * 1.5
'''

def calcular_precio(lista_inmuebles, presupuesto):
    inmuebles_aprobados = []
    for inmueble in lista_inmuebles:
        zona = inmueble['zona']
        metros = inmueble['metros']
        habitaciones = inmueble['habitaciones']
        garaje = inmueble['garaje']
        antiguedad = 2024 - inmueble['año']

        if zona == 'A':
            precio_inmueble = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
        elif zona == 'B':
            precio_inmueble = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5
        else:
            continue
        
        inmueble['precio'] = precio_inmueble

        if precio_inmueble <= presupuesto:
            inmuebles_aprobados.append(inmueble)

    return inmuebles_aprobados


### Programa Principal ###

lista_inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = int(input("Ingrese su presupuesto para la compra del inmueble: "))

inmuebles_aprobados = calcular_precio(lista_inmuebles, presupuesto)
for inmueble in inmuebles_aprobados:
    precio_formatado = format(inmueble['precio'], '.2f')
    print(f"El inmueble del año {inmueble['año']} tiene un precio de ${precio_formatado}")

    
    


