'''

Curso: Python Intermedio  
Sección: M
Catedrático: Lic. Fernando Paz

Alumno: Lucía García 

'''

# Ejercicio uno
print("------------------------------------------------------------")
print("--------- Juega adivinando el color de la fruta ------------")
print("------------------------------------------------------------\n")


def colorFruta(turno = 1):
    color  = input("¿Cual es el color de la fruta? ")
    if color != 'naranja':
        if turno < 3:
            print ( "\n" + color + " no es el color de la fruta \n")
            turno += 1 
            colorFruta(turno)
        else:
            print(" \n ¡Perdiste el juego! no adivinaste el color \n")
    else:
        print(" \n ¡Felicitaciones ganaste! Adivinaste el color correcto \n")

colorFruta() 


#Ejercicio dos

print("\n------------------------------------------------------------")
print("----------- Serie Fibonacci Recursivo ----------------------")
print("------------------------------------------------------------\n")

x = input("ingrese el numero del elemento para obtener el fibonacci : ")
numero = int(x)
def fibonacci (n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
resultado = fibonacci(numero)
print("\n El resulatado de fibonacci del numero ",numero,"es", resultado)

print("------------------------------------------------------------")


#ejercicio tres
print("\n------------------------------------------------------------")
print("---------- Factorial de un numero Recursivo ----------------")
print("------------------------------------------------------------\n")

nfactorial = input(" Ingrese el numero factorial a calcular :  ")
numero = int(nfactorial)

def factorial(f):
    if f <= 1:
        return 1
    else:
        return f * factorial(f-1)

rfactorial= factorial(numero)
print(" \n El " ,numero, "! es : ", rfactorial)
print(" \n------------------------------------------------------------")
