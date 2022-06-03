class Cosa(object):
    def __init__(self,size):
        self.size = size
class Cartuchera (Cosa):
    def __init__ (self,size,capacidad):
        Cosa.__init__(self,size)
        self.capacidad = capacidad
        self.cosas_dentro = []
    def meter (self,util):
        #que util sea de la clase util
        #util sea de size <=cartuchera.size
        #len(cosas_dentro)<capacidad
        if not isinstance(util,Util):
            print('solo entran útiles')
        elif  util.size > self.size :
            print('el tamaño del util es mayor al de la cartuchera')
        elif len(self.cosas_dentro) >= self.capacidad:
            print('La cartuchera esta llena')
        else:
            self.cosas_dentro.append(util)
    def listar (self):
        self.cosas_dentro= '\n'.join(self.cosas_dentro)
        print(self.cosas_dentro)
    def esta_dentro (self,util):
        return util in self.cosas_dentro
    def quitar(self,util):
        if util in self.cosas_dentro:
            self.cosas_dentro. remove(util)
    def traspasar (self,other):
        for u in other.cosas_dentro:
            self.meter(u)
            other.quitar(u)


class Util(Cosa):
    pass

class Lapiz(Util):
    pass
class Lapicera (Util):
    def __repr__(self) -> str:#lo que se guarda en la lista
        return ('lapiz de tamaño ->' + str(self.size))
    def __str__(self) -> str:#lo que se imprime cuando se invoca
        return ('lapiz de tamaño:' + str(self.size))
class Regla(Util):
    pass


#isinstance(r,regla)-> para saber si y es una instancia de la clase x

#Diseñar la clase Billetera, la billetera tiene capacidad 
#Diseñar la clase Billete, tiene denominacion 1,5,10,50
#Se puede meter billetes en la billetera
#Se puede quitar billetes de la billetera
#Se pide unir billeteras.
#construir una billetera con los billetes de 2 billeteras.
#al fin, las billeteras origen quedan vacias.

#Algoritmo para tener la menor cantidad de billetes.
