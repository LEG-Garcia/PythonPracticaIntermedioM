'''

Curso: Python Intermedio  
Sección: M
Catedrático: Lic. Fernando Paz

Alumno: Lucía García 

'''

#Ejercicio 1

print("\n------------------------------------------------------------")
print("---------- Precio por la compra de la Fruta ----------------")
print("------------------------------------------------------------")

diccionarioFrutas  = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

nombreFruta = input("\nIngrese el nombre de la fruta : ")
fruta = nombreFruta.title() 
kilo  = float(input("\n¿Cuantos Kilos quiere? "))

if fruta in diccionarioFrutas:
    PrecioUnitario = diccionarioFrutas[fruta]
    total= PrecioUnitario * kilo
    print("\nLos" ,kilo, " Kilos de la ", fruta , "le cuestan : " ,round(total,2), "\n")
else:
    print("\nLa fruta: ", fruta , ", no se tiene en existencia \n")


#Ejercicio dos

print("\n------------------------------------------------------------")
print("---------- Tabla de multiplicar en fichero -----------------")
print("------------------------------------------------------------")

rutaArchivo = 'C:\\xampp\\htdocs\\PythonPracticaIntermedioM\\tabla-n.txt'

tablaMultiplicar = open(rutaArchivo, 'w')

numero = int(input("\nTabla de multiplicar entre 1 y 10, Ingrese el numero  : "))

i= numero
j = 1

if numero < 11:
    tablaMultiplicar.write("\nLa tabla de multiplicar de: " + str(numero) + "\n")
    while j < 11 :
        tablaMultiplicar.write( str(i) + " * " + str(j)  + " = " + str(i * j) + "\n")
        j += 1
    print("\nTabla de multiplicar fue creada en el archio tabla-n.txt")  
else:
    print("El numero: ",numero, " no se encuentra entre 1 y 10 para mostrar su tabla de multiplicar")

tablaMultiplicar.close() 