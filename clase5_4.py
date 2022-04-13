 #%% #define a function that removes from the given array of integers all the 
     #values contained in a second array 

    
def remove_all (array_one,array_two):
    
    #for value in array_one:
        #print (value) #devuelve el valor de cada elemento
        
    #for i in range(0,len(array_one)):#devuelve el valor de cada elemento
     #   print (array_one[i])

    #for index, value in enumerate (array_one):
     #   print (index)
      #  print(value)
    result = []
    
    for value in array_one:
       if value not in array_two:
            result.append(value) #sacar valores de una lista y meterlos en una 
                                 #nueva
    
   # for value in array_one :
    #    for subvalue in array_two:
     #       if value!=subvalue:
      #          result.append(value)
    return result          
            
print (remove_all( [1,2,5,3,8,9,2,2,10,6] , [1,2]))
       

#%% Juntar los elementos de dos listas en una mimsa lista.

list_1=['w','c',1,2,3]
list_2= [6,8,5,9,4]

list_3=[]

for value,subvalue in zip (list_1,list_2):
        list_3.append([value,subvalue])
        
print (list_3)

#%% Juntar los elementos de dos listas en una mimsa lista.

def pair_elements (array_one,array_two):
    
    result=[]
    for elemento_list1,elemento_list2 in zip (array_one,array_two):
        result.append((elemento_list1,elemento_list2))
    return result
    

print (pair_elements (['w','c',1,2,3],[6,8,5,9,4]))

#%% Juntar todos los elementos con todos los otros elementos.

def pair_elements (array_one,array_two):
    result=[]
    
    for value in array_one:
        for subvalue in array_two:
            result.append((value,subvalue))
    return result
print (pair_elements (['w','c','d','f'],[6,8,5,9]))

#%%

list_1= [1,2,3,4]
list_2= ['w','c','d','f']
list_3=[]

for value in list_1:
    for subvalue in list_2:
        list_3.append ((value,subvalue))
        
print (list_3)


 #%% #define a function that removes from the given array of integers all the 
     #values contained in a second array 
     
     
list_1=[1,2,3,5,6,4,8,5,5,3,2,3]
list_2= [3,5]

list_3=[]

for value in list_1:
    if value not in list_2:
        list_3.append(value)

print(list_3)


#%%devuelve el valor de cada elemento

list_1=[1,2,4,5,6,'hola']

for i,value in  enumerate(list_1,1):

    print (f'el elemento numero {i} de la lista vale:{value}')


#%% POSIBLE TP

def main ():
    
    print(f'la palabra que debe adivinar tiene{total_letras}')
    total_letras= len (palabra)
    palabra='pato'
    palabra_adivinada=[]
    letra=input ('Ingrese una letra')
    letra_minus= letra.lower()



def letra_correcta(a):
    
    pass

if __name__=='__main__':
    main()



#%%















