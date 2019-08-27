import os
from random import randint, uniform, random
# This funtion generates integer numbers
def Z():
    ansZ = randint(0 , 100)
    return ansZ


# This funtion generates integer numbers
def R():
    ansR = uniform(0 , 100)
    return ansR
#MAIN
os.system("clear")
print ("The integer random nimber is : ", Z())
r = R()
print ("The integer random nimber is : ", r)

'''
#main###################################····
def calc (x,y,z):
    if z == 1 :
        ans = x + y
    elif z == 2 :
        ans = x - y
    elif z == 3 : 
        ans = x * y 
    else:
        ans = x / y
    return ans

#main###################################···· 
os.system("clear")
n1 = int(input("data numbers to generate: "))
n2 = int(input("second number: "))
n2 = int(input("second number: "))
print ("::: MENU :::")
print ("[1]. Add")
print ("[2]. Subs")
print ("[3]. Mult")
print ("[4]. Div")
opt = int(input("Press an option: "))
print("The answer is: ", calc(n1,n2,opt))
'''