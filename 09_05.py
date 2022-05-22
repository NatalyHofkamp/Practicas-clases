#%% 1) Imprime en consola algo de un archivo de texto.
def less (texto_prueba):
    with open (texto_prueba,'r') as f:
        for line in f:
            print(line)
def main ():
    less('texto_prueba.txt')
    
if __name__ == '__main__':
    main()
    
    
#%% 2) Recibe un archivo y un numero de lineas.

def head (filename,num_line):
    with open (filename,'r') as f:
        for i in range (num_line):
            print(f.readline())
            
def main ():
    head('texto_prueba.txt',3)
    
if __name__ == '__main__':
    main()
    
    
#%% 3.1) Recibe un archivo y devuelve las ultimas tantas lineas que se piden.

def tail (filename, num_lines):
    with open (filename,'r') as f:
        lista = f.readlines()
        for i in range (num_lines,0,-1):
            print (lista[-i])
                     
def main ():
    tail('texto_prueba.txt',3)
    
if __name__ == '__main__':
    main()
    
    
#%% 3.2) Recibe un archivo y devuelve las ultimas tantas lineas que se piden.

def tail (filename, num_lines):
    with open (filename,'r') as f:
        lista = f.readlines()
        lista2 = lista[-num_lines:]
        lista2 = "".join(lista2)
        print (lista2)
        
                     
def main ():
    tail('texto_prueba.txt',3)
    
if __name__ == '__main__':
    main()
    
    
#%% crear archivo vacio


def touch(filename):
    with open (filename,'w') as f :
        f.write ('Hola, como estas?')
        
def main ():
    touch('some_text.txt')

if __name__ == '__main__':
    main()


































