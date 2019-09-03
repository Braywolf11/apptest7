from random import randint, uniform , random
import os

N = []
def getlist(x) :
    i = 1
    while i <= x :
        n = randint(0,100)
        N.append()
        i = i + 1

def showList() :
    i=0
    while i < len(N)-1 :
       print("The numbers in the pos ",i, " is : ", N[i])


##MAIN##############
os.system("clear")
data = int(input("how many random numbres do you to generate?:  "))
getlist(data)
KEY = input("how many random numbres do you to generate?:  ")
showList()