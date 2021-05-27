'''

Curso: Python Intermedio  
Sección: M
Catedrático: Lic. Fernando Paz

Alumno: Lucía García 

'''

# Ejercicio uno

print("\n------------------------------------------------------------")
print("---------------- IVA y Descuento de productos   ------------")
print("------------------------------------------------------------\n")


# ----- Funcion de aplicar descuento ----

def aplicar_descuento (precio, descuento):
    return precio - precio * descuento / 100

#-------- Funcion de Aplicar Iva ---------

def aplicar_iva (precio, iva):
    return precio + precio * iva / 100

#-------- Funcion de cesta ---------
def canasta ( canasta, funcion):
    total = 0
    for precio , descuento in canasta.items():
        total += funcion(precio, descuento)
    return total

# diccionarioProducntosDescuento = {precio : descuento}

precioDecuento = {150.75:5, 200:10, 45:5, 350.50:20}
#                       canasta    ,   funcion 
tdescuento = canasta(precioDecuento,aplicar_descuento)
print("El descuento aplicado a las compras es de: ",tdescuento)

# diccionarioProducntosIva = {precio : iva} el iva en GUATEMALA por producto es el 12%

precioIva = {150.75:12, 200:12, 45:12, 350.50:12}
#              canasta   ,   funcion 
tIva = canasta(precioIva,aplicar_iva)
print("\nEl IVA aplicado a las compras es de: ",tIva)


# Ejercicio dos

print("\n------------------------------------------------------------")
print("-------------------- Elevar lista al cuadrado   ------------")
print("------------------------------------------------------------\n")


def funncion_lista(funcion, lista):
  
    listaVacia = []
    for i in lista:
        listaVacia.append(funcion(i))
    return listaVacia

def elevarAlCuadrado(n):
    return n * n

# lista = [numero, letras]
listaNumeros=[2, 6, 10, 14, 18]
listaAlCuadrado = funncion_lista(elevarAlCuadrado, listaNumeros)
print("Listado : ", listaNumeros)
print("\n Listado elevado al Cuadrado: " , listaAlCuadrado)