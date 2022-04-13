# -*- coding: utf-8 -*

    
def match_duration(hours, minutes, seconds):
    """
    Parameters

    hours : TYPE(int)
        este parámetro son las horas que duró el partido expresado en segundos. 
        una hora = 3600 segundos.
    minutes : TYPE (int)
        este parametro son los minutos que duró el partido expresado en segundos. 
        un minuto= 60 segundos
    seconds : TYPE(int)
        este parámetro son los segundos que duró el partido.
        

    Returns 
     
    TYPE(Int)
        La función devolverá la suma de los parámetros insertados expresados 
        en segundos,siendo este el tiempo que duró el partido en total.

    """
    x=hours*3600
    y=minutes*60
    z=seconds
    return (x+y+z) 
    
print ('el partido duró un total de: ', match_duration(11,6,23) , 'segundos')

