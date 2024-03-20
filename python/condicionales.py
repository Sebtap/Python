                                                                        #Decisión

#1 Ingresar dos números A y B y si A>B calcular e informar A - B, en caso contrario A + B.
''''a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))

if a>b:
    print(f"La resta de a-b es: {a-b}")
elif b<a:
    print(f"La suma de a+b es: {a+b}")
else:
    print("Los numeros ingresados son iguales")'''
    
#2 Ingresar un número entero e indicar si es par o impar
''''num=int(input("Ingrese un numero entero: "))

if num%2==0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")'''

#3 Ingresar un carácter e indicar si es o no una vocal, debe considerarse tanto mayúsculas como minúsculas.
''''caracter=input("Ingrese un caracter: ")
caracter=caracter.lower() #CONVIERTE A MINÚSCULA 
if caracter=='a' or caracter=='e' or caracter=='i' or caracter=='0' or caracter=='u':
    print(f"El caracter {caracter} es una vocal")
else:
    print(f"El caracter {caracter} es una consonante")'''
    

#4. Dados tres números enteros, determinar cuál es el mayor siempre y cuando sean distintos. Caso contrario 
#mostrar cuantos números están repetidos.
''''lista=[]
i=0
while(i<3):
    num=int(input("Ingrese un numero entero: "))
    lista.append(num)
    i=i+1
lista.sort(reverse=True) #Ordena la lista de mayor a menor
print(lista)

if lista[0]!=lista[1]:
    print(f"El numero mayor es {lista[0]}")
elif lista[0]==lista[1] and lista[0]==lista[2]:   
    print("Hay 3 numeros repetidos")
elif lista[0]==lista[1] and lista[0]!=lista[2]:
    print("Hay 2 numeros iguales")
else:
    print("Hay 2 numeros iguales")'''

#5. Se lee un número de cinco cifras correspondiente a un boleto de colectivo. Verificar si es o no capicúa.
''''boleto=input("Ingrese un numero entero de 5 cifras: ")

if boleto[0]==boleto[-1] and boleto[1]==boleto[-2]:
    print(f"El numero {boleto} es capicua")
else:
    print(f"El numero {boleto} no es capicua")'''
    
#6. Un producto se vende de a cajas de 15 unidades. Se ingresa la cantidad de unidades vendidas y se debe 
#informar la cantidad de cajas mínimas necesarias para cubrir dicha cantidad.
''''num=int(input("Ingrese cantidad de unidades vendidas: "))
cant=num/15
print(cant)
if cant==int(cant):
    print(f"La cantidad de cajas necesarias es: {int(cant)}")
else:
    print(f"La cantidad de cajas necesaria es {int(cant+1)}")'''


#7. Realizar un programa en cual se ingresen los 3 lados de un triángulo e indique si el mismo es equilátero,
#escaleno o isósceles. El tipo de triangulo debe mostrarse solo en caso de que con los lados ingresados se 
#forme un triángulo (para que sea triángulo la suma de dos de sus lados siempre es mayor que el tercer lado. 
#Esto debe cumplirse para todos los lados)
''''i=0
lista=[]
while i<3:
    num=int(input(f"Ingrese el lado {i+1} del triangulo: "))
    lista.append(num)
    i=i+1
print(lista)
if lista[0]+lista[1]>lista[2] or lista[0]+lista[2]>lista[1] or lista[1]+lista[2]>lista[0]:
    if lista[1]==lista[0] and lista[1]==lista[2]:
        print("El triangulo es equilatero")
    elif lista[1]==lista[0] and lista[1]!=lista[2]:
        print("El triangulo es escaleno")
    elif lista[1]!=lista[0] and lista[1]==lista[2]:
        print("El triangulo es escaleno")
    elif lista[0]==lista[2] and lista[0]!=lista[1]:
        print("El triangulo es escaleno")
    else:
        print("El triangulo es isosceles")
else:
    print("No es un triangulo")'''
    

#8. Ingresar tres letras minúsculas por teclado y mostrarlas en pantalla ordenadas alfabéticamente. 
''''i=0
lista=[]
while i<3:
    letra=input("Ingresa una letra minúscula: ")
    lista.append(letra)
    i=i+1
lista.sort()#ordena la lista alfabeticamente
print(lista)'''


#9. Al efectuar una compra, si adquirimos más de 100 unidades de un mismo artículo, nos hacen un descuento 
#de un 40%; entre 25 y 100 unidades un 20%; entre 10 y 24 unidades un 10% y no hay descuento para menos 
#de 10 unidades. Hacer un programa que calcule el importe a pagar ingresando la cantidad de unidades 
#vendidas y el valor unitario.
''''cantidadUnidades=int(input("Ingrese la cantidad de unidades vendidas: "))
precioProducto=int(input("Ingrese el valor unitario: "))
if cantidadUnidades>100:
    print(f"Importe a pagar {(precioProducto - (40*precioProducto/100))}")
elif cantidadUnidades>=25 and cantidadUnidades<=100:
    print(f"Importe a pagar {(precioProducto - (20*precioProducto/100))}")
elif cantidadUnidades>=10 and cantidadUnidades<=24:
    print(f"Importe a pagar {(precioProducto - (10*precioProducto/100))}")
else:
    print(f"Importe a pagar {precioProducto}")'''

#10. Leer una fecha representada por dos enteros, mes y año, y dar como resultado los días que tiene el mes, 
#teniendo en cuenta los años bisiestos. Un año es bisiesto cuando es múltiplo de 4 y no de 100, o cuando es 
#múltiplo de 400.
''' 
def es_bisiesto(year): #Esta función toma un año como entrada y devuelve True si el año es bisiesto y False si no lo es.
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def dias_del_mes(mes, year):
    """
    Función para obtener el número de días en un mes dado, teniendo en cuenta si el año es bisiesto.
    """
    # Diccionario con el número de días para cada mes
    dias_por_mes = {
        1: 31,  # Enero
        2: 29 if es_bisiesto(year) else 28,  # Febrero
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31, # Octubre
        11: 30, # Noviembre
        12: 31  # Diciembre
    }
    
    return dias_por_mes.get(mes, None)#en caso de no estar el mes, el metodo get devuelve None

# Solicitar al usuario que ingrese el mes y el año
mes = int(input("Ingresa el número del mes (1-12): "))
year = int(input("Ingresa el año: "))

# Obtener el número de días en el mes ingresado
dias = dias_del_mes(mes, year)

# Imprimir el resultado
if dias is not None:
    print(f"El mes {mes} del año {year} tiene {dias} días.")
else:
    print("Mes inválido. Por favor, ingresa un número de mes válido (1-12).")
'''

#11. Se ingresa la altura (en metros) y peso (en kilogramos) de una persona adulta con dichos datos se debe 
#calcular el índice de masa corporal mediante la fórmula: 
#peso / (estatura**2)
#Según el valor obtenido de masa corporal se debe mostrar un carácter indicando el estado de la persona:
# Delgadez: índice de masa corporal <16
# Delgadez Moderada: índice de masa corporal mayor o igual a 16 y menor o igual a 18.49
# Normal: índice de masa corporal mayor a 18,49 menor a 25
# Sobrepeso: índice de masa corporal mayor o igual a 25 y menor a 30
# Obesidad: índice de masa corporal mayor o igual a 30
''''altura=float(input("Ingrese la altura en metros: "))
peso=float(input("Ingrese el peso en kilogramos: "))
indiceMasaCorporal=peso/altura**2
print(indiceMasaCorporal)
if indiceMasaCorporal<16:
    print("delgadez")
elif indiceMasaCorporal>=16 and indiceMasaCorporal<=18.49:
    print("delfadez moderada")
elif indiceMasaCorporal>=18.49 and indiceMasaCorporal<25:
    print("Normal")
elif indiceMasaCorporal>=25 and indiceMasaCorporal<30:
    print("Sobrepeso")
elif indiceMasaCorporal>=30:
    print("Obesidad")'''
    
#12. Realizar un programa que, por medio de un menú, realice la suma, resta, multiplicación o división de dos 
#números enteros ingresados por teclado. 
''''def sumar(num1,num2):
    print(f"La suma de los numeros es: {num1+num2}\n")
    
def resta(num1,num2):
    print(f"La resta de los numeros es: {num1-num2}\n")

def multiplicar(num1,num2):
    print(f"La multiplicacion de los numeros es: {num1*num2}\n")

def dividir(num1,num2):
    print(f"La division de los numeros es: {num1/num2}\n")

num1=float(input("Ingrese el primer numero: "))      
num2=float(input("Ingrese el segundo numero: "))

while True:
    print("-------------MENU------------")
    print("Seleccione 1 para sumar ")
    print("Seleccione 2 para restar ")
    print("Seleccione 3 para multiplicar ")
    print("Seleccione 4 para dividir ")
    print("Seleccione 5 para salir ")
    
    opcion=int(input("Ingrese opcion: "))
    if opcion==1:
        sumar(num1,num2)
    elif opcion==2:
        resta(num1,num2)
    elif opcion==3:
        multiplicar(num1,num2)
    elif opcion==4:
        dividir(num1,num2)
    elif opcion==5:
        break
    else:
        print("Ingresaste un numero incorrecto")
'''

#13. Realizar un programa que ingresando el precio de un producto y el medio de pago permita calcular el 
#importe final a abonar:
# Si el medio de pago es E que equivale a afectivo se le descuenta el 10%
# Si el medio de pago es D que equivale a tarjeta de débito se le descuenta el 3.5%
# Si el medio de pago es C que equivale a tarjeta de crédito tiene un incremento del 5%
# Si el medio de pago es T que equivale a tickets el importe no sufre modificacione
''''precioProducto=float(input("Ingrese el precio del producto: "))
medioPago=input("Ingrese el medio de pago E D C o T: ")
medioPago=medioPago.upper()
if medioPago=="E":
    print(f"Total a pagar {(precioProducto - (10*precioProducto/100))}")
elif medioPago=="D":
    print(f"Total a pagar {(precioProducto - (3.5*precioProducto/100))}")
elif medioPago=="C":
    print(f"Total a pagar {(precioProducto + (5*precioProducto/100))}")
elif medioPago=="T":
    print(f"Total a pagar {precioProducto}")'''