
def twice_as_old ():
    current_son_age=int(input('ingrese edad del hijo'))
    current_father_age=int(input('ingrese edad del padre'))
    dif= abs(current_son_age*2 - current_father_age)
    return dif

print (twice_as_old())