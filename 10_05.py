#%% consola
f = open('texto_listas.txt','r')
edades = []
l = f.readline()
while l:
    edad = int(l.split(',')[1])
    edades.append(edad)
    l = f.readline()
    
print(edades)

promedio_edades = sum(edades)// len(edades)
print (promedio_edades)

#%% edades de las personas en cada provincia 

f = open('texto_listas.txt','r')
personas= {}
l = f.readline()
while l:
    prov = l.strip().split(',')[-1]
    edad = int(l.split(',')[1])
    if prov in personas:
        personas[prov].append(edad)
    else:
        personas[prov]=[edad]
    l = f.readline()
  
print(personas)

#%% promedio de las edades de cada provincia
f = open('texto_listas.txt','r')
personas= {}
l = f.readline()
while l:
    prov = l.strip().split(',')[-1]
    edad = int(l.split(',')[1])
    if prov in personas:
        personas[prov].append(edad)
    else:
        personas[prov]=[edad]
    l = f.readline()
    
promedio_pba = sum (personas['pba'])/ len(personas['pba'])
print (personas['pba'])
print(f'el promedio de edad en pba es : {promedio_pba} años')

for provincia in personas:
    promedio_prov = sum (personas[provincia])/ len(personas[provincia])
    print (provincia, promedio_prov )
    
    
#%%construir un programa que lea el archivo planilla.txt
#y devuelva la frecuencia de registros por provincias


def frecuencia (filename):
    with open (filename,'r') as f:
        provincias = {}
        l= f.readline()
        while l: 
                prov = l.strip().split(',')[-1]
                edad = int(l.split(',')[1])
                if prov in provincias:
                    provincias[prov].append(edad)
                else:
                    provincias[prov] = [edad]
                l= f.readline()
        print(provincias)
        for prov in provincias:
            frecuencia = len(provincias[prov])
            print (prov,frecuencia)

def main ():
    frecuencia('texto_listas.txt')
    
if __name__ == '__main__':
    main()
    




















































