import math

#Exercises 1&2

class Fraction:
    def __init__(self,numerator,denominator):
        """Creates a fraction"""
        self.__numerator=numerator
        self.__denominator=denominator
        self.__float=numerator/denominator
    def numerator(self):
        """shows the numerator of the fraction"""
        if not isinstance(self.__numerator,int):
            raise ValueError('The numerator must be an integer')
        return self.__numerator
    def denominator(self):
        """shows the denominator of the fraction"""
        if not isinstance(self.__denominator,int):
            raise ValueError('The denominator must be an integer')
        if self.__denominator==0:
            raise ValueError('the denominator must not be equal to 0')
        return self.__denominator
    def __float__(self):
        """shows the decimal value approaching the fraction"""
        return self.__float
    def __str__(self):
        """shows the fraction created"""
        print ('(',self.numerator(),'/',self.denominator(),')')
    def simplify(self):
        """transforms the fraction so that it is in its smallest form"""
        gcd = math.gcd(self.__numerator, self.__denominator)#we calculate the greatest common divisor in order to simplify the fraction
        self.__numerator=self.__numerator//gcd
        self.__denominator=self.__denominator//gcd
        self.__float=self.__numerator/self.__denominator
        return Fraction(self.__numerator,self.__denominator)
    def add(self,other):
        """adds 2 fractions by replacing the first one by the sum"""
        if not isinstance(other,Fraction):
            raise ValueError('You must apply the add method only with two fractions')
        self.__numerator=self.__numerator*other.__denominator+other.__numerator*self.__denominator
        self.__denominator=self.__denominator*other.__denominator
        self.__float=self.numerator()/self.denominator()
        return Fraction(self.__numerator,self.__denominator)
    def mult(self,other):
        """multiplies 2 fractions by replacing the first one by the product"""
        if not isinstance(other,Fraction):
            raise ValueError('You must apply the mult method only with two fractions')
        self.__numerator=self.__numerator*other.__numerator
        self.__denominator=self.__denominator*other.__denominator
        self.__float=self.numerator()/self.denominator()
        return Fraction(self.__numerator,self.__denominator)


if __name__ == '__main__':
    F=Fraction(2,5) #F cannot be simplified
    G=Fraction(300,90) #G can be simplified
    F.__str__()
    G.__str__()
    F.simplify()
    assert (F.numerator()==2  and F.denominator()==5) 
    G.simplify()
    assert (G.numerator()==10 and G.denominator()==3)
    F.add(Fraction(1,8))
    assert F.numerator()==21
    assert F.denominator()==40
    assert F.__float__()==0.525
    G.mult(Fraction(8,27))
    G.simplify()
    G.__str__()
    assert (G.numerator()==80 and G.denominator()==81)
    G.mult(Fraction(0,2))
    assert G.numerator()==0
    

#Exercise 3    
  
H=Fraction(0,1)
for k in range(1,10000):
    H.add(Fraction(1,k))
print('Harmonic series(10000)=',H.__float__())

#Exercise 4

L=Fraction(0,1)
for k in range(0,10000):
    L.add(Fraction((-1)**k,2*k+1))
print('Leibniz(10000)=',L.__float__())



