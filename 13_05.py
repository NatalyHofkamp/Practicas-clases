#%% RECURSIVIDAD.
#Una palabra es palíndroma si es capicúa, si leída de izquierda a derecha 
#es igual de derecha a izquierda.

def palindroma(palabra):
    if len(palabra) == 0 or len (palabra) == 1:
        return print('es palindroma')
    else :
        