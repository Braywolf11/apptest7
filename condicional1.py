'''
this scrip let ap`ly basic math operations as:
add, Mult, Subs and div.

1 Ther user must two numbers
2. the user must press and option from menu
3. ther funtion must apply the operation
'''
import os
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
n1 = int(input("First number: "))
n2 = int(input("second number: "))
print ("::: MENU :::")
print ("[1]. Add")
print ("[2]. Subs")
print ("[3]. Mult")
print ("[4]. Div")
opt = int(input("Press an option: "))
print("The answer is: ", calc(n1,n2,opt))