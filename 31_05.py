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
#Se puede meter billetes en la billetera.
#Se puede quitar billetes de la billetera.
#Se pide unir billeteras.
#construir una billetera con los billetes de 2 billeteras.
#al fin, las billeteras origen quedan vacias.
#Algoritmo para tener la menor cantidad de billetes.

class Billetera (object):
    def __init__ (self,capacidad):
        self.capacidad = capacidad
        self.cosas_dentro =[]
    def meter  (self,billete):
        if not isinstance(billete,Billete):
            print('La billetera solo acepta billetes')
        elif len (self.cosas_dentro)>= self.capacidad:
            print('la billetera esta llena')
        else:
            self.cosas_dentro.append(billete)
    def quitar (self,billete):
        if billete in self.cosas_dentro:
            self.cosas_dentro.remove(billete)

    def __repr__(self) -> str:
        r= 'billete de capacidad'+str(self.capacidad)+'\n'

        r+= 'Contenido'+str(len(self.cosas_dentro))+'\n'
        for billete in self.cosas_dentro:
            r+=''+billete.__repr__()
        return r 
    def vaciar(self):
        self.cosas_dentro=[]
    #Crear una billetera a partir de otras dos.
    def unir (self,other):
        if not isinstance (other,Billetera):
            print('Solo pueden unirse dos billeteras.')
        nueva = Billetera(self.capacidad+other.capacidad)
        for billete  in self.cosas_dentro:
            nueva.meter(billete)
        self.vaciar()

        for billete in other.cosas_dentro:
            nueva.meter(billete)
        other.vaciar()
        return nueva
    def cambiar(self):
        #dada una billetera con ciertos billetes de denominacion baja,reducir la canti de billetes al minimo conservando el valor.
        billetes ={}
        valor=[50,10,5,1]
        while v>0:
            if v-valor[0] >=0:
                v-=valor[0]
                if valor[0] not in billetes:
                    billetes[valor[0]]=1
                else:
                    billetes[valor[0]]+=1
            else:
                del valor[0]
        for key,value  in billetes.items():
            print(f'hay {value} billetes de {key}')

#%%
#otra forma correcta de cambio
    def cambiar(valor):
        billetes =[]
        denominaciones =[50,10,5,1]
        i=0
        while v>0:
            if v>= denominaciones[i]
                billetes.append(denominaciones[i])
                v-=denominaciones[i]
            else:
                i+=1
        return billetes
    def valor (self):
        v=0
        for billete in self.cosas_dentro:
            v+=billete.denominacion
        return v

    def partir_en_dos (self):
        # crear dos billeteras con los billetes de self.
        #tal que los valores de ambas sean semejantes.

        while i < len (billetes):
            if valores[0]+ billetes[i]<= valores[1]:
                















        billeteras= [Billetera(self.capacidad),Billetera(self.capacidad)]
        billetes ={}
        denominaciones =[50,10,5,1]
        for billete in self.cosas_dentro:
            if billete not in billetes:
                billetes[billete]=1
            else:
                billetes[billetes]+=1

        mitad = self.valor//2

        if mitad - denominaciones[0]>=0 and denominaciones[0]>0 :
            Billetera.meter(denominaciones[0])
            mitad

        return billeteras



class Billete (object):
    #Agregar restriccion para la denominacion
    def __init__(self,denominacion):
        if denominacion not in (1,5,10,50):
            self.denominacion = None
        else:
            self.denominacion = denominacion
    def __repr__(self) -> str:
        return 'Billete de:' +str(self.denominacion)





