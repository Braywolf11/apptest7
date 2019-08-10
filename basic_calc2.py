#basic calc to junior users
#Developer: Brayan F. Rivera

#libraries###################################
import os
#funtion###################################


###################################··········
def calc(x,y):
    suma = x + y
    print ("la suma es: ", suma)
    
   
#main################################### ····

os.system("clear")  
print("press number 1: ")
a = int (input ()) 

b = int (input ("press number 2: "))


calc(a,b)