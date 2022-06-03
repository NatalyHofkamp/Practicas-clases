#%% 1)Para cada inciso, implementá una función recursiva que reciba un número z y un entero k y
#retorne.
#Multiplicacion -> z * k

def multiplicar (z,k):
    if k==1:
        return z
    else:
        return z+multiplicar(z,k-1)
    
multiplicar(2,3)
# %% 1. Suma -> z+k

def suma (z,k):
    if k==1:
        return z+1
    else:
        return 1+suma(z,k-1)
suma(2,3)
suma(3,7)

#%%  1. Exponente -> Z^K

def elevar (z,k):
    if k==1:
        return z
    else:
        return z*(elevar(z,k-1))

elevar(2,2)
elevar(4,2)

#%% 2)Implementar una función recursiva que retorne la cantidad de dígitos de un número entero.

def 

#%% 3) Implementar una función recursiva que reciba un entero no negativo y retorne dicho número
#espejado, es decir, para el 1234 retorna 4321.

def reverse_list(n):
    new_list=[]
    n=list(str(n))
    if len(n)==0:
        return''.join(new_list)
    else:
        return  new_list.append (n[-1]), reverse_list(n[:-1])

print(reverse_list(1234))

#%%