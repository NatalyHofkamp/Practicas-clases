meses=(('enero',31), ('febrero',28),('diciembre',31))

for mes,dias in meses:
    print ('el mes', mes, 'tiene', dias, 'dias.')
    
#%% practica de slicing

personas= (('Martin', 'Suarez', 'Ingles'), ('Juana', 'Perez',' Matemática'))

for firstname,lastname,course in personas: 
    print (f"welcome {firstname}{lastname}! this is {course}'s site")
    

#%%
docentes= [('Patricio','perez'), ('jorge','martinez'),('clara','jimenez')]
print ('¿quien es tu profe?')
for i, profe,apellido in enumerate (docentes,-2):
    print (f"{i}. {profe} {apellido}")
    

#%%
doc_teoricas = ["Pato", "Ernesto", "Roberto", "Claudio", "Nacho"]
print("¿Quién es el docente de tus teóricas?")
for i, profe in enumerate(doc_teoricas, 1):
 print(f"{i}. {profe}")

#%% funciones maximos y minimos
list_1=[0,105.2,1]
a= max (list_1)
b=min(list_1)


print (a)
print (b)

#%% conversiones 

test_str=(1,2,(5,6,8))
a =list(test_str)
b=tuple (test_str)
c= str (test_str)
print(a)
print (b)
print (c)

#%% búsqueda

cadena='Hola,cómo estas?'

a= cadena.index ('o')
b= cadena.index ('e')
c= cadena.index ('l')
#d=cadena.index ('h')
e=cadena.find('k')


print(a)
print(b)
print(c)
#print(d)
print(e)

#%% casing 

cadena = "peoPLE caLl Me paTO."

a=cadena.upper()
b=cadena.lower()
c=cadena.title()

print(a)
print(b)
print(c)

#%%
n_maximo = int(input("¿n máximo? "))
suma = 0
for n in range(n_maximo):
 suma += n
print("La suma de 0 a", n_maximo, "es", suma)





















