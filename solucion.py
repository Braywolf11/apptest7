import os
from random import randint, uniform, random
def AL(x,y,z):
    while i <= x:
        ansZ = randint(y , z)
        return ansZ

#main###################################···· 
os.system("clear")
n = int(input("data numbers to generate: "))
l1 = int(input("lower limit: "))
l2 = int(input("upper limit: "))
print ("::: MENU :::")
print ("[1]. imprimir")
opt = int(input("Press an option: "))
print("The answer is: ", AL())
