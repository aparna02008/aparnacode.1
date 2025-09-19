import numpy as np

class matrix_calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self): 
        return self.a/self.b
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[6,1,3]])
    
      


c=matrix_calculator(a,b)
print(c.addition())
print(c.subtraction())
print(c.multiplication())
print(c.division())



