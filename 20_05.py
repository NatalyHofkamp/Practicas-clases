def frecuencia (texto_archivo):
    with open (texto_archivo,'r') as f:
        palabras = {}
        l = f.readline()
        while l: 
            l = l.strip().split(' ')
            for palabra in l:
                if len(palabra)>=4 and palabra not in palabras:
                    palabras[palabra]=1
                elif palabra in palabras:
                        palabras[palabra]+=1
            l = f.readline()
                    
    valores = list(palabras.values())
    val_max = max(valores)
   
    for key,value in palabras.items():
        if value == val_max:
            return print(key)
                      
            
def main ():
    frecuencia ('texto_archivo.txt')
    
if __name__ == '__main__':
    main()
    