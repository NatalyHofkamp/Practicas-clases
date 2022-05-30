#%% 1) Escriba una función, llamada less, que reciba un archivo e imprima el contenido del archivo.
def less(filename):
    with open (filename,'r') as f:
        l = f.readline()
        while l:
            print(l)
            l = f.readline()
less('words.txt')
# %% 2)Escriba una función, llamada head, que reciba un archivo y un número N e imprima las
#primeras N líneas del archivo

def head(filename,n):
    with open(filename,'r') as f:
        l= f.readline()
        x=0
        while x<n:
            print(l)
            l =f.readline()
            x+=1

head('words.txt',2)

# %% 3) Escriba una función, llamada tail, que reciba un archivo y un número N e imprima las últimas
#N líneas del archivo

def tail(filename,n):
    with open(filename,'r') as f:
        l=f.readlines()
        for i in range(n+1,0,-1):
            print(l[-i])

tail('words.txt',2)

# %% 4) Escribir una función, llamada touch, que reciba el nombre del archivo a guardar, y genere una
#archivo de texto vacío.

def touch (filename):
    with open(filename,'w') as f:
        f.write('holis')

touch ('filename')

#%% 5)  Escribir una función, llamada cp, que copie todo el contenido de un archivo a otro, de modo
#que quede exactamente igual.

def cp(archivo1,archivo2):
    with open(archivo1,'r') as f:
        l=f.readlines()
    with open(archivo2,'w') as x:
        l=' '.join(l)
        x.write(l)

cp('words.txt','words_copiado')


# %% 6) Escribir una función, llamada wc, que dado un archivo de texto, lo procese e imprima por
#pantalla cuántas líneas, cuántas palabras, cuántos caracteres contiene el archivo, y el nombre del
#archivo.


def wc(filename):
    with open (filename,'r') as f:
        lineas = 0
        caracteres = 0
        palabras= 0
        for linea in f:
            lineas+=1
            largo = len(linea)
            caracteres+=largo
            linea= linea.strip().split(' ')
            palabras+= len(linea)
    print(lineas,palabras,caracteres,filename)
wc('words.txt')

#%% 7)Escribir una función, llamada grep, que reciba una cadena y un archivo, e imprima las líneas
#del archivo que contienen esa cadena.


def grep(cadena,archivo):
    with open (archivo,'r') as f :
        for linea in f:
            if cadena in linea:
                print(linea)
    
grep('taza','words.txt')

#%% 8) Escribir una función, llamada cat, que reciba dos cadenas referidas a los nombres de dos
#archivos, y guarde en un tercer archivo el contenido de los dos archivos.

def cat(archivo1,archivo2,archivo3):
    with open(archivo1,'r') as f:
        contenido1 = ''.join (f.readlines())
    with open(archivo2,'r') as h:
        contenido2 = ''.join (h.readlines())
    with open(archivo3,'w') as j:
        j.write(contenido1)
        j.write(contenido2)

cat('words.txt','filename.txt','mantequilla')

#%% 9) Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de
#destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo
#destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y
#la z (del alfabeto inglés), se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
#caracter

def rot13 (origen,destino):
    with open(origen,'r') as origin:
        new_words= []
        for linea in origin:
            linea = linea.strip().split(' ')
            for palabra in linea:
                new_word = []
                for letra in palabra:
                      encriptado= (ord(letra) +2 -97 ) % 26 +97
                      letra_encriptada = chr(encriptado)
                      print(letra_encriptada)
                      new_word.append(letra_encriptada)
                new_word=''.join(new_word)
                new_words.append(new_word)
        new_words = '\n'.join(new_words)

    with open(destino,'w') as destiny:
        destiny.write(new_words)


rot13('words.txt','destiny')

#%% 10) Escribir una función load_data que reciba un nombre de archivo, cuyo contenido tiene el
#formato key:value, y devuelva un diccionario con el primer campo como clave y el segundo como
#diccionario.

def load_data (archivo):
    with open(archivo,'r') as f:
        l=f.readline()
        dic={}
        while l:
            key= l.split(':')[0]
            value = l.strip().split(':')[1]
            dic[key]=value
            l=f.readline()
    print(dic)
load_data('load_data.txt')

#%% 11) Escribir una función save_data que reciba un diccionario y un nombre de archivo, y guarde el
#contenido del diccionario en el archivo, con el formato key:value.

def save_data (dict,archivo):
    with open(archivo,'w') as f:
        for key in dict:
            formato =[]
            formato.append(key)
            valor= dict[key]
            formato.append(valor)
            imprimir = ':'.join(formato)
            f.write(imprimir)
            f.write('\n')

save_data ({'nombre': ' nataly', 'apellido': ' hofkamp', 'edad': '19'},'save_data')

#%% 12)  Escribir una función, llamada sed, que reciba el nombre de un archivo, y dos cadenas. La
#primera cadena en el archivo es la que queremos reemplazar por la segunda.

def sed (archivo,cadena1,cadena2):
    with open(archivo,'r') as f:
        l=f.readlines()
        lista=[]
        for cadena in l:
            cadena= cadena.strip()
            print(cadena)
            lista.append(cadena)
        for i in lista:
            if i==cadena1:
                indice = lista.index(i)
                lista[indice] = cadena2
        lista='\n'.join(lista)
    with open(archivo,'w') as f:
        f.write(lista)

sed('words.txt','maceta pelotero ojota taza', 'esta es una linea cambiada')

#%% 13) Escribir una función que reciba la información que se quiere escribir en un archivo en formato CSV.
#Esta información tiene que estar estructurada en una secuencia de secuencias.

def csv(informacion):
    with open('texto2.txt','w') as f :
        for linea in informacion:
            new_linea= ','.join(linea)+'\n'
            f.write(new_linea)
    
csv( [
 ["First Name","Last Name","Country","Date of Birth"],
 ["Emanuel","Ginobili","Argentina","1977"],
 ["Donald","Trump","USA","1946"],
 ["Carl","Gauss","Germany","1855"]
]
)

#%% 14) Escribir una función que reciba la información que se quiere escribir en un archivo en formato TSV.
#Esta información tiene que estar estructurada en una secuencia de secuencias.

def tsv(informacion):
     with open('texto3.txt','w') as f :
        for linea in informacion:
            new_linea= '    '.join(linea)+'\n'
            f.write(new_linea)
    
tsv([
 ["First Name","Last Name","Country","Date of Birth"],
 ["Lewis","Hamilton","United Kingdom","1985"],
 ["Max","Verstappen","Belgium","1997"],
 ["Charles","Leclerc","Monaco","1997"]
]
)


#%% 15) TERMINAR
#1. Eliminar los nombres de los personajes.
#2. Eliminar lineas en blanco.
#3. Eliminar puntuaciones.
#4. Eliminar informacion adicional para los actores.
#5. Guardar el archivo con los cambios


def guion(archivo):
    with open(archivo,'r+') as f:
        new_list= []
        for linea in f:
            new_line=[]
            linea=linea.strip().split(' ')
            del linea [0]
            for palabra in linea:
                if '.' in palabra:
                    palabra=list(palabra)
                    del palabra[-1]
                    palabra=''.join(palabra)
                    new_line.append(palabra)
                if '('in palabra:
                    inicio=linea.index(palabra)
                    if ')' in palabra :
                        fin =linea.index(palabra)
                        i=0
                        if i in range((1+fin)-inicio):
                            del(linea[inicio])
                            i+=1
            print(linea)

guion('guion.txt')




#%% 16) Dado dos archivos en formato CSV, dinosaurs1.csv y dinosaurs2.csv, escribir un
#programa que lea los dos archivos guardados en disco, y luego imprima los nombres de los
#dinosaurios bípedos, desde el más lento al más rápido.

import math
def bipedos (archivo1,archivo2):
    g=9.8
    with open(archivo1,'r') as f:
        dic_length={}
        for l in f:
            l=l.strip().split(',')
            name=l[0]
            leg_length= l[1]
            dic_length[name]=leg_length
    with open(archivo2,'r') as h:
        bipedal = []
        dic_stride={}
        for l in h:
            l=l.strip().split(',')
            name=l[0]
            leg_stride= l[1]
            dic_stride[name]=leg_stride
            if l[-1] =='bipedal':
                bipedal.append(l[0])
    dinasours_velocity ={}
    for dinasour in bipedal:
        length = float(dic_length[dinasour])
        stride = float(dic_stride[dinasour])
        velocity = ((stride / length) - 1) * (length * g)** 0.5
        dinasours_velocity[dinasour] = velocity
    velocities = list(dinasours_velocity.values())
    velocities.sort()
    for i in velocities:
        for key,value in dinasours_velocity.items():
            if value == i:
                print(key)

bipedos('dinosaurs1.csv','dinosaurs2.csv')

# %% 17) TERMINAR 
# Dado un archivo en formato CSV, que contiene canciones (nombre, duración, artista), escribir
# un programa que lea el archivo e imprima por pantalla la lista con el siguiente formato.

def canciones(archivo):
    with open(archivo,'r') as f:











# %%
