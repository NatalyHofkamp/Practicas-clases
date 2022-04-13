#%% ejercicio 11

def greet_msg (name):
    return'Hello,', name

def greet():
    name =input ("Ingrese nombre:")
    msg= greet_msg(name)
    print(msg)  
    
greet()


#%% ejercici0 en clase 

def quarter ():
    mes= int(input('ingrese un mes'))

    if mes<=3 :
        return ('Usted está en Q1')
    elif mes<=6:
        return ('Usted está en Q2')
    elif mes<=9:
        return ('Usted está en Q3')
    elif mes <=12 :
        return ('Usted está en Q4')
    else:
         return 'ingrese un valor válido'
    
print(quarter())


    
    
#%% prueba finger1
hours=11*3600
minutes=6*60
seconds=23
x= hours + minutes + seconds