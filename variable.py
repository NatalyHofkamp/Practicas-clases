#%% conver_millas1


a=input('Ingrese su nombre')
print(a)

b=int(input('Ingrese las millas a convertir'))
millas=b * 1.609344

print('Bienvenide',a , 'La conversión resulta',millas, 'km')

#%% ejemplo_prof

def Miles_to_km(miles):
    return miles * 1.6

def actividad1():
    print ('Bienvenido, Alvaro')
    miles=input('ingrese las millas a convertir :')
    km=Miles_to_km(float(miles))
    print(f'La conversión resulta :{km} km.')

actividad1() 