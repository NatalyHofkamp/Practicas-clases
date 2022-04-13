# %% mazo de cartas, saco una carta, cuántas quedan? cual saqué?

#mi método

mazo = ['ancho de basto',
       '1 de basto',
       '2 de basto',
       '3 de basto',
       '4 de basto',
       '5 de basto',
       '6 de basto',
       '7 de basto',
       '11 de basto',
       '12 de basto',
       'ancho de copa',
       '1 de copa',
       '2 de copa',
       '3 de copa',
       '4 de copa',
       '5 de copa',
       '6 de copa',
       '7 de copa',
       '11 de copa',
       '12 de copa',
       'ancho de espada',
        '1 de espada',
        '2 de espada',
        '3 de espada',
        '4 de espada',
        '5 de espada',
        '6 de espada',
        '7 de espada',
        '11 de espada',
        '12 de espada',
        'ancho de oro',
        '1 de oro',
        '2 de oro',
        '3 de oro',
        '4 de oro',
        '5 de oro',
        '6 de oro',
        '7 de oro',
        '11 de oro',
        '12 de oro']
total_mazo= len(mazo)
carta = int(input('ingrese un numero'))
print (f'el mazo tiene {total_mazo} cartas')
print (f'se sacó del mazo la carta : {mazo[carta-1]}')

del mazo[carta-1]

total_mazo= len(mazo)
print (f'ahora el mazo tiene {total_mazo} cartas')




#%% mazo de cartas, saco una carta, cuántas quedan? cual saqué?
#método de ernesto


mazo = list(range(1,41))
print (mazo)
import random 
carta = random.choice(mazo)
del mazo[carta]
def busqueda_posicion (carta):
    inicio = 0
    final = len(mazo)
    while inicio <= final:
        valor_medio = (inicio +final)//2
        if  carta == mazo[valor_medio-1]:
            return valor_medio
        elif carta < mazo[valor_medio-1]:
            final = valor_medio-1
        else: 
            inicio = valor_medio+1
            
def posicion_elemento (carta):
    resultado_busqueda = busqueda_posicion(carta)
    if resultado_busqueda is None:
        return f'La carta {carta} no se encuentra en el mazo'
    else:
        return  resultado_busqueda
print (posicion_elemento(carta))


#def nom_carta (resultado_busqueda):
 #   nombre_carta = mazo2.index(resultado_busqueda)
  #  if resultado_busqueda :
   #     return ( f'la carta  que se quitó estaba en la posición {resultado_busqueda},por lo tanto era la carta {nombre_carta}')
#print (nom_carta(resultado_busqueda))

cant_mazo= len (mazo)
print (f'Ahora el mazo tiene {cant_mazo} cartas')











