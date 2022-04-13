def enlistar (ip):
    ip = ip.replace (',','[.]')#solamente es útl para string
    return ip
print  (enlistar('222.558.226.333'))
            

def otramanera(ip):
    result = ''
    
    for letra in ip:
        if letra == '.':
            result +='[.]'
        else:
            result+= letra
    return result

def other (ip):
    ip = ip.split('.')
    
    return '[.]'.join(ip) #listas -> se agrega en medio de cada elemento

#%% joyas forma 1

def joyas():
    joyas= 'AaEeIiOoUu'
    piedra= str(input('ingrese las piedras'))
    piedras=[]
    for letra in piedra:
        if letra in joyas:
            piedras.append(letra)
            cant_piedras= len(piedras)
    return f'Hay {cant_piedras} joias'


print (joyas())


#%% joyas forma 2
def joyas():
    joyas= 'AaEeIiOoUu'
    piedra= str(input('ingrese las piedras'))
    count = 0
    for letra in piedra:
        if letra in joyas:
            count +=1
    return f'Hay {count} joias'


print (joyas())


#%%
#ord()#convierte una letra a ASCII
#chr()#convierte el valor en ASCII a número o letra

def cifrado ():
    entrada= str(input('ingrese la palabra a transformar'))
    mensaje = entrada.lower()
    mensaje_nuevo=[]
    for letra in mensaje:
           letra_ASCII= ord(letra)
           encriptado= (letra_ASCII +2 -97 ) % 26 +97
           letra_encriptada = chr(encriptado)
           mensaje_nuevo.append(letra_encriptada)
    mensaje_new=''.join(mensaje_nuevo)
    print (mensaje_new)
    return  mensaje_new

def descifrado (mensaje_new):
    mensaje_final=[]
    for letra in mensaje_new:
        letra_ASCII= ord(letra)
        desencriptado= (letra_ASCII -2 -97)%26 +97
        letra_desencriptada = chr(desencriptado)
        mensaje_final.append(letra_desencriptada)
    print (''.join(mensaje_final))

descifrado(cifrado())



#%%











