#%% 1) Corrija el siguiente programa defectuoso para que imprima la negación 
#de la variable lógica state

state = not True #agregué un not 
print(state)

#%% 2) Corrija este programa defectuoso que produce un error al intentar 
   #Ejecutarlo.

cake = True
if cake == True: #agregué un igual
 print("cake es True")
else:
 print("The cake is a lie")

#%% 3) Escriba una función que diga si un número es par o impar


def is_even(number: int) -> bool:
  if number%2==0:
      print (f'{number} es un número par')
  else:
      print (f'{number} es un número impar')
      
is_even (2)
is_even(5)
is_even(100)
is_even(145)

#%% 4) Escriba una función que dados dos números a y b compare estos números y 
#retorne otro número indicando el resultado de la comparación del siguiente modo:
#0, si a y b son iguales,
#negativo, si a es menor que b,
#positivo, si a es mayor que b.


def cmp_number(a: float, b: float) -> float:

    if a==b :
        print (0)
    elif a<b:
        print ('-1 ')
    else:
        print ('1')


cmp_number(2,5)

#%% 5)Escriba una función que pida un número x, luego pida otro y,
# y devuelva los dos números multiplicados y divididos.

def mult_div():    

    x=float(input('ingrese el primer número:'))
    y=float(input('ingrese el segundo número:'))

    z= x*y 
    print (f'El resultado de la multiplicación es {z}')
    if y!=0 :
        w=x*1/y
        print (f'El resultado de la división es {w}')
    elif y==0:
        print ('no se puede dividir por cero.')

mult_div()


#%% 7) Escriba una función que calcule y retorne las raíces de la ecuación: 
#ax² + bx + c = 0. Sólo debe resolver la ecuación para el caso en que el 
#discriminante es mayor que 0.

from math import sqrt

def calc_raices (a,b,c):
   # a=int(input('ingrese el valor de a'))
    #b=int(input('ingrese el valor de b '))
    #c= int (input('ingrese el valor de c'))
    discriminante=(b**2) -(4*a*c)
    print (f'su función es {a}x^2 + {b}x+{c}')
    raiz1 = (-b+sqrt(discriminante))*(1/(2*a))
    raiz2 = (-b-sqrt(discriminante))*(1/(2*a))
    if discriminante >0:
        print (f'Las raices de su función son {raiz1} y {raiz2}')
    else:
        print('su discriminante es negativo')
        

calc_raices(1,3,2)
        
#%% 8) Escribir un programa que dado un día del año (1 a 366) ingresado por
# el usuario, imprima el día de la semana que le corresponde.
# Debe asumir que el año comenzó, por ejemplo, un domingo. Por ejemplo:
#si se ingresa '5', imprime 'jueves', si se ingresa '10' imprime 'martes', 
#si se ingresa '294',imprime 'sabado'.





#idea que funciona

#def dia (): 
  #  lista= ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
   # num_dia= int(input('ingrese un dia'))

    #if num_dia >366 or num_dia<0:
     #   print ('este dia no existe')
    #else:
     #       for i in range (1,8):
      #          if (num_dia -i)%7==0:
       #             return lista[i-1]
#%%
def dia ():
    lista = ['Domingo', 'lunes','martes','miercoles','jueves','viernes','sabado']
    dia_us = int(input('ingrese un dia del año'))
    resto = dia_us%7
    indice = resto -1
    print (lista[indice])
dia()

#%%******************************************************************************

domingo=[]
lunes=[]
martes=[]
miercoles=[]
jueves=[]
viernes=[]
sabado=[]

año=[]

for d in range (1,366,7):
    d='Domingo'
    domingo.append(d)
for l in range (2,366,7):
    l='Lunes'
    lunes.append(l)

for m in range (3,366,7):
    m='martes'
    martes.append(m)
    
for x in range (4,366,7):
    x='miercoles'
    miercoles.append(x)
    
for j in range (5,366,7):
    j='jueves'
    jueves.append(j)

for v in range (6,366,7):
    v='viernes'
    viernes.append(v)

for s in range (7,366,7):
    s='sabado'
    sabado.append(s)



for d,l,m,x,j,v,s in zip(domingo,
                          lunes,
                          martes,
                          miercoles,
                          jueves,
                          viernes,
                          sabado):
    año.append((d,l,m,x,j,v,s))


#dia =input('ingrese un número del año')

print (año[5])

#%% 9)Escribir una función que dadas dos rectas definidas por su pendiente y 
#su ordenada al origen devuelva la abcisa en la que se intersectan. Validar 
#lo que considere necesario.

def interseccion (m1,b1,m2,b2):
  
    recta_1= (f' f(x)={m1}x + {b1}')
    recta_2= (f'  g(x)={m2}x + {b2}')
    
    print (f'la interesección entre las rectas {recta_1} y {recta_2}  es :')
    r_pendientes= m1-m2
    r_ord= b2-b1
    
    x= r_ord/r_pendientes
    
    print (x)



interseccion(2,4,5,6)

interseccion(3,4,8,6)

#%% 10)a)


def bisiesto ():
    bisiesto ='es un año bisiesto'
    not_bisiesto='no es un año bisiesto'
    año =int(input('ingrese un año'))
    if   año%4==0 and (año%400==0 or not año%100==0):
        print (bisiesto)
        return (mes_año(True))
        
    else:
        print (not_bisiesto)
        return (mes_año(False))

def mes_año(esBisiesto):
    mes= int(input('ingrese un mes del año'))
    if esBisiesto :
        año_bisiesto=[31,29,31,30,31,30,31,31,30,31,30,31]
        dia_mes_bisiesto= año_bisiesto[mes-1]       
        return dia_mes_bisiesto
    else:
        año_no_bisiesto=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia_mes_nobisiesto=año_no_bisiesto[mes-1]
        return dia_mes_nobisiesto
    

#%%Dada una fecha (día, mes, año), indicar si es válida o no.
def bisiesto (año,mes):
    bisiesto ='es un año bisiesto'
    not_bisiesto='no es un año bisiesto'
    if   año%4==0 and (año%400==0 or not año%100==0):
        print (bisiesto)
        return mes_año(True,mes)
        
    else:
        print (not_bisiesto)
        return mes_año(False,mes)

def mes_año(esBisiesto,mes):
    if esBisiesto :
        año_bisiesto=[31,29,31,30,31,30,31,31,30,31,30,31]
        dia_mes_bisiesto= año_bisiesto[mes-1]       
        return dia_mes_bisiesto
    else:
        año_no_bisiesto=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia_mes_nobisiesto=año_no_bisiesto[mes-1]
        return dia_mes_nobisiesto

def dia_año(dia,mes,año):
    
    if dia <=bisiesto(año,mes):
        print ('la fecha es válida')
    else: 
        print('la fecha no es válida')
        
dia = int(input('ingrese el dia'))
mes=int(input('ingrese el mes'))
año = int(input('ingrese el año'))

dia_año(dia,mes,año)
#%%Dada una fecha, indicar los días que faltan hasta fin de mes


def bisiesto (año,mes):
    bisiesto ='es un año bisiesto'
    not_bisiesto='no es un año bisiesto'
    if   año%4==0 and (año%400==0 or not año%100==0):
        print (bisiesto)
        return mes_año(True,mes)
        
    else:
        print (not_bisiesto)
        return mes_año(False,mes)

def mes_año(esBisiesto,mes):
    if esBisiesto :
        año_bisiesto=[31,29,31,30,31,30,31,31,30,31,30,31]
        dia_mes_bisiesto= año_bisiesto[mes-1]       
        return dia_mes_bisiesto
    else:
        año_no_bisiesto=[31,28,31,30,31,30,31,31,30,31,30,31]
        dia_mes_no_bisiesto=año_no_bisiesto[mes-1]
        return dia_mes_no_bisiesto

def dia_año(dia,mes,año,dia_mes_bisiesto,dia_mes_no_bisiesto,esBisiesto):
    
    while dia <=bisiesto(año,mes):
        dias_faltan_bis = abs (dia_mes_bisiesto - dia)
        dias_faltan_no_bis = abs (dia_mes_no_bisiesto - dia)
        if esBisiesto:
            print (f'Faltan {dias_faltan_bis} para fin de mes')
        else:
            print (f'Faltan {dias_faltan_no_bis} para fin de mes')
         
    print('la fecha no es válida')
        
dia = int(input('ingrese el dia'))
mes=int(input('ingrese el mes'))
año = int(input('ingrese el año'))

dia_año(dia,mes,año)



#%%
import time
counter = 0
while True:
 counter += 1
 print("I'm Mr. Meeseeks, look at me", '!' * counter)
 time.sleep(1)


#%% Imprima en la consola de Python interactivo los números pares del 0 al 100.



for i in range (0,100,2):
    print (i)

#%%☆ Escriba una función que imprima en pantalla los múltiplos de, a la vez,
#7 y 23 (por ejemplo, 161 es múltiplo de ambos, 21 es múltiplo de 7 pero no de 
#23 y 46 es múltiplo de 23 pero no de 7)
#Escribir un programa que pida al usuario dos números A y B e imprima en la
#pantalla todos los números múltiplos de, a la vez, 7 y 23, en el intervalo [A, B).

def multiplos ():
    mul_7 = int(input('ingrese un número minimo'))
    mul_23 = int(input('ingrese un número máximo '))

    for i in range (mul_7,mul_23):
        if i%7==0 and i%23==0 :
            print(i)

multiplos()

#%% Escribir un programa que pida al usuario cuatro números A, B, C, y D e
#imprima en la pantalla todos los números múltiplos de, a la vez, C y D,
#en el intervalo [A, B).


def multiplos ():
    A = int(input('ingrese un número minimo'))
    B = int(input('ingrese un número máximo '))
    C = int(input('ingrese un numero '))
    D = int (input('ingrese otro numero'))
    for i in range (A,B):
        if i%C==0 and i%D==0 :
            print(i)

multiplos()

#%%  Escriba una función que devuelva el producto entre dos números haciendo
#una suma repetida



def multiplicar(num,cant_sum):
    if cant_sum==0:
        return 0
    elif cant_sum ==1:
        return num
    elif cant_sum>1:
        return num + multiplicar(num,cant_sum-1)
    
num=int(input('ingrese un numero'))
cant_sum=int(input('ingrese otro numero'))
print (multiplicar(num,cant_sum))
    
    
    
























