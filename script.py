import numpy as np 
from sympy import * 
class matrix: 
    def __init__(self, order:float ,elements:list) :
        self.order = order 
        self.elements = np.array(elements)
            
            
    #def matrix_elements(order):
    
    #    for u in range(1, (order*order)+1):
    #        elements = []
    #        x = elements.append(int(input('Enter matrix:')))
        
    #     return x 
    def calculate_dtr(self):
        
        if (self.order == 2 ): 
            dtr = (self.elements[0][0]*self.elements[1][1])-(self.elements[0][1]*self.elements[1][0])
            return dtr
        if (self.order == 3 ): 
            dtr = {(self.elements[0][0]*self.elements[1][1]*self.elements[2][2])+(self.elements[0][1]*self.elements[1][2]*self.elements[2][0])
            + (self.elements[0][2]*self.elements[1][0]*self.elements[2][1])-(self.elements[0][2]*self.elements[1][1]*self.elements[2][0])
            -(self.elements[0][1]*self.elements[1][0]*self.elements[2][2])-(self.elements[0][0]*self.elements[1][2]*self.elements[2][1])}
            for u in dtr:
                y = u 
            return y
    
    def check_col(self, dtr):
        if (self.order==3 and self.elements[0][2]==1 and self.elements[1][2]==1 and self.elements[2][2]==1):
            if (dtr==0.0):
                return 'Puncte coliniare'
            else:
                return'Puncte necoliniare'
        else: 
            return'Last column must contain only 1 values'
    def trg_area(self, dtr):
        dtr = abs(dtr)
        arr = dtr / 2  
        return arr
    def power(self):
        x = int(input('What power to raise the matrix to: '))
        y = np.copy(self.elements)
        result = np.copy(self.elements)
        p=int(2) 
        while(p<=x):
            for line in range(0, self.order):
                for column in range(0, self.order): 
                    resul = 0.0
                    for element in range(0, self.order):
                        
                        resul += ( float(self.elements[line, element])  * float(y[element, column]))
                        
                        result[line, column] = resul
                        
            self.elements = np.copy(result)
            
            p = p+1
        return result 
                            
            
        


def select_function(m):
    while(True):
        switch = str(input('Enter:\n 1 for calculating determinant \n 2 for checking if points are coliniar\n 3 for calculating area of triangle\n 4 for finding the power\n 0 for exiting program\n'))
        if (switch == '1'):
            print(f"The determinant is: {m.calculate_dtr()}")
        if (switch == '2'):
            print(m.check_col(m.calculate_dtr()))
        if (switch == '3'):
            print (f'The area is {m.trg_area(m.calculate_dtr())}')
        if (switch == '4'):
            print (m.power())
        if (switch == '0'):
            return 1 
      
      

         
x = int(input('Enter order: '))
y =[]

for u in range(1, (x*x)+1):
    y.append(float(input('Enter matrix:')))
# print(y)
matrix1 = matrix(x,y)
#matrix1 = matrix (3, [[1,0,1],[0,1,0],[1,0,1]])
matrix1.elements = matrix1.elements.reshape(3,3)
#print(matrix1.elements)


#print(matrix1.power())

select_function( matrix1)


