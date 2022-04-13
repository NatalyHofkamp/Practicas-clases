print(""" *** Welcome to the Super Tennis Annotator app ***
       How do you want to use it?
       
       1-Manual Input
       2-Simulation
       """)

def conver_score(score1,score2,player1,player2):
    if score1==5:
        print (player1,': AD')
        
    elif score1==4:
        print (player1,': 40')

    elif score1==3:
        print (player1,': 30')
    elif score1==2:
        print (player1,': 15')
    elif score1==1:
        print(player1, ': 00')
        
    if score2==5:
        print (player2,': AD')
        
    elif score2==4:
        print (player2,': 40')

    elif score2==3:
        print (player2,': 30')
    elif score2==2:
        print (player2,': 15')
    elif score2==1:
        print(player2, ': 00')
        

def func_ganador(score1,score2,player2,player1,pregunta):
    if score2==4 and score1<3 :
        print (player2)
    elif score1==4 and score2<3:
       print (player1)
    elif score2==5 and score1==4 and pregunta==player2 :
         print (player2)
    elif score1==5 and pregunta==player1 and score2==4:
        print  (player1)
        
def func_logica(score1,player1,player2,score2,pregunta):
   
     if score1==4 and score2<4 and pregunta==player1:
        score1+=1
     elif score2==4 and score1<4 and pregunta==player2:
        score2+=1
     elif score1==5 and score2==4 and pregunta==player2:
        score1=4
        score2=4
     elif score1==4 and score2==5 and pregunta==player1:
        score1=4
        score2=4
     elif score1==4 and score2==4 and pregunta==player1:
        score1=5
     elif score2==4 and score1==4  and pregunta==player2:
        score2=5
     if pregunta== player2:
            score2= score2+1
     elif pregunta == player1:
            score1=score1+1
     else :
       print ('choose one of the players')
        
     return score1,score2 




def func_manual(player1,player2):
    """
    Parameters
    ----------
    player1 : TYPE str
    Este parámeto será el nombre del jugador número1.
     
    player2 : TYPE str
        Este parámeto será el nombre del jugador número2.

    Returns
    -------
    Esta función le dará la opción la usuario de ingresar el nombre 
    del jugador que anotó el punto. Luego, cuando uno de ellos 
    cumpla las condiciones preestablecidas, aparecerá en pantalla
    junto con su nombre 'WINS THE GAME', declarando que es el ganador del juego.
    """
    score1=1
    score2=1
    print('*** Super Tennis Annotator ***')
   
    while score1<=5 and score2<=5 :
        print ('SCORE')
        print (conver_score(score1, score2, player1, player2))
        pregunta= input('who scored?')
        score1,score2= func_logica(score1, player1, player2, score2, pregunta)
    
        
    return  print (func_ganador(score1, score2, player2, player1, pregunta),'WINS THE GAME')
        
       

       
       

def func_simu_full(player1,player2):
    """
    

    Parameters
    ----------
    player1 : TYPE str 
       Este parámeto será el nombre del jugador número1.
    player2 : TYPE str 
       Este parámeto será el nombre del jugador número2.

    Returns
    -------
    Esta función hará la elección al azar entre los jugadores para saber quién
    anotó un punto. Luego imprimirá en pantalla el nombre los jugadores junto con su puntaje
    correspondiente. Finalmente, cuando uno de ellos cumplas las condiciones necesarias, se imprimirá
    en pantalla su nombre junto con 'WIN THE GAME', declarando quue ése jugado es el ganador.
    Luego, el programa finaliza. 

    """
    score1=1
    score2=1
    print('*** Super Tennis Annotator ***')
    
   
    while score1<=5 and score2<=5 :
        print ('SCORE')
        import random 
       
                
        pregunta=random.choice([player1,player2])
        
        func_logica(score1, player1, player2, score2, pregunta)
        print ('WHO SCORED?',pregunta)
        return print (conver_score(score1, score2, player1, player2)) 
       
        
     
def func_simu(player1,player2):
    """
    

    Parameters
    ----------
    player1 : TYPE str
        Este parámeto será el nombre del jugador número1.
    player2 : TYPE str
       Este parámeto será el nombre del jugador número2.

    Returns
    -------
    Esta función hará una elección al azar entre los jugadores 
    ingresados por el usuario. Finalmente, cuando alguno de
    ellos cumpla las condicione necesarias, se imprimirá su nombre
    en pantalla junto con 'WIN THE GAME', explicando que ése jugador
    es el ganador el juego.  Luego, el programa finaliza. 
    """
    score1=1
    score2=1
    
    print('*** Super Tennis Annotator ***')
  
    while score1<=5 and score2<=5 :
        import random 
        pregunta=random.choice([player1,player2])

        func_logica(score1, player1, player2, score2, pregunta)
        return print (conver_score(score1, score2, player1, player2))


def func_main ():
    """
    Returns
    -------
    Esta función será la encargada de dar la presentación al usuario
    sobre el juego y los distintos modos de llevarlo a cabo. 
    Luego, le será solicitado al usuario ingresar el nombre de los jugadores,
    para finalmente ser dirigido al modo de juego que eligió.

    """
   
    choice=int(input('Enter the mode you want to play'))
   
        
    while choice!= 1 and choice!=2:
         
        print (' ##Error-> you must enter a valid value.##')
        choice=int(input('Enter the mode you want to play'))
        
     
    player1=input('Insert player 1')
    player2=input('Insert player 2')
    
    

    if choice==1 :
        func_manual(player1,player2)
     
    elif choice ==2:
        modo_func_simu=int(input(""" Choose how you want to view it
               
               1-See full development
               2-See winner and final score
               """))
        while modo_func_simu!= 1 and modo_func_simu!=2:
              
             print (' ##Error-> you must enter a valid value.##')
             modo_func_simu=int(input(""" Choose how you want to view it
                    
             1-See full development
             2-See winner and final score
                    """))   
                
        if modo_func_simu == 1:
             func_simu_full(player1,player2)
             
        elif modo_func_simu==2:
            func_simu(player1,player2)
            
              
if __name__ == '__main__':
    func_main ()
    



