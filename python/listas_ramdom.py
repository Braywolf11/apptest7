import os
vector = ['Orange','apple','fresa']
n = []
os.system("clear")
print(vector)
print("ther first item in fruts array is : ",vector[0])
print("ther first item in fruts array is : ",vector[2])
vector.append("lemon")
KEY = input("Press any key to continue ...")
print(vector)
print(len(vector))
print("ther first item in fruts array is : ",vector[0])
print("ther first item in fruts array is : ",vector[len(vector)-1])