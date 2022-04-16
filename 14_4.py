#%%CADENAS 
#%% 1)
#Corrija este código para que imprima la longitud de un string:
print(len("Esto es un texto"))

#%% 2) 
#Escribir una función que cuente la cantidad de letras A que se encuentran en
#una palabra. Complete el siguiente código:
    
def count_A():
    palabra = str(input('ingresa una palabra'))
    count = 0
    for i in palabra:
        if i == 'a' or i == 'A':
            count+=1
    print (f'hay {count} a en {palabra}')

count_A()

#%% 3) 
#Escriba una función count(s, character) que cuente cuántas veces aparece el 
#carácter character en la cadena s. Complete el siguiente código:
    
    
def count(palabra, character) :
     count = 0
     for i in palabra:
         if i == character:
             count +=1

     print (f'hay {count} {character} en {palabra}')
    
    
count ('anana','a')

count ('supercalifragilístico','a')

#%% 4)
#Escriba un programa que le pida al usuario un carácter y un texto y luego
# muestre la cantidad de ocurrencias del carácter en el texto ingresado. 

def cant_letra (letra,texto):
    contador_letra = 0
    for i in texto:
        if i == letra:
            contador_letra +=1
    print (f'La cantidad de {letra} en el texto es {contador_letra}')

cant_letra ('a','podemos ingresar una cadena relativamente larga y contar la cantidad de ocurrencias de un carácter')
    
    
            
#%% 5) 
#Escriba un programa que le pida al usuario un texto y dos caracters e indique
#qué carácter tiene más ocurrencias. Por ejemplo, puede seguir la siguiente interfaz:
    
def contador (palabra,letra1,letra2):
    contador_letra1 = 0
    contador_letra2 = 0
    
    for i in palabra :
        if i == letra1:
            contador_letra1+=1
        elif i == letra2:
            contador_letra2 +=1
        
    if contador_letra1 < contador_letra2:
        print (f'hay mas "{letra2}" que "{letra1}" en {palabra}')   
    elif contador_letra1 == contador_letra2: 
        print (f'hay la misma cantidad de  "{letra2}" que "{letra1}" en {palabra}') 
        
    else:
        print (f'hay mas "{letra1}" que "{letra2}" en {palabra}') 
        

contador ('supercalifragilistico','a','l')
contador ('banana','a','n')
contador ('retroalimentacion','a','o')

    
#%% 6) 
# Escriba una función que tome una cadena de texto y retorne una nueva cadena
#formada por la letra inicial, la letra del medio, y la letra final, de la
#cadena inicial.

    
    
def shorten(palabra) -> str:
 
 palabra = list(palabra)
 primer_letra = palabra [0]
 letra_medio= palabra [len(palabra)//2]
 letra_final = palabra[-1]
 

 if len (palabra)==1:
     print("".join(primer_letra))
 elif len (palabra) ==2:
     print("".join(primer_letra),
               "".join (letra_medio))
 else: 
     print("".join(primer_letra),
           "".join (letra_medio),
           "".join (letra_final))
shorten ('p')
shorten ('pmz')
shorten ('code')
shorten ('haxor')

#%% 7)
#Escribir una función que dada una dirección IPv4 válida, devuelva una versión
#modificada de esa dirección IP, a esta versión modificada la llamaremos
#"IP con colmillos". Una dirección IP con colmillos reemplaza cada punto "." 
#de la dirección IP original con "[.]".

def colmillos (ip):
   palabra_final =''
   for i in ip:
       if i == '.':
           palabra_final += '[.]'
       else:
           palabra_final+= i
   return palabra_final          
print (colmillos('255.10.26'))


def colmillitos (ip): 
    ip = ip.replace ('.','[.]')
    return ip
print (colmillitos('255.10.26'))

def dientes (ip):
    ip = ip.split('.')
    return  '[.]'.join(ip)
print (dientes('255.10.26'))
    

#%% 8)
#Dada una cadena de caracteres que representa los tipos de piedras que son
#joyas, y otra cadena de caracteres que representa las piedras que tienes,
#quieres saber cuántas joyas tienes, es decir, cuántas de las piedras que 
#tienes son también joyas.

def joyas ():
    joyas = 'AaEeIiOoUu'
    piedras=str(input('ingrese las piedras que tiene'))
    count =0
    for i in piedras:
        if i in joyas:
            count+=1
    print(f'hay {count} joyas en {piedras}')
    print ('hay',count,'joyas en',piedras)

joyas ()
    
 
#%% 9)
# una función que retorne True si un password (string) cumple con los siguientes
#requisitos:
#Tiene que tener por lo menos una letra minúscula.
#Tiene que tener por lo menos una letra mayúscula.
#Tiene que tener por lo menos un número.
#Tiene que tener por lo menos un signo no alfanumérico (p.ej. ! ó $).
#Tiene que tener entre 8 y 31 caracteres.
def condiciones(contraseña,i):
    return  i.islower() or i.isupper() or i.isdigit() or i.isalpha()
def password():
    contraseña = input('ingresa una contraseña')
    largo = len(contraseña)
    
    if largo>8 and largo<31:
        for i in contraseña: 
            while condiciones:
                contraseña = True
        contraseña = False
        return contraseña
            
    else:
       print ('no cumple con la cantidad')
    
def validar (contraseña):
    if contraseña == True:
        print ('la contraseña es válida')
    else:
        print ('la contraseña no es válida')
    
validar(password())

        
#%%10) modo prueba
#Escribir una función que reciba una cadena, representando una fecha en formato
#AAAA-MM-DD, y retorne un True si esa fecha corresponde a Sagitario, el signo 
#del zodiaco. Sagitario es entre el 22 de noviembre y el 21 de diciembre
#
def signo ():
    fecha ='DD/MM/AAAA'
    print (f'ingrese una fecha {fecha}')
    dia = int(input('ingrese un dia'))
    mes = int(input('ingrese un mes'))
    año= int(input('ingrese un año'))
    dia_us=str(dia)
    mes_us=str(mes)
    año_us=str(año)
   
    if len(dia_us)<=2 and len(mes_us)<=2 and len(año_us)<=4:
            if mes==11 and dia>=22 or mes==12 and dia<=21:
                print ('es de sagitario')
            else:
                print ('no es de sagitario')
    else :
        print('ingrese una fecha correcta')

signo()



#%% 10) modo serio
#Escribir una función que reciba una cadena, representando una fecha en formato
#AAAA-MM-DD, y retorne un True si esa fecha corresponde a Sagitario, el signo 
#del zodiaco. Sagitario es entre el 22 de noviembre y el 21 de diciembre
#

def sagitario (fecha):
    print(f'si nació el {fecha} entonces :')
    fecha = fecha.split('/')
    fecha=list(fecha)
    mes = int(fecha[1])
    dia = int(fecha[2])
    if mes==11 and dia>=22 or mes==12 and dia<=21:
        print ('es de sagitario')
    else:
        print ('no es de sagitario')
    
sagitario('2033/5/16')
sagitario('2033/11/16')
sagitario('2033/11/25')


#%% 11) random 
import random 
rango= range (1,10)
transformacion= random.choice(rango)
def cifrado (transformacion):
    entrada= str(input('ingrese la palabra a transformar'))
    mensaje = entrada.lower()
    mensaje_nuevo=[]
    for letra in mensaje:
           letra_ASCII= ord(letra)
           encriptado= (letra_ASCII +transformacion -97 ) % 26 +97
           letra_encriptada = chr(encriptado)
           mensaje_nuevo.append(letra_encriptada)
    mensaje_new=''.join(mensaje_nuevo)
    print (mensaje_new)
    return mensaje_new 
    

def descifrado (mensaje_new):
    mensaje_final=[]
    for letra in mensaje_new:
        letra_ASCII= ord(letra)
        desencriptado= (letra_ASCII - transformacion -97)%26 +97
        letra_desencriptada = chr(desencriptado)
        mensaje_final.append(letra_desencriptada)
    print (''.join(mensaje_final))

descifrado(cifrado(transformacion))

#%% 12) ****terminar****
#Escribir una función que permita determinar si una cadena podría formar una 
#palabra, del siguiente modo: el carácter "?" sirve de comodín para cualquier 
#letra, mientras que sea 1 (una) letra, por lo que "*oca" puede formar la 
#palabra "poca", también la palabra "boca", o "roca". La palabra "?" puede
#formar cualquier cadena de largo 1, mientras que "?o?a" puede formar "poca", 
#"bota", "rosa", etc.



def matches(palabra,secreto):
    if len(palabra)== len(secreto): 
       for letra in secreto :
                posicion_signo= secreto.index('?')
       for i in palabra:
           letra_si=palabra[posicion_signo]
       secreto =secreto.replace('?',letra_si)
       print (secreto)
       for letra in secreto:
            for i in palabra:
                if letra==i:
                    return True
    else:
        return f'{palabra} y {secreto} no tienen la misma longitud.'
                
    
print (matches('cosa','?l?t')) 
    

#%% LISTAS 
#%% 1)
#Programar una función que tome una lista de números y compute la suma de
#todos los números en la lista.

def suma_list():
    lista= list(range(11))
    suma=0
    for i in lista: 
      suma+=i
    return suma
print (suma_list())

#%% 2)
#Programar una función que elimine todas las ocurrencias de un cierto elemento
#en una lista.

def eliminar ():
    elemento ='a'
    lista=['a','b','a','c','z','A','F']
    for i in lista:
        if elemento in lista:
            posicion=lista.index(elemento)
            del lista[posicion]
    print (lista)

eliminar()


#%% 3)Modo 1
#Programar una función que tome una lista y elimine todos los elementos 
#duplicados.

def eliminar ():
    lista = [1,3,8,8,'v',3,2]
    lista_new = []
    print (lista)
    for i in lista:
        if i not in lista_new:
            lista_new.append(i)
    return lista_new
print (eliminar())

#%% 3)Modo 2
#Programar una función que tome una lista y elimine todos los elementos 
#duplicados.

def eliminar ():
    lista = [2,1,5,6,3,3,2,4]
    print (lista)
    lista= list(set(lista))
    print (lista)

eliminar ()

#%% 4) 
#Programar una función que tome dos listas y retorne True si las listas tienen
#por lo menos un elemento en común.

def igualdad ():
    lista1 = [1,5,3,6]
    lista2 = [7,8,6,5] 
    for i1 in lista1:
        for i2 in lista2:
            if i1==i2:
                return True
def check (esta):
    if esta == True:
        print ('Las listas tienen en comun al menos un elemento')
    else :
        print ('Las listas no tienen en comun ningun elemento')
        
check(igualdad())
#%% 5)
#Programar una función my_max que tome por argumento una lista con números 
#(int o float) y retorne el número máximo.

def my_max(lista):
    numero_max=max(lista)
    print (numero_max)
    
my_max([1,5,2,3,6,9,4,2])

#%% 6)
#Hay un lenguaje de programación con sólo cuatro operaciones y una variable, x
# definido por los siguientes items:
#Inicialmente, el valor de x siempre es 0.
#++x y x++ incrementa el valor de la variable x en 1.
#--x y x-- decrementa el valor de la variable x en 1.


def operaciones (lista):
    x=0
    for i in lista:
        if i =='--x' or i =='x--':
            x-=1
        elif i== '++x' or i == 'x++':
            x+=1
        
    print (x)
operaciones ([] )
operaciones (["++x"] )
operaciones (["--x"] )
operaciones (["--x", "x++"] )
operaciones (["++x", "x++"]  )
operaciones (["++x", "x++", "x--"])

#%% 7)
#Programar una función llamada terminan_en_vocal que tome por argumento una
#lista de strings, y devuelva otra lista con los strings que terminan en vocal.
#Pueden probar la función con las palabras que surgen de aplicar la función 
#split al preámbulo de la Constitución Nacional.


def terminan_en_vocal(lista_str):
    vocales = 'aeiou'
    palabras_terminan_vocal = []
    for palabra in lista_str:
        if palabra[-1]in vocales:
           palabras_terminan_vocal.append(palabra)
    return palabras_terminan_vocal

print (terminan_en_vocal(['casa','miramar','juanito','casa','mar','olla']) )
                
    
#%% 8) ****terminar****     
# Programar una función que tome como argumento un párrafo (un string con 
#muchas palabras), y retorne una lista indicando la frecuencia con la que 
#ocurren palabras de distinta longitud (la estructura de la lista a retornar
#queda a criterio del diseñador, pero debe ser explicada claramente en el 
#docstring). Es decir, la función debe computar cuantas palabras de largo 1 hay
# en el párrafo, cuantas de largo 2, y así sucesivamente hasta la longitud más 
#larga que tenga el párrafo.

def frecuencia_long (parrafo):
    
    parrafo = list (parrafo.split(' '))
    contador_long2=0
    contador_long1=0
    contador_long3=0
    contador_long4=0
    contador_long5=0
    contador_long6=0
    contador_long7=0
    contador_long8=0
    contador_long9=0
    contador_long10=0
    for palabra in parrafo:
        largo = len(palabra)
        if largo== 2:
            contador_long2+=1
        elif largo== 1:
            contador_long1+=1
        elif largo== 3:
            contador_long3+=1
        elif largo== 4:
            contador_long4+=1
        elif largo== 5:
            contador_long5+=1
        elif largo== 6:
            contador_long6+=1
        elif largo== 7:
            contador_long7+=1
        elif largo== 8:
            contador_long8+=1
        elif largo== 9:
            contador_long9+=1
        elif largo== 10:
            contador_long10+=1
            
        
        
    print ( f'hay {contador_long2} palabras de 1')
    print ( f'hay {contador_long1} palabras de {largo}')
    print ( f'hay {contador_long3} palabras de {largo}')
    print ( f'hay {contador_long4} palabras de {largo}')
    print ( f'hay {contador_long5} palabras de {largo}')
    print ( f'hay {contador_long6} palabras de {largo}')
    print ( f'hay {contador_long7} palabras de {largo}')
    print ( f'hay {contador_long8} palabras de {largo}')
    print ( f'hay {contador_long9} palabras de {largo}')
    print ( f'hay {contador_long10} palabras de {largo}')
    
    


frecuencia_long('hola gente como andan , espero que bien ')


#%% 9) 
#Escribir una función que reciba una lista de listas y elimine todas las listas
#cuyo 3er elemento sea mayor a un número dado. 

def eliminar_3 (listas):
    numero = 28
    lista_new = []
    for mini_lista in listas:
        if mini_lista[2]< numero:
            lista_new.append (mini_lista)   
    return lista_new

print (eliminar_3( [["W", 5, 31], ["U", 7, 18], ["F",
11, 15], ["B", 16, 28]]))
            


#%% 10) a)
#Escribir una función que recibe una lista de al menos 3 elementos y retorna
#True si el segundo es mayor al tercero y la suma de estos dos es mayor 20.

def filtrado (lista):
    if len(lista)>=3:
            if lista[1]>lista[2] and lista[1]+lista[2]==20:
                return True
            else:
                return f'la lista {lista} no cumple las condiciones'

print (filtrado([5,11,9,6,5]))
print (filtrado([5,3,5,6,5]))

#%% 10) b) 
#Escribir una función llamada filtrar que recibe una lista L y una función f
#y retorne una lista con aquellos elementos de L que al aplicarles f
#(al ejecutar f con cada uno de ellos como argumento, individualmente) 
#devuelven True
   

        

def eliminar_3 (lista):
    numero = 28
    for mini_lista in lista:
        if mini_lista[2] < numero:
            filtrar(mini_lista)
        return filtrar(mini_lista)
def filtrar (mini_lista):
    lista_new = []
    lista_new.append(mini_lista)


print(filtrar(eliminar_3([["W", 5, 31], ["U", 7, 18], ["F",11, 15], ["B", 16, 28]])))


#%% TUPLAS
#%% 1) 
# Escribir una función que reciba una fecha en formato AAAA-MM-DD y retorne un
# tupla de 3 enteros con la fecha. En el formato AAAA-MM-DD, AAAA representa 
# el año con 4 dígitos, MM el mes con 2 dígitos, yDD el día con 2 dígitos.


def fecha (fecha):
     fecha = fecha.split('/')
     list(fecha)
     print (fecha)
     lista = []
     for i in fecha:
                 lista.append(int(i))
     
    
     tupla = tuple(lista)
     return tupla
   
    
print (fecha('2022/5/15'))
print (fecha('22/5/59'))
print (fecha('2022/5/15'))
print (fecha('2022/5/15'))

#%% 2)
# Escribir una función que reciba una lista de tuplas, donde cada tupla 
#contiene un nombre y una fecha(la fecha puede ser una tupla o una cadena en 
#formato AAAA-MM-DD, a elección de quien programa la función). La función debe
#retornar True si todas las personas son de sagitario. Considere el caso
#particular en que la lista contenga 8 tuplas, los primeros 6 nombres sean 
#"Gachi", "Pachi", "Lorena", "novio", "exnovio" y "Andrea", y sean todos de 
#sagitario, en cuyo caso debe imprimirse un mensaje acorde, además de retornar
#el correspondiente True



def sagitario (lista):
    
    for i in lista:
        i=list(i)
        dia = i[3]
        mes = i[2]
        nombre = i[0]
        if mes==11 and dia>=22 or mes==12 and dia<=21:
            print (f'{nombre} es de sagitario')
           
    return True 
            
sagitario([('gachi',2022,11,25),('pachi',2452,11,30),
           ('Lorena',2022,11,22),('novio',2022,12,3),
           ('exnovio',2022,12,5),('Andrea',2022,12,21),
           ('gachi',2022,5,3),('gachi',2022,5,4)])        
    
    











#%%

f= 'la mar estaba serena '
i=0

while i<len(f):
    f[i]='e'
    i+=1

print (f)