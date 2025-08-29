import numpy as np
class Matrix_opearation():
    def __init__(self,a,):
        self.a=a
        
    def transpose(self):
        e=np.transpose(self.a)
        print("Transpose of a :", e)
    def determinant(self):
        b=np.linalg.det(self.a)
        print("Determinant of a :",b)
    def inverse(self):
        c=np.linalg.inv(self.a)
        print("Inverse of a:",c)
    def eigen_values(self):
        d,f=np.linalg.eig(self.a)
        print("Eigenvalue of a :",d)
        print("Eigenvector of a :",f)
       
a=np.array([[1,2,3,4],[6,7,8,9],[10,11,2,4],[5,7,9,10]])

player=Matrix_opearation(a)
player.transpose()
player.determinant()
player.inverse()
player.eigen_values()
