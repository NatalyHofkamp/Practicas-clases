#%%  G U I A 1
#%% 11)
def main ():
    pizza6 = 1020*2
    pizza8 = 1380
    bebypic = 410
    postre = 800  
    amigos = 5
    gstotal= pizza6 + pizza8 + bebypic + postre
    gsindiv = gstotal/amigos 
    amigo1y2= pizza6+pizza8
    amigo3 = bebypic
    amigo4 = postre
    amigo5=0
    
    gastos= [amigo1y2,amigo3,amigo4,amigo5]
    
    for i in gastos :
        if i > gsindiv:
             dar = abs (i -gsindiv)
             i= gastos.index(i)
             print (f'al amigo {i+1} le deben dar {dar} ')
            
        elif  i < gsindiv:
            devolver = abs (gsindiv-i)
            i = gastos.index (i)
            print (f'el amigo {i+1} debe devolver {devolver} ')


main ()
       

#%%  G U I A 2
#%% 13) 
# Escriba una función que dado un número devuelva el primer número múltiplo de 
#10 inferior o igual a él. Por ejemplo, para 153 debe devolver 150.


def multiplo (numero):
    
    for i in range (numero,0,-1):
        if i<=numero and i%10==0:
           return i
        
print (multiplo(153))
print (multiplo(45))
#%% 12) 
# Escriba una función que dadas la hora, minutos y segundos devuelva el tiempo
#en segundos.

def segundos (tiempo):
    
    tiempo = list (tiempo.split(':'))
    
    hora = int(tiempo [0])
    minutos = int (tiempo [1])
    segundos = int (tiempo [2])
    
    hora= hora *3600
    minutos = minutos*60
    
    tiempo = ':'.join (tiempo)
    print ( f' hay {hora+minutos+segundos} segundos en la hora {tiempo} ')
    
    
segundos ('12:23:15')

#%% 12)b)

#Escriba un programa que pida la hora al usuario y muestre el tiempo en segundos.

def segundos ():
   tiempo =[]
   hora = str(input('ingrese la hora'))
   tiempo.append (hora)
   minutos = str(input('ingrese los minutos'))
   tiempo.append (minutos)
   segundos = str(input('ingrese los segundos'))
   tiempo.append(segundos)
   hora_seg= int (tiempo[0])*3600
   minutos_seg= int(tiempo[1])*60
   
   hora =':'.join (tiempo)
   print(f'hay {hora_seg + minutos_seg+ int (tiempo[2])} segundos en la hora {hora} ')
segundos()


#%% 14)
#Escriba una función que dado un tiempo en segundos, retorne el tiempo en horas,
#minutos ysegundos. Por ejemplo, para 3745 debe devolver 1, 2, 25


def tiempo (segundos):
    
    hora =str(segundos //3600)
    minutos = str( (segundos % 3600)//60)
    segundo = str( (segundos % 3600)%60)

    hora = [hora,minutos,segundo]
    
    tiempo = ':'.join(hora)

    print (f'{segundos} segundos equvalen a {tiempo}')

tiempo (3600)

tiempo (44595)

#%% G U I A 3 pensar

#Escribir un programa que inicie pidiendo al usuario que ingrese la fecha e
#imprima cuántos días faltan para la primavera. 

def dia_año (dia,mes):
    if mes == 2:
        dia= dia+31
    elif mes == 3:
        dia= dia+59
    elif mes == 4:
        dia = dia + 89
    elif mes == 5:
        dia = dia + 120
    elif mes == 6:
        dia = dia + 150
    elif mes == 7:
        dia = dia + 181
    elif mes == 8:
        dia = dia + 211
    elif mes == 9:
        dia = dia + 242
    elif mes ==10:
        dia = dia + 272
    elif mes== 11:
        dia= dia +303
    elif mes ==12:
        dia= dia+334
    return primavera (int(dia))

def primavera(dia): 
    if int(dia)< 264 :
        dias= 264 - dia  
        print(f'faltan {dias} dias para primavera.')
    elif int(dia)> 264 :
        dias= abs(365-dia)+264
        print(f'faltan {dias} dias para primavera.')
dia_año(18,7)
dia_año(1,1)
dia_año(13,11)

#%% G U I A 4
#%% 11)
#Escriba una función que le pida al usuario ingresar 10 números enteros y que 
#imprima el mayor número impar de los ingresados. De no haber ingresado ningún 
#número impar, que imprima un mensaje para dar aviso.

def max_impar (letras):
    
    letras = letras.split(',')
    numeros = list(letras)
    impares = []  
    for i in numeros:
        if int (i) %3==0 and  int (i) %2!=0:
            impares.append(int(i))
    print (impares)
    mayor_numero = max(impares)
    return (f' El mayor numero impar es : {mayor_numero}')

print(max_impar('1,2,3,4,5,6,7,8,9,10'))
print(max_impar('5,9,15,23,69,52,123,63,652,1'))
print(max_impar('8,5,36,456,852,459,12,357,1030,526'))


#%% 19) TERMINAR 
# Escriba un programa que juegue al piedra, papel o tijera contra el humano.


#%% 20)
import random 
def dados ():
    player1 = 0
    player2 = 0
    puntaje2= 0 
    while player1<30 and player2<30 :
        print (f'*** {player1} - {player2} ***')
        eleccion1 = int (input('Aprete 1 para tirar'))
        eleccion2 = int (input ('aprete 2 para tirar'))
        if eleccion1 ==1 and eleccion2==2:
             tiro1 = random.choice (range(1,7))
             print (f'player1 sacó {tiro1}')
             tiro2 = random.choice (range(1,7))
             print (f'player2 sacó {tiro2}')
             if tiro1!=tiro2 :
                    if tiro1 > tiro2:
                        puntaje = tiro1+tiro2+puntaje2
                        player1+= puntaje 
                        print ( f'ganó {puntaje} puntos player1 ')
                        puntaje2 = 0 
                    elif tiro1 < tiro2:
                       puntaje = tiro1+tiro2+puntaje2
                       player2+= puntaje 
                       print ( f'ganó {puntaje} puntos player2 ')
                       puntaje2 = 0
             else:
                 print ('ambos jugadores sacaron el mismo puntaje')
                 puntaje2 = tiro1+tiro2 
        else:
            print ('ingrese un valor válido')
                 
    return winner(player1,player2)

def winner (player1,player2):
    if player1>player2:
        print ('**PLAYER1 ES EL GANADOR, FELICIDADES!**')
    else: 
        print ('**PLAYER2 ES EL GANADOR, FELICIDADES!**')
dados()








#%%

def count_A(the_string):
    contador = 0
    for i in the_string:
        if i =='a' or i=='A':
            contador+=1
    return contador

print(count_A('banana'))

#%%

def contador(texto:str):
    caracter_1=str(input('ingrese el primer caracter'))
    caracter_2 = str(input('ingrese el segundo caracter'))
    texto=texto.split(' ')
    texto=list(texto)
    contador_1=0
    contador_2=0
    
    for i in texto:
        for letra in i:
            if letra == caracter_1:
                contador_1+=1
            elif letra == caracter_2:
                contador_2+=1
    if contador_1>contador_2:
        print(f'hay más {caracter_1} que {caracter_2} ')
    else:
        print(f'hay más {caracter_2} que {caracter_1} ')
            
            
    
contador(' podemos ingresar una cadena relativamente larga y contar la cantidad de ocurrencias de un carácter')
            
            
            
            
            

            
            
            
            
#%%
            
def formato(fecha:str):
    fecha= fecha.split('-')
    fecha= list(fecha)
    lista=[]
    for i in fecha:
        lista.append(int(i))
    fecha= tuple(lista)
    return fecha

print(formato('2022-5-13'))
            
            
#%%

def multiplo(numero:int):
    Lista=list(range(numero,0,-1))
    
    for valor in Lista:
        if valor<=numero and valor%10==0:
            return  valor
print (multiplo(153) )          
            
            
#%%

def letras (cadena:str):

    letra_inicial=cadena[0]
    letra_final=cadena[-1]
    medio=len(cadena)//2
    letra_medio=cadena[medio]
    letras=[]
    letras.append(letra_inicial,letra_medio,letra_final)
    return ','.join(letras)
               
            
            
print(letras('banana'))            
            
            
            
#%%

def terminan_en_vocal(lista):
    vocales='aeiou'
    vocal=[]
    for i in lista:
        if i[-1] in vocales:
            vocal.append(i)
    return vocal
            
print(terminan_en_vocal(['hola','como','estas']))          
            
            
            
    

#%%

def eliminar(listas,numero):
    for i in listas:
        if i[2]>numero:
            listas.remove(i)
    return listas


print(eliminar( [["W", 5, 31], ["U", 7, 18], ["F",
11, 15], ["B", 16, 28]],20))




#%%

def lenguaje(lista):
    x=0
    for i in lista:
        if i=='++x' or i=='x++':
            x+=1
        elif i=='--x' or i=='x--':
            x-=1
    return x

print (lenguaje(['++x','x++']))



#%%

def suma(a,b):
    
    x=0
    for i in range(b):
        x+=a
    return x 
    
    
    
print(suma(2,3))


    
    
#%%    
def suma(a,b):
   i=0
   x=0
   while i<b:
       i+=1
       x+=a
   return f'el resultado es {x}'



print(suma(2,3))


#%%

def joyas(piedras:str):
    joyas='aeiou'
    contador=0
    for i in piedras:
        if i in joyas:
            contador+=1
    return contador

print(joyas('abchfopemik'))





























