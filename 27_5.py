
class cordinate(object):
    def __init__ (self,x,y):
        self.x=x
        self.y =y
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


class rectangulo(object):
    def __init__(self,inicio,alto,ancho):
        self.inicio= cordinate(inicio)
        self.alto = alto
        self.ancho= ancho

    def perimetro(self):
        perimetro = int(self.ancho*2 + self.alto*2)
        return perimetro


    def area(self):
        area = int(self.ancho * self.alto )
        return area

    def dentro(self,punto):
        alto2= self.inicio.y+self.alto 
        ancho2 = self.inicio.x +self.ancho

        if punto.y  self.inicio.x>= punto.y<= alto2 and punto.x<= ancho2 and punto.x>=self.inicio.x :
            return True
        else:
            return False
        
    def __str__(self):
        return 'inicio'+self.inicio+'\n alto' + self.alto
 
 
 a =rectangulo(cordinate(0,0),20,50)