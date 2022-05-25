#%% 1) --> sort no es un método de diccionarios.
#%% 2) imprima en pantalla las claves de un diccionario.

dic = {'a':1,'b':2,'c':3}

dic_values = dic.keys()
for value in dic_values:
    print(value)

# %% 3) Imprima por pantalla los valores de un diccionario.

dic = {'a':1,'b':2,'c':3}

dic_values = dic.values()
for i in dic_values:
    print (i)

#%% 4)  Escriba una función que recibe un número y devuelve un diccionario cuyas claves son desde el
#número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.


def diccionario (n):
    dict= {}
    claves= list(range(1,n+1))
    for i in claves:
        dict[i]= i*i
    return dict

print(diccionario(10))

#%% 5) Escriba una función que recibe una cadena y devuelve un diccionario con la cantidad de
#apariciones de cada carácter en la cadena.

def apariciones (cadena):
    dict={}
    for letra in cadena:
        if letra in dict:
            dict[letra]+=1
        else:
            dict[letra]=1
    return dict

print(apariciones('hola, cómo estas?'))


#%% 6)Escribir un programa que guarde el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} en
#una variable, pregunte al usuario por una divisa y muestre su símbolo por pantalla, o un mensaje de
#aviso si la divisa no está en el diccionario.

def divisa ():
    divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    eleccion = input('qué divisa querés?')

    print (divisa[eleccion])

divisa()


#%% 7) Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
#claves sea el primer elemento de la tupla y el valor el segundo, asumir que nunca estarán repetidas las
#claves.

def diccionario_tuplas (lista):
    dict ={}
    for clave,valor in lista:
        dict[clave]=valor
    print(dict)
        


diccionario_tuplas([('a',1),('b',2),('c',3)])
# %% 8) Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las
#claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
def diccionario_tuplas(lista):
    dict ={}
    for clave,valor in lista:
        if clave in dict:
            dict[clave].append(valor)
        else:
            dict[clave] = [valor]
    
    print (dict)

diccionario_tuplas([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días') ]
)


#%% 9)  Escribir una función que reciba la cantidad de iteraciones a realizar de una tirada de 2 dados y
#devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
import random
def frecuencia_de_tiradas (n):
    dict ={}
    i=0
    while i <n:
        dado1 =random.choice(range(1,7))
        dado2 = random.choice(range(1,7))
        suma= dado1+dado2
        if suma in dict:
            dict[suma]+=1
        else:
            dict[suma]=1
        i+=1
    return dict

print(frecuencia_de_tiradas(9))
        
#%% 10) ☆ Implementamos una agenda con un diccionario
#*Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente

def agenda ():
    dic={'clara':1176985263,'martin':1178956482,'jose':1146598752}     
    while True:
        q = input('desea trabajar con la agenda? si/no')
        if q =='si':
            opcion= input ('ingrese el nombre con el que quiere trabajar')
            if opcion in dic:
                print(dic[opcion])   
                pregunta= input('es correcto? si/no')
                if pregunta == 'si':
                    return 'joya, nos vemos!'
                else:
                    new_value=input('ingrese el nuevo número')
                    dic[opcion]= new_value
                    print('joya, se guardo el nuevo número')
            elif opcion not in dic:
                pregunta = input(f'ingrese el número de {opcion}')
                dic[opcion]=pregunta
                print(f'joya, el número de{opcion} es {pregunta}')
        else:
            break

print(agenda())

#%% 11) Escribir un archivo llamado words.py que contenga una variable que sea una lista con palabras
#(strings). Escribir, luego, una función que lea las palabras en words.py y las almacene como valores en
#un diccionario. La clave a la que pertenece cada palabra es su propia longitud. Luego se pueden
#recuperar rápidamente todas las palabras de una determinada longitud.
def palabras_longitud(longitud):
    a= ['hola casa taza pasa masa cama pala jazmin maceta pelotero ojota mancha manija puerta cerradura']
    dic ={}
    for palabra in a:
        palabra = palabra.split(' ')
        for word in palabra:
            long= len(word)
            if long in dic:
                dic[long].append(word)
            else:
                dic[long] =[word]
    palabras = ', '.join(dic[longitud])        
    print(f'las palabras de longitud {longitud} son : {palabras}.')

palabras_longitud(4)

#%% 12) Lea que es un bit de paridad [https://en.wikipedia.org/wiki/Parity_bit] y cree una función que
#reciba una lista de strings con 7 bits y devuelva un diccionario donde estos strings sean las claves y el
#parity bit el valor.


def parity_bit(lista):
    dic = {}
    for bit in lista:
        cantidad =0
        for numero in bit:
            if int(numero) == 1:
                cantidad+=1
        if cantidad %2==0:
            uno = 0
        else:
            uno = 1
        if bit not in dic:
            dic[bit]=uno
    return dic  
print(parity_bit(["0110100","1011010",'0111000']))






















    


# %%
