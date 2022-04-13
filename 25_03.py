##% definir si tiene vocales una palabra 

def es_vocal(letra):
    if letra =='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        return True
    else:
        return False 

def tiene_vocales(p):
    cant_vocales=False
    for i in p:
        cant_vocales=cant_vocales or es_vocal(i)
    return cant_vocales
    
def contar_vocales(p):
    cant_vocales=0
    for i in p:
        if es_vocal(i):
            cant_vocales=cant_vocales+1
    return cant_vocales 

#%% piedra, papel o tijera.

def regla(jug1,jug2):
    if jug1==jug2:
        return 0
    elif jug1=='piedra'and jug2=='tijera':
        return 2
    elif jug2=='piedra'and jug1=='tijera':
         return 1
     
     
    
    
    
    
resultado ==regla(apuesta1,apuesta2)
if resultado ==0:
    print("empate")
elif resultado ==1:
    print('gano1 ')
elif resultado==2:
    print('gano2')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    