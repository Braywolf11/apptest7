import os
def palabra() :
    
    fruta = input("Enter the secret word, Please: ")
    letra = fruta[1]
    print (letra)

def jugar() :
    print("bien")

def configuracion() :
    print("bien")


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    
    Titulo = "    :::MENU PRINCIPAL:::   "
    print('-' * len(Titulo))
    print(Titulo)
    print ("1. Ingresar palabra secreta")
    print ("2. Jugar")
    print ("3. Configuración")
    print ("4. Salir")
     
    print ("Digite una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print (palabra())
    elif opcion == 2:
        print (jugar())
    elif opcion == 3:
        print(configuracion())
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
