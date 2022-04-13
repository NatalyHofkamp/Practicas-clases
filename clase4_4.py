def print_list (one_list):
    for value in one_list:
        print(value)

def print_reverse(one_list):#imprimir los valores en reversa de una lista
    for i in range (len(one_list)-1,-1,-1):#i tiene los valores de los indices
        print (one_list[i])

def reverse_list(one_list): #ingresar  los valores en reversa de una lista a otra
    output=[]
    for i in range (len(one_list)-1,-1,-1):
        output.apppend(one_list[i])
    
    return output


def func (one_list,number): #busca en la lista un valor, y devuelve
                            #del primero que encuentra, su valor de índice
    for i in range (0,len(one_list)):
        if number == one_list[i]:
            return i
            

def func_2 (one_list,number):   # devuelve el índice del último valor que encnuentre
 result=None
 for i in range (0,len(one_list)):
     if number==one_list[i]:
         result=i
 return result 

def main():
   one_list=[45,32,15,102,'naty']
   print_reverse(one_list)

if __name__=='__main__':
    main()
    
    