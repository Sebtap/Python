                                                    #Estructura Repetitiva
#1. Ingresar 10 números enteros. Mostrar la suma y el promedio.
''''i=0
suma=0
while i<10:
    num=int(input("Ingrese un numero: "))
    suma=suma+num
    i=i+1

promedio=suma/10
print(f"La suma de los 10 enteros ingresados es: {suma}")    
print(f"El promedio de los 10 enteros ingresados es: {promedio}") ''' 

#2. Ingresar 20 números enteros. Determinar e informar la cantidad de valores pares del conjunto
''''i=0
contador=0
def par(num):
    global contador  # Declarar la variable contador como global para poder modificarla sino python la toma como variable local y no estaria declarada
    if num%2==0:
       contador=contador+1 
while i<20:
    num=int(input("Ingrese un numero: "))
    par(num)
    i=i+1

print(f"La cantidad de numeros pares son: {contador}")'''

#3. Ingresar los extremos de un intervalo cerrado; a continuación ingresar 15 valores e informar cuántos pertenecen 
#a ese intervalo
''''i=0
contador=0
extIzq=int(input("Ingrese extremo izquierdo de un intervalo cerrado: "))
extDer=int(input("Ingrese extremo derecho de un intervalo cerrado: "))

def determinar(num):
    global contador
    if num>=extIzq and num<=extDer:
        contador=contador+1
        
while i<15:
    num=int(input("Ingrese un numero: "))
    determinar(num)
    i=i+1

print(f"La cantidad de valores que pertenecen a ese intervalo son: {contador}")'''

#4. Ingresar 20 números naturales, determinar e informar:
#a. El promedio de los valores múltiplos de 3
#b. La cantidad de valores múltiplos de 5
#c. La sumatoria de los valores que se ingresan en orden par.
''''i=0
total=0
contador=0
sumatoria=0

def suma(num):
    global total
    total=total+num

    
while i<15:
    num=int(input("Ingrese un numero natural: "))
    if num%3==0:
        suma(num)
    elif num%5==0:
        contador=contador+1
        
    if num%2==0:
        print(sumatoria)
        sumatoria=sumatoria+1
    i=i+1

promedio=total/15
print(f"El promedio de los valores multiplos de 3 es: {promedio}")
print(f"La cantidad de valores multiplos de 5 es: {contador}")
print(f"La cantidad de valores pares son: {sumatoria}")'''

#5. Ingresar 15 valores enteros entre 0 y 100 y mostrar si está el número 25. Decir en qué posición se encuentra 
#dentro del conjunto empezando con la posición 1. Avisar si no se encuentra. 
#a. Para el caso de que el número 25 esté más de una vez mostrar la posición de la primera vez que aparece 
#dentro del conjunto
#b. Para el caso de que el número 25 esté más de una vez mostrar la posición de la última vez que aparece 
#dentro del conjunto

''''valores = [] # Crear una lista para almacenar los valores

# Solicitar al usuario que ingrese 15 valores enteros entre 0 y 100
for i in range(15):
    valor = int(input("Ingrese un valor entero entre 0 y 100: "))
    # Verificar si el valor está dentro del rango permitido
    if valor < 0 or valor > 100:
        print("El valor ingresado está fuera del rango permitido. Por favor, ingrese un valor entre 0 y 100.")
    else:
        valores.append(valor)

# Verificar si el número 25 está en la lista y mostrar su posición
if 25 in valores:
    primera_posicion = valores.index(25) + 1  # La posición se cuenta desde 1
    print(f"El número 25 está en la posición {primera_posicion} dentro del conjunto.")
else:
    print("El número 25 no se encuentra en el conjunto.")

# Mostrar la posición de la última vez que aparece el número 25
if valores.count(25) > 1:
    ultima_posicion = len(valores) - valores[::-1].index(25)  # Última posición, contando desde 1
    print(f"La última vez que aparece el número 25 es en la posición {ultima_posicion}.")'''
    
#6. Ingresar un número N y un exponente E ambos enteros. Mostrar la potencia E del número
# Solicitar al usuario que ingrese el número N y el exponente E
''''N = int(input("Ingrese el número base (N): "))
E = int(input("Ingrese el exponente (E): "))

potencia = 1 # Inicializar el resultado de la potencia como 1


for i in range(E): # Calcular la potencia de N elevado a E utilizando un bucle
    potencia *= N

# Mostrar el resultado
print(f"La potencia de {N} elevado a {E} es: {potencia}")'''

#7. Escribir un programa que calcule el factorial de un número
''''numero=int(input("Ingrese un numero para calcular factorial: "))
factorial=1
auxiliar=1
for i in range(numero):
    factorial=auxiliar*factorial
    print(factorial)
    auxiliar+=1
   
print(factorial) '''

#8. Ingresar una cantidad desconocida de números enteros entre 1 y 100. Finalizar cuando se ingresa un 0. Mostrar 
#cuántos números se ingresaron sin contar el 0. 
''''num=int(input("Ingresar un numero del 1 al 100: "))
contador=0   
while num!=0:
    num=int(input("Ingresar un numero del 1 al 100: "))
    contador+=1
print(f"La cantidad de numeros ingresados sin contar el cero es: {contador}")   '''
      
#9. Hacer un programa que lea una secuencia de caracteres hasta el punto y cuente las vocales y los espacios en 
#blanco
''''texto=input("Ingrese una secuencia de caracteres: ")
contador=len(texto)
aux=0; aux2=0
texto=texto.lower()
for i in range(contador):
    if texto[i]=='.':
        break
    elif texto[i] in['a','e','i','o','u']:
        aux+=1
    elif texto[i]==' ':
        aux2+=1

print(f"La cantidad de vocales es {aux} y los espacios en blanco son {aux2}")  '''  

#10. Ingresar 10 valores enteros con signo e informar cuál es el máximo y su ubicación dentro del conjunto, 
#comenzando por 1. 
'''lista=[]
listaOrdenada=[]
for i in range(10):
    numero=int(input("Ingrese un numero entero: "))
    lista.append(numero)
    listaOrdenada.append(numero)

listaOrdenada.sort(reverse=True)

for i in range(10):
    if lista[i]==listaOrdenada[0]:
        print(f"El valor maximo y su ubicacion es: {lista[i]} y {i+1}")
        
#otra forma de hacerlo
maximo = float('-inf')  # Inicializamos el máximo con el valor más pequeño posible
ubicacion_maximo = None

for i in range(1, 11):
    numero = int(input(f"Ingrese el valor entero {i}: "))
    lista.append(numero)
    
    # Verificamos si el número ingresado es mayor que el máximo encontrado hasta ahora
    if numero > maximo:
        maximo = numero
        ubicacion_maximo = i

print(f"El valor máximo es: {maximo} y su ubicación en la lista es: {ubicacion_maximo}")
'''        
#12. Ingresar 10 valores enteros con signo e informar cuál es el mínimo y su ubicación dentro del conjunto, 
#comenzando por 1. 
''''minimo=float('+inf') #Inicializamos el minimo con el valor maximo posible
ubicacion_minima= None
lista=[]
for i in range(10):
    numero=int(input("Ingrese un numero entero {i}: "))
    lista.append(numero)
    
    if numero<minimo:
        minimo=numero
        ubicacion_minima=i

print(f"El valor minimo es: {minimo} y su ubicacion esta en: {ubicacion_minima+1}")'''

#13. Ingresar valores enteros con signo hasta que se ingrese un 0. Informar cuál es el máximo y cuál es el mínimo de 
#dichos valores. 
''''maximo=float('-inf')
minimo=float('+inf')
i=1
ubicacion_minima=None
ubicacion_maxima=None
num=int(input("Ingrese un numero entero: "))
while num!=0:
    num=int(input("Ingrese un numero entero: "))
    
    if num<minimo:
        minimo=num
        ubicacion_minima=i
    elif num>maximo:
        maximo=num
        ubicacion_maxima=i
    i+=1    
print(f"El valor minimo es: {minimo} y su ubicacion esta en: {ubicacion_minima+1}")  
print(f"El valor maximo es: {maximo} y su ubicacion esta en: {ubicacion_maxima+1}") '''    

#14. Ingresar un número entero mayor a 0. Debe dibujar un triángulo rectángulo con * con tantas filas como el número 
#indicado. En cada fila se va incrementando la cantidad de asteriscos. Por ejemplo si se ingresa el número 6 debe 
#mostrar en pantalla:
#*
#**
#***
#****
#*****
#******
'''contador=1
num=int(input("Ingrese un numero entero mayor que cero: "))
for i in range(num):
    for i in range(contador):
        print("*", end='')  # Usamos end='' para evitar un salto de línea después de cada asterisco
    print("\n")
    contador+=1
'''

#15. Ingresar un número entero mayor a 0. Debe dibujar una pirámide con * con tantas filas como el número indicado. 
#En cada fila se va incrementando la cantidad de asteriscos de 2 en 2. Por ejemplo si se ingresa el número 5 debe 
#mostrar en pantalla:
#    *
#   ***
#  *****
# *******
#*********

''''contador=1
contador2=1
num=int(input("Ingrese un numero entero mayor que cero: "))
for i in range(num):
    for i in range(num-contador2):
        print(" ",end='')
    for i in range(contador):
        print("*", end='')  # Usamos end='' para evitar un salto de línea después de cada asterisco   
    print("\n")
    contador+=2
    contador2+=1'''

#16. Tomando como base el ejercicio anterior ingresar un número entero mayor a 0 y dibujar un rombo con *. Por 
#ejemplo si se ingresa el número 5 dibuja la pirámide de 5 filas y luego completa el rombo al ir decrementando la 
#cantidad de asteriscos.
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
''''contador=1
contador2=1
num=int(input("Ingrese un numero entero mayor que cero: "))
for i in range(num):
    for i in range(num-contador2):
        print(" ",end='')
    for i in range(contador):
        print("*", end='')  # Usamos end='' para evitar un salto de línea después de cada asterisco   
    print("\n")
    contador+=2
    contador2+=1
  
contador-=4
contador2=1 
for i in range(num-1):
    for i in range(contador2):
        print(" ",end='')
    for i in range(contador):
        print("*", end='')  # Usamos end='' para evitar un salto de línea después de cada asterisco   
    print("\n")
    contador2+=1
    contador-=2'''
    
#17. Realizar un programa que le solicite al usuario el ingreso de una vocal (este dato de ingreso se debe validar). Luego 
#el programa debe exhibir en pantalla la vocal ingresada en cinco líneas y cinco columnas. La vocal debe estar 
#formada en cada carácter por la misma letra en mayúscula.
#El programa finaliza con la letra f.
#Restricciones
#Por cada printf se debe exhibir un solo carácter o salto de línea o espacio.
#Ejemplo
#Ingreso del carácter a
#AAAA
#A  A
#AAAA
#A  A
#A  A
#Ingreso del carácter e
#EEEEE
#E
#EEEEE
#E
#EEEEE
''''contador = 1
vocal = ''  # Inicializar vocal

while vocal!='f':
    vocal = input("Ingrese una vocal (o 'F' para finalizar): ").lower() 
    
    if vocal not in ['a', 'e', 'i', 'o', 'u']:
        print("Por favor, ingrese una vocal válida.")
        continue  # Volver al inicio del bucle si la vocal ingresada no es válida
    
    if vocal == 'a':
        for i in range(5):
            if contador in [1, 3]:
                for i in range(5):
                    print("A", end='')  # Imprimir 'A' sin salto de línea
            else:
                print("A   A")  # Imprimir 'A   A' sin salto de línea
            print()  # Salto de línea al final de cada fila
            contador += 1
'''

#18. Extender el programa anterior para que la vocal se exhiba en n líneas y m columnas ingresadas por teclado.

#19 Se ingresan datos de los empleados de una empresa:
# - Legajo (entero entre 1000 y 5000)
# - Sueldo básico (float mayor a 1000)
# -Antigüedad en años ( mayor o igual a 0)
# -Sexo ( 'M' o 'F')
# -Categoría (entero entre 1 a 5)
#Por cada empleado ingresado se debe calcular el sueldo final a abonar sabiendo que:
# -Las Categorías 2 y 3 tienen $500 de bonificación
# -La Categoría 4 tiene 10% de bonificación
# -La Categoría 5 tiene 30% de bonificación
# -Si la antigüedad es mayor a 10 años recibe una bonificación del 10% adicional
#-Todos los datos ingresados deben ser validados. 
#-El ingreso finaliza con un legajo igual a cero.
#Informar:
# -El sueldo a abonar a cada empleado
# -Cantidad de empleados de más de 10 años de antigüedad
# -El mayor sueldo y el legajo del empleado que cobra dicho sueldo
# -Cantidad de hombres y de mujeres
# Inicializar variables para el análisis
''''empleados_mas_10_anios = 0
mayor_sueldo = float('-inf')
legajo_mayor_sueldo = None
cantidad_hombres = 0
cantidad_mujeres = 0

# Bucle para ingresar datos de empleados
while True:
    # Solicitar datos del empleado
    legajo = int(input("Ingrese el legajo del empleado (o 0 para finalizar): "))
    if legajo == 0:
        break
    
    sueldo_basico = float(input("Ingrese el sueldo básico del empleado: "))
    if sueldo_basico <= 1000:
        print("El sueldo básico debe ser mayor a 1000.")
        continue
    
    antiguedad = int(input("Ingrese la antigüedad en años del empleado: "))
    if antiguedad < 0:
        print("La antigüedad no puede ser negativa.")
        continue
    
    sexo = input("Ingrese el sexo del empleado (M/F): ").upper()
    if sexo not in ['M', 'F']:
        print("El sexo debe ser 'M' o 'F'.")
        continue
    
    categoria = int(input("Ingrese la categoría del empleado (1 a 5): "))
    if categoria not in [1, 2, 3, 4, 5]:
        print("La categoría debe ser un número entre 1 y 5.")
        continue
    
    # Calcular el sueldo final
    bonificacion = 0
    if categoria == 2 or categoria == 3:
        bonificacion += 500
    elif categoria == 4:
        bonificacion += sueldo_basico * 0.10
    elif categoria == 5:
        bonificacion += sueldo_basico * 0.30
    
    if antiguedad > 10:
        bonificacion += sueldo_basico * 0.10
    
    sueldo_final = sueldo_basico + bonificacion
    
    # Actualizar variables para el análisis
    if antiguedad > 10:
        empleados_mas_10_anios += 1
    
    if sexo == 'M':
        cantidad_hombres += 1
    else:
        cantidad_mujeres += 1
    
    if sueldo_final > mayor_sueldo:
        mayor_sueldo = sueldo_final
        legajo_mayor_sueldo = legajo
    
    # Mostrar el sueldo a abonar al empleado
    print(f"Sueldo a abonar al empleado con legajo {legajo}: ${sueldo_final:.2f}")

# Informar los resultados
print(f"Cantidad de empleados con más de 10 años de antigüedad: {empleados_mas_10_anios}")
print(f"Mayor sueldo: ${mayor_sueldo:.2f}, Legajo del empleado: {legajo_mayor_sueldo}")
print(f"Cantidad de hombres: {cantidad_hombres}, Cantidad de mujeres: {cantidad_mujeres}")'''

#20 Un concesionario de automóviles desea registrar los trabajos realizados en su taller a lo largo del 
#día. Para ello por cada cliente que llega se ingresa:
#• DNI del cliente (entero mayor o igual a 1000000)
#• Tipo de vehículo (char donde P indica un vehículo particular y U utilitario)
#• Tipo de trabajo (char donde S indica service de rutina y R reparación)
#• Duración del trabajo (entero mayor o igual a 1 que indica la cantidad de horas de mano de 
#obra empleadas para el trabajo).
#• Costo de Repuestos e Insumos empleados (float igual o mayor a 0)
#La carga finaliza al ingresar un DNI igual a cero. Todos los datos deben estar correctamente 
#validados, si se ingresa un dato incorrecto se lo debe volver a solicitar, mostrando un mensaje 
#indicando que el dato es inválido.
#Si se trata de un service de rutina el costo de la hora de trabajo es de $100 y si es una reparación de 
#$150. 
#Si el vehículo es utilitario al importe final a abonar se le hace un descuento del 20%
#Se desea:
#1. Por cada cliente mostrar el importe final a abonar por el trabajo, detallando el costo de 
#mano de obra y de repuestos/insumos si corresponde.
#2. El porcentaje de reparaciones y de services realizados en el día
#3. Cual fue la reparación más costosa del día (considerar única)
#4. Importe de ganancia total obtenido en el día considerando que sobre los repuestos e 
#insumos se gana un 20% del costo cobrado al cliente y las horas se toman como 100% de 
#ganancia
''''total_services=0
total_reparaciones=0
maxima=float('-inf')
ganancia_total=0
while True:#bucle infinito hasta que lea un break
   
    dni=int(input("Ingrese DNI del cliente mayor o igual a 1000000 (ingrese 0 para terminar la carga de datos): "))
    if dni<1000000 and dni!=0:
        continue
    if dni==0:
        break
   
    tipo_vehiculo=input("Ingrese 'P' para vehiculo particular y 'U' vehiculo utilitario: ")
    if tipo_vehiculo not in['P','U']:
        continue
   
    tipo_trabajo=input("Ingrese 'S' para service de rutina y 'R' reparacion: ")       
    if tipo_trabajo not in['S','R']:
        continue
   
    duracion=int(input("Ingrese la cantidad de horas de mano de obra: "))
    if duracion<1:
        continue
    
    costo_repuestos=float(input("Ingrese de repuestos igual o mayor a 0: "))
    if costo_repuestos<0:
        continue
    
    if tipo_trabajo=='S':
        costo_trabajo=100*duracion
        total_services += 1
    elif tipo_trabajo=='R':
        costo_trabajo=150*duracion
        total_reparaciones +=1
        if costo_trabajo>maxima:
            maxima=costo_trabajo
    
    if tipo_vehiculo=='U':
        costo_total=costo_trabajo+costo_repuestos
        costo_total=costo_total-20*costo_total/100
    elif tipo_vehiculo=='P':
        costo_total=costo_repuestos+costo_trabajo   
    
    ganancia_total+=costo_trabajo+20*costo_repuestos/100 
    print(f"cliente {dni} su importe abonar es {costo_trabajo} con una mano de obra de {costo_trabajo} y repuestos con insumos de {costo_repuestos}")    

  
total_trabajos=total_reparaciones+total_services
# Calcular el porcentaje de reparaciones
porcentaje_reparaciones = (total_reparaciones / total_trabajos) * 100

# Calcular el porcentaje de services
porcentaje_services = (total_services / total_trabajos) * 100

# Mostrar los resultados
print(f"Porcentaje de reparaciones: {porcentaje_reparaciones:.2f}%")
print(f"Porcentaje de services: {porcentaje_services:.2f}%")     
    
print(f"El porcentaje de reparaciones y servicios realizados en el dia es: {porcentaje_reparaciones} y {porcentaje_services}")  
print(f"La reparacion mas costosa del dia fue de {maxima}")
print(f"La ganancia total obtenida en el dia es de: {ganancia_total}")
'''

#21  Un importador de autos de alta gama desea registrar los vehículos recibidos en el último 
#embarque. Por cada vehículo se registra:
#• Marca (char, F para Ferrari, P para porche y L para Lamborghini)
#• Año de fabricación (entero entre 1970 y 2020)
#• Costo del vehículo (float que representa el costo en dólares debe ser mayor o igual a 
#300000)
#• Si está reservado o no (entero donde 1 indica que el vehículo ya estaba reservado 
#previamente y un 0 sino estaba reservado)
#La carga de vehículos finaliza con una marca igual a X. Todos los datos deben estar correctamente 
#validados, si se ingresa un dato incorrecto se lo debe volver a solicitar, mostrando un mensaje 
#indicando que el dato es inválido.
#Se desea: 
#1. Si el vehículo estaba reservado, ingresar el número de teléfono de la persona que realizó la 
#reserva y mostrar por pantalla un mensaje que diga “Llamar a TTT y avisar que su vehículo 
#marca MMM ya ha llegado.” Reemplazar TTT por el número de teléfono y MMM por la 
#marca del vehículo.
#2. Indicar el costo y de que marca fue el vehículo más costoso recibido en el embarque 
#(considerar único)
#3. Indicar cuantos vehículos de cada marca se recibieron
#4. Sabiendo que el costo del transporte en total para todos los vehículos fue de 50000 dólares 
#prorratear el costo entre los vehículos recibidos e indicar cual fue el costo de traer cada 
#vehículo.
''''aux=0;aux2=0;aux3=0;maximo=float('-inf');cantidad_vehiculos=0
while True:
    marca=input("Ingrese marca del vehiculo ('F':Ferrari, 'P':Porche, 'L':Lamborghini y 'X':Salir de la carga de datos) : ")
    if marca not in['F','P','L'] and marca!='X':
        continue
    if marca=='X':
        break
    
    año_fabricacion=int(input("Ingrese año de fabricacion (entre 1970 y 2020): "))
    if año_fabricacion<1970 or año_fabricacion>2020:
        continue
    
    costo_fabricacion=float(input("Ingrese costo en dolares (mayor o igual a 300000): "))
    if costo_fabricacion<300000:
        continue
    
    reservado=int(input("Ingrese si esta reservado el vehiculo (1:reservado y 0:no esta reservado): "))
    if reservado not in[1,0]:
        continue
    
    if reservado==1:
        telefono=int(input("Ingrese el numero de telefono del cliente que realiza la reserva: "))
    
    if costo_fabricacion>maximo:
        maximo=costo_fabricacion
        marca_mas_costoso=marca
        
    if marca=='F':
        aux+=1
    elif marca=='P':
        aux2+=1
    elif marca=='L':
        aux3+=1    
    print(f"Llamar a {telefono} y avisar que su vehiculo marca {marca} ya ha llegado")
    
    cantidad_vehiculos+=1    

print(f"La marca del vehiculo mas costoso es {marca_mas_costoso} con costo total de {maximo}")
print(f"De la marca Ferrari se recibieron: {aux}, de Porche: {aux2} y de Lamborshini: {aux3}")
print(f"El costo de trasporte total es de {cantidad_vehiculos*50000} dolares")
'''

#22  Una panadería dispone de cierta cantidad de kilos de harina para fabricar sus productos. Por cada 
#kilo de harina puede fabricar uno de los siguientes productos: 2 tortas, 36 facturas o 100 panes.
#Al comenzar el programa debe ingresar cuantos kilos de harina hay stock y mostrar cuantos 
#productos de cada tipo podría fabricar con el stock disponible, por ejemplo:
#Con XX kilos de harina puede fabricar:
#XX Totas
#XX Facturas
#XX Panes
#Luego preguntar que quiere fabricar (T: torta, F facturas, P panes) y cuantos kilos de harina va a 
#utilizar para fabricarlos (debe controlar que ingrese un número entre 1 y la cantidad de kilos 
#disponibles). Todos los datos deben estar correctamente validados, si se ingresa un dato incorrecto 
#se lo debe volver a solicitar, mostrando un mensaje indicando que el dato es inválido.
#Mostrar la cantidad fabricada de dicho producto con los kilos de harina elegidos y volver a mostrar 
#la pantalla que indique que es lo que se puede volver a fabricar con lo restante. Se debe continuar 
#el programa hasta que no quede harina disponible o hasta que se ingrese una X en el producto a 
#fabricar.
#Al finalizar mostrar
#1. Cantidad de productos fabricados de cada tipo
#2. La cantidad máxima de harina utilizada en un proceso de fabricación (considerar único)
#3. Si existe aquel o aquellos productos de los cuales no se fabricó ninguna unidad
#4. Si quedó, cuantos kilos de harina no se utilizaron.
''''
harina_stock=int(input("Ingresa la cantidad de harina que hay en stock: "))
cant_tortas=2*harina_stock
cant_facturas=36*harina_stock
cant_panes=100*harina_stock
aux=0;aux2=0;aux3=0;maxima=float('-inf')
print(f"Stock disponible {harina_stock}kg y con esto puede producir {cant_tortas} tortas o {cant_facturas} facturas o {cant_panes} panes")
while True:
    
    opcion=input(("Que quiere fabricar: ('T':tortas, 'F':facturas, 'P':panes y 'X':salir programa): "))
    if opcion=='X':
        break
    elif opcion not in['T','F','P']:
        print("Se ha ingresado un dato incorrecto")
        continue
    
    harina_utilizada=int(input("Cantidad de harina a utilizar de lo que hay disponible: "))
    if harina_utilizada>harina_stock or harina_utilizada<1:
        print("Se ha ingresado un dato incorrecto")
        continue
    
    if opcion=='T':
        aux+=harina_utilizada*2
    elif opcion=='F':
        aux2+=harina_utilizada*36
    elif opcion=='P':
        aux3+=harina_utilizada*100
    
    if harina_utilizada>maxima:
        maxima=harina_utilizada
            
    harina_stock=harina_stock-harina_utilizada
    if harina_stock==0:
        break
    
    
    
    print(f"Stock disponible {harina_stock}kg y con esto puede producir {harina_stock*2} tortas o {harina_stock*36} facturas o {harina_stock*100} panes")
    
print(f"La cantidad de tortas fabricadas es {aux}, de facturas {aux2} y de panes {aux3}")    
print(f"La cantida maxima de harina utilizada en un proceso es: {maxima}kg")
if harina_stock!=0:   
    print(f"Kilos de harina no utilizados {harina_stock}kg")'''

#23 Una panadería especializada en la fabricación de sándwiches de miga desea realizar un sistema 
#de toma de pedidos para el día siguiente. 
#Por cada pedido se ingresa:
#- Código de cliente (entero de 4 cifras)
#- Turno de entrega (M: mañana, T: tarde, N: noche)
#Y luego del detalle de los gustos sándwiches a solicitar ingresando por cada uno:
#- Código (entero de dos dígitos que corresponde al gusto del sándwich)
#- Cantidad
#Luego de ingresar un gusto preguntar si quiere agregar otro gusto al pedido (S/N).
#La carga de pedidos finaliza con un código de cliente igual a 0.
#Todos los datos deben estar correctamente validados, si se ingresa un dato incorrecto se lo debe 
#volver a solicitar, mostrando un mensaje indicando que el dato es inválido.
#Los sandwiches cuyos códigos comiencen con 1, 2 o 3 son gustos clásicos y su precio es de $50 c/u 
#o $550 por docena.
#Los sandwiches cuyos códigos comiencen con 4 o 5 son gustos veganos y su precio es de $75 c/u.
#El resto de los códigos corresponden a sándwiches especiales cuyo precio es de $100 c/u que 
#tienen un descuento del 10% comprando más de 20 unidades.
#Se desea:
#1. Mostrar el importe a pagar en cada pedido
#2. Cual fue la mayor cantidad distinta de gustos solicitados en un mismo pedido (considerar 
#única)
#3. Porcentaje de sándwiches veganos solicitados sobre el total de sándwiches.
#4. Cuantos pedidos se deben entregar en cada turno
# Inicializar variables
max_cantidad_distinta = 0
total_sandwiches = 0
total_veganos = 0
total_mañana = 0
total_tarde = 0
total_noche = 0

# Bucle para ingresar pedidos
while True:
    # Solicitar detalles del pedido
    codigo_cliente = int(input("Ingrese el código de cliente (4 cifras): "))
    if codigo_cliente == 0:
        break
    
    turno_entrega = input("Ingrese el turno de entrega (M: mañana, T: tarde, N: noche): ").upper()
    while turno_entrega not in ['M', 'T', 'N']:
        print("Turno inválido. Intente nuevamente.")
        turno_entrega = input("Ingrese el turno de entrega (M: mañana, T: tarde, N: noche): ").upper()
    
    cantidad_distinta = 0
    precio_pedido = 0
    
    # Detalles de los gustos de sándwiches
    while True:
        codigo_sandwich = int(input("Ingrese el código del sándwich (2 dígitos): "))
        while codigo_sandwich < 10 or codigo_sandwich > 99:
            print("Código de sándwich inválido. Intente nuevamente.")
            codigo_sandwich = int(input("Ingrese el código del sándwich (2 dígitos): "))
        
        cantidad = int(input("Ingrese la cantidad: "))
        while cantidad <= 0:
            print("Cantidad inválida. Intente nuevamente.")
            cantidad = int(input("Ingrese la cantidad: "))
        
        # Calcular importe a pagar por cada sándwich según las condiciones dadas
        if codigo_sandwich >= 10 and codigo_sandwich <= 39:
            precio_sandwich = 50
            if cantidad >= 12:
                precio_sandwich = 550
        elif codigo_sandwich >= 40 and codigo_sandwich <= 59:
            precio_sandwich = 75
        else:
            precio_sandwich = 100
            if cantidad > 20:
                precio_sandwich *= 0.9
        
        precio_pedido += precio_sandwich * cantidad
        cantidad_distinta += 1
        
        respuesta = input("¿Agregar otro sándwich al pedido? (S/N): ").upper()
        if respuesta != 'S':
            break
    
    # Actualizar máximo de cantidad distinta de gustos
    if cantidad_distinta > max_cantidad_distinta:
        max_cantidad_distinta = cantidad_distinta
    
    # Actualizar conteo de sándwiches veganos y totales
    if codigo_sandwich >= 40 and codigo_sandwich <= 59:
        total_veganos += cantidad
    total_sandwiches += cantidad
    
    # Actualizar conteo de pedidos por turno
    if turno_entrega == 'M':
        total_mañana += 1
    elif turno_entrega == 'T':
        total_tarde += 1
    else:
        total_noche += 1
    
    # Mostrar el importe a pagar por el pedido
    print(f"Importe a pagar por el pedido: ${precio_pedido:.2f}")
    
# Calcular porcentaje de sándwiches veganos sobre el total
porcentaje_veganos = (total_veganos / total_sandwiches) * 100

# Mostrar resultados
print(f"Mayor cantidad distinta de gustos solicitados en un mismo pedido: {max_cantidad_distinta}")
print(f"Porcentaje de sándwiches veganos sobre el total: {porcentaje_veganos:.2f}%")
print(f"Cantidad de pedidos para mañana: {total_mañana}")
print(f"Cantidad de pedidos para tarde: {total_tarde}")
print(f"Cantidad de pedidos para noche: {total_noche}")
  
