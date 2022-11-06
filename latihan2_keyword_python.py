# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:24:18 2022

@author: salim
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:06:41 2022

@author: salim
"""
import keyword
print("The set of keywords in this version is: ")  
print( keyword.kwlist )  

print("=======================================================")
print()
print(4 == 4)  
print(6 > 9)  
print( True or False )  
print( 9 <= 28 )  
print( 6 > 9 )  
print( True and False )  
print("=======================================================")

print( True == 3 )  
print( False == 0 )  
print( True + True + True)  

print("========================================================")

def no_return_function(a,b):  
    num1 = a  
    num2 = b  
    addition = int(num1) + int(num2)  
    
    return addition

number = no_return_function(4,5)  
print(number)  

print("================================")
print()
print( True is True )  
print( False is True )  
print( None is not None )  
print( (9 + 5) is (7 * 2))  
print((5) is (10))
print((5) is (5))

print("===========================================================")
# Program to show the use of keywords for, while, break, continue  
for i in range(15):      
    print( i+ 8, end = " ")          
    # breaking the loop when i = 9  
    if i == 9:  
        break     
print()        
# looping from 1 to 15  
i = 0 # initial condition  
while i < 15:          
    # When i has value 9, loop will jump to next iteration using continue. It will not print  
    if i == 9:  
        i += 3  
        continue  
    else:  
        # when i is not equal to 9, adding 2 and printing the value  
        print( i + 2, end = " ")              
    i += 1  




