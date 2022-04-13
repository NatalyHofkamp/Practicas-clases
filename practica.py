# -*- coding: utf-8 -*-

i=1

while i<10000 and not(i%5==0 and i%7==0):
    i=i+1

if i==10000 :
    print('no existe')

else:
    
    print('existe y es', i)
    
   #%%
   
i=1

while i<25 :
    i=i+1
    
print (i)
   
#%%

import math 

print(math.sqrt(144))

#%%

i=1
j=0
z= i<100 and j>8
soluciones=[]

while i<100 and j>8:
    if z:
        soluciones.append(i)
        j=j+1
        i=i+1
        print (soluciones)
#%%
import math
numero =int(input('ingrese un número'))

while numero<0:
    print('ERROR -> ingrese un numero positivo')
  
    numero =int(input('ingrese un número'))
    


print(f"\n Su raiz cuadrada es :{(math.sqrt(numero)):.2f}")

#%%

i=0 

while i<20:
    print(i)
    i+=1

#%% tipos de variables 
##  variables globales
name='john'

def fun1 ():
    print (name)
    
def greet (name:str) -> str:
    return f'hello,{name}'
    
def main ():
    ## variables locales
    name= 'Mike'
    print (greet(name))

if __name__=='__main__':
    main()


#%%  Area or Perimeter 

def calc_rect_square(): 
    length= int(input('ingrese la altura '))
    width= int(input('ingrese el ancho '))
    rect_perimeter= length*2 +2*width 
    area_square= width**2

   
    if length== width:
        return( area_square)
    
    else:
        return (rect_perimeter)
print(calc_rect_square())
#%%
num_1=len (input('ingrese un número'))

num_2= len (input('ingrese otro número '))
 
print (num_1+num_2 )
   
#%% DOT CALCULATOR 

def calculator():
    num_1=len (input('ingrese un número'))

    num_2= len (input('ingrese otro número '))
    
    operaciones=['suma','resta','multiplicacion','division']
    
    print ('De las siguientes operaciones: ')
    for i,operacion in enumerate (operaciones,1):
        print (f'{i}. {operacion}')
        
    choice = int (input('¿cual desea realizar?'))
    
    if choice== 1:
        print (num_1 + num_2)
    elif choice== 2:
        print (num_1-num_2)
    elif choice==3 :
        print (num_1*num_2)
    elif choice ==4:
        if num_2==0:
            print ('no se puede dividir por cero')
        else:
            print (num_1/num_2)

calculator()



#%%escriba un programa que juegue al piedra, papel o tijera contra el humano.
import random

opciones = ['piedra','papel','tijera']
print('Elija entre:')
for i,opcion in enumerate(opciones,1):
    print (f'{i}. {opcion}')
eleccion = int(input())
random_elec = random.choice(opciones)

if eleccion ==1:
   eleccion = opciones[0]
   
elif eleccion == 2:  
   eleccion =  opciones[1]
   
elif eleccion == 3 :
    eleccion = opciones[1]
    
    return eleccion 
        
    
if eleccion ==random_elec:
    print ('debe elegir de nuevo')

elif eleccion== 1 and random_elec ==2:
    
    
    
    




































